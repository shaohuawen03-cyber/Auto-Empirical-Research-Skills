#!/usr/bin/env python3
"""Deterministic content and OOXML audit for the final SCI deliverables."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import re
import zipfile
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT_MD = ROOT / "manuscript" / "manuscript_sci_final.md"
MANUSCRIPT_DOCX = ROOT / "manuscript" / "manuscript_sci_final.docx"
SUPPLEMENT_MD = ROOT / "manuscript" / "supplementary_tables_sci_final.md"
SUPPLEMENT_DOCX = ROOT / "manuscript" / "supplementary_tables_sci_final.docx"
REPORT = ROOT / "quality_reports" / "sci_final_audit.json"
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def expand_citations(text: str) -> set[int]:
    found: set[int] = set()
    for raw in re.findall(r"\[([0-9,–\- ]+)\]", text):
        for part in raw.split(","):
            part = part.strip()
            if "–" in part or "-" in part:
                chunks = re.split(r"[–-]", part)
                if len(chunks) == 2 and all(chunk.strip().isdigit() for chunk in chunks):
                    lo, hi = map(int, chunks)
                    found.update(range(lo, hi + 1))
            elif part.isdigit():
                found.add(int(part))
    return found


def audit_three_line_tables(root: ET.Element) -> dict:
    tables = root.findall(f".//{W}tbl")
    details = []
    for index, table in enumerate(tables, start=1):
        tbl_borders = table.find(f"./{W}tblPr/{W}tblBorders")
        checks = {
            "top_rule": False,
            "bottom_rule": False,
            "left_rule_absent": False,
            "right_rule_absent": False,
            "inside_horizontal_absent": False,
            "inside_vertical_absent": False,
            "header_separator": False,
            "no_shading": not bool(table.findall(f".//{W}shd")),
        }
        if tbl_borders is not None:
            for name, key, desired in [
                ("top", "top_rule", "single"),
                ("bottom", "bottom_rule", "single"),
                ("left", "left_rule_absent", "nil"),
                ("right", "right_rule_absent", "nil"),
                ("insideH", "inside_horizontal_absent", "nil"),
                ("insideV", "inside_vertical_absent", "nil"),
            ]:
                node = tbl_borders.find(f"{W}{name}")
                checks[key] = node is not None and node.attrib.get(f"{W}val") == desired
        first_row = table.find(f"./{W}tr")
        if first_row is not None:
            header_cells = first_row.findall(f"./{W}tc")
            checks["header_separator"] = bool(header_cells) and all(
                (bottom := cell.find(f"./{W}tcPr/{W}tcBorders/{W}bottom")) is not None
                and bottom.attrib.get(f"{W}val") == "single"
                for cell in header_cells
            )
        details.append({"table": index, **checks, "pass": all(checks.values())})
    return {"count": len(tables), "details": details, "all_pass": bool(tables) and all(item["pass"] for item in details)}


def audit_docx(path: Path, expected_tables: int, expected_references: int) -> dict:
    with zipfile.ZipFile(path) as archive:
        bad_crc = archive.testzip()
        names = set(archive.namelist())
        document_bytes = archive.read("word/document.xml")
        styles_bytes = archive.read("word/styles.xml")
        core_bytes = archive.read("docProps/core.xml")
    root = ET.fromstring(document_bytes)
    ET.fromstring(styles_bytes)
    ET.fromstring(core_bytes)
    table_audit = audit_three_line_tables(root)
    text = "".join(node.text or "" for node in root.iter(f"{W}t"))
    reference_paragraphs = 0
    for paragraph in root.findall(f".//{W}p"):
        pstyle = paragraph.find(f"./{W}pPr/{W}pStyle")
        if pstyle is not None and pstyle.attrib.get(f"{W}val") == "Reference":
            reference_paragraphs += 1
    line_numbering = root.find(f".//{W}sectPr/{W}lnNumType") is not None
    footer_reference = root.find(f".//{W}sectPr/{W}footerReference") is not None
    no_revision_markup = not any(
        root.findall(f".//{W}{tag}") for tag in ("ins", "del", "moveFrom", "moveTo", "commentReference")
    )
    no_comments_part = not any(name.startswith("word/comments") for name in names)
    no_personal_creator = b"<dc:creator></dc:creator>" in core_bytes and b"<cp:lastModifiedBy></cp:lastModifiedBy>" in core_bytes
    return {
        "path": str(path.relative_to(ROOT)),
        "sha256": digest(path),
        "zip_crc_ok": bad_crc is None,
        "xml_parse_ok": True,
        "table_count": table_audit["count"],
        "expected_table_count": expected_tables,
        "table_count_ok": table_audit["count"] == expected_tables,
        "three_line_tables": table_audit,
        "reference_paragraph_count": reference_paragraphs,
        "expected_reference_count": expected_references,
        "reference_count_ok": reference_paragraphs == expected_references,
        "line_numbering": line_numbering,
        "page_number_footer": footer_reference,
        "no_revision_markup": no_revision_markup and no_comments_part,
        "anonymised_core_metadata": no_personal_creator,
        "forbidden_placeholder_absent": "AUTHOR_INPUT_NEEDED" not in text,
    }


def main() -> None:
    manuscript = MANUSCRIPT_MD.read_text(encoding="utf-8")
    supplement = SUPPLEMENT_MD.read_text(encoding="utf-8")
    body, references = manuscript.split("## References", 1)
    reference_numbers = [int(value) for value in re.findall(r"(?m)^(\d+)\. ", references)]
    cited = expand_citations(body)
    expected = set(range(1, 43))
    forbidden = [
        "AUTHOR_INPUT_NEEDED",
        "ZZL-Zoro",
        "GSE42872",
        "project’s",
        "source-docs",
        "Fig. ",
        "Confirm author line",
    ]
    content_checks = {
        "reference_sequence_1_to_42": reference_numbers == list(range(1, 43)),
        "all_listed_references_cited": cited == expected,
        "cited_reference_numbers": sorted(cited),
        "uncited_reference_numbers": sorted(expected - cited),
        "out_of_range_citations": sorted(cited - expected),
        "main_table_count_is_5": len(re.findall(r"(?m)^\| .+ \|$", manuscript)) > 5 and manuscript.count("**Table ") == 5,
        "supplement_table_count_is_5": supplement.count("## Supplementary Table S") == 5,
        "placeholder_and_workflow_tokens_absent": not any(token in manuscript for token in forbidden),
        "reference_23_author_verified": "23. Li J, Lian T, Guo P, Li J, Qi J, He M, et al." in references,
        "reference_31_pages_corrected": "Cell. 2019;178(1):242–260.e29." in references,
        "reference_33_author_line_corrected": "Belstrøm D, Constancias F, Drautz-Moses DI, Schuster SC, Veleba M, Mahé F, et al." in references,
        "irrelevant_melanoma_reference_removed": "10.1158/2159-8290" not in references,
        "all_dois_present": len(re.findall(r"doi:10\.", references, flags=re.I)) == 42,
        "scientific_boundaries_present": all(
            phrase in manuscript
            for phrase in [
                "do not establish taxonomic origin, brain exposure, binding affinity, neurotoxicity, or an AD mechanism",
                "no dynamic-stability claim is made",
                "does not support assignment of the candidates to *P. gingivalis*",
            ]
        ),
    }
    docx_checks = {
        "manuscript": audit_docx(MANUSCRIPT_DOCX, expected_tables=5, expected_references=42),
        "supplement": audit_docx(SUPPLEMENT_DOCX, expected_tables=5, expected_references=0),
    }
    content_pass = all(value for key, value in content_checks.items() if isinstance(value, bool))
    docx_pass = all(
        package["zip_crc_ok"]
        and package["xml_parse_ok"]
        and package["table_count_ok"]
        and package["three_line_tables"]["all_pass"]
        and package["reference_count_ok"]
        and package["line_numbering"]
        and package["page_number_footer"]
        and package["no_revision_markup"]
        and package["anonymised_core_metadata"]
        and package["forbidden_placeholder_absent"]
        for package in docx_checks.values()
    )
    report = {
        "schema": "local.sci_final_audit.v1",
        "content": content_checks,
        "docx": docx_checks,
        "content_pass": content_pass,
        "docx_pass": docx_pass,
        "verdict": "PASS" if content_pass and docx_pass else "FAIL",
        "boundary": "Structural OOXML and deterministic content audit; journal-specific rendering and author declarations still require accountable-author review.",
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(REPORT)
    print(report["verdict"])
    if report["verdict"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
