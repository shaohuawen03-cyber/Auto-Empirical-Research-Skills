#!/usr/bin/env python3
"""v0.5 deterministic audit suite (adapted from the Light-skills submission-grade pipeline).

Emits JSON reports under quality_reports/:
  manuscript_consistency.json     core numbers, prohibited claims, reference sequence 1-43
  language_structure_audit.json   8 parallel H2 sections, citation coverage, placeholders
  citation_inventory_audit.json   DOI parity across EN/ZH/verified/bib (bib may be a documented superset)
  manuscript_word_count.json      journal-neutral word-count estimate
  docx_package_audit.json         ZIP integrity, XML parse, paragraph/table/media counts
All scripts use the Python standard library only.
"""
from __future__ import annotations

import hashlib
import json
import re
import zipfile
from pathlib import Path
from xml.dom import minidom

ROOT = Path(__file__).resolve().parents[1]
EN = ROOT / "manuscript" / "manuscript_en.md"
ZH = ROOT / "manuscript" / "manuscript_zh.md"
VERIFIED = ROOT / "references" / "verified_references.md"
BIB = ROOT / "manuscript" / "references.bib"
QC = ROOT / "quality_reports"
QC.mkdir(parents=True, exist_ok=True)

N_REFERENCES = 43

EXPECTED = [
    "11,269,961", "11,721,988", "31,510", "33,786", "30,557", "32,754",
    "3,359", "3,446", "953", "1,032", "40", "72", "3,518", "3,299",
    "219", "923", "111", "15", "12", "8", "10.99", "10.52", "4.20",
    "6.98", "83.95", "0.2796", "0.2882", "2,893", "547",
    "\u22129.60", "\u22129.49", "\u22129.29", "\u22129.27", "\u22129.03",
    "\u22129.01", "\u22128.94", "\u22128.91", "\u22128.88", "\u22128.35",
    "\u22128.25", "FLLHTTR", "YLSLLQR", "ALLLHRC", "FCLHLQLR", "YHHLLCRR",
    "LLHLPKRTT", "LLHPLRL", "WLLVHLKK", "LLHPLRC", "HLLTLKKHV",
    "HLPLLHRCC", "HVLLLRQCA",
]

PROHIBITED_EN = {
    "identified periodontitis-specific": "Disease specificity is not established.",
    "p. gingivalis-derived candidates": "Taxonomic origin is not established.",
    "proved that": "Causal/mechanistic proof is not available.",
    "demonstrated that the candidates": "Candidate mechanism is not validated.",
    "experimentally confirmed": "No wet validation was performed.",
}
PROHIBITED_ZH = {
    "牙周炎特异性微肽": "未建立疾病特异性。",
    "牙龈卟啉单胞菌来源候选": "未建立分类学来源。",
    "证明这些候选": "未完成机制验证。",
    "证实这些候选": "未完成机制验证。",
    "实验证实": "未进行湿实验验证。",
}

PLACEHOLDER_RE = re.compile(r"\b(?:TODO|TBD|RESULT GAP|MATERIAL GAP)\b", re.I)
CITATION_RE = re.compile(r"\[([0-9,;\-\u2013\u2014\s]+)\]")
DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.I)
TRAILING = ".,;:)]}"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(name: str, obj: dict) -> None:
    (QC / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def citation_numbers(body: str) -> list[int]:
    found: set[int] = set()
    for match in CITATION_RE.finditer(body):
        for part in re.split(r"[,;]", match.group(1)):
            part = part.strip()
            span = re.fullmatch(r"(\d+)\s*[-\u2013\u2014]\s*(\d+)", part)
            if span:
                start, end = map(int, span.groups())
                found.update(range(min(start, end), max(start, end) + 1))
            elif part.isdigit():
                found.add(int(part))
    return sorted(found)


def audit_consistency() -> str:
    results = {}
    for lang, path, ref_heading in (("english", EN, "## References"), ("chinese", ZH, "## 参考文献")):
        text = path.read_text(encoding="utf-8")
        body = text.split(ref_heading, 1)[0]
        missing = [v for v in EXPECTED if v not in text]
        prohibited = PROHIBITED_EN if lang == "english" else PROHIBITED_ZH
        hits = [{"phrase": p, "reason": r} for p, r in prohibited.items()
                if (p in body.lower() if lang == "english" else p in body)]
        ref_block = text.split(ref_heading, 1)[1]
        nums = [int(n) for n in re.findall(r"(?m)^(\d+)\.\s", ref_block)]
        results[lang] = {
            "path": str(path.relative_to(ROOT)),
            "sha256": sha256(path),
            "missing_expected_values": missing,
            "prohibited_claim_hits": hits,
            "reference_numbers_sequential_1_to_43": nums == list(range(1, N_REFERENCES + 1)),
        }
    checks = {
        "schema": "local.manuscript_consistency.v1",
        **results,
        "core_value_presence_bilingual": not results["english"]["missing_expected_values"]
        and not results["chinese"]["missing_expected_values"],
        "prohibited_claims_absent": not results["english"]["prohibited_claim_hits"]
        and not results["chinese"]["prohibited_claim_hits"],
        "references_sequential_bilingual": results["english"]["reference_numbers_sequential_1_to_43"]
        and results["chinese"]["reference_numbers_sequential_1_to_43"],
    }
    checks["verdict"] = "PASS" if all(v for k, v in checks.items() if isinstance(v, bool)) else "FAIL"
    write("manuscript_consistency.json", checks)
    return checks["verdict"]


def audit_structure() -> str:
    report = {}
    for lang, path, ref_heading in (("en", EN, "## References"), ("zh", ZH, "## 参考文献")):
        text = path.read_text(encoding="utf-8")
        body = text.split(ref_heading, 1)[0]
        sections = re.findall(r"(?m)^##\s+(.+?)\s*$", text)
        cited = citation_numbers(body)
        report[lang] = {
            "h2_sections": sections,
            "h2_section_count": len(sections),
            "cited_before_reference_list": cited,
            "all_1_to_43_cited": cited == list(range(1, N_REFERENCES + 1)),
            "placeholder_count": len(PLACEHOLDER_RE.findall(text)),
            "author_input_needed_markers": len(re.findall(r"AUTHOR_INPUT_NEEDED", text)),
        }
    ok = (
        report["en"]["h2_section_count"] == report["zh"]["h2_section_count"] == 8
        and report["en"]["all_1_to_43_cited"] and report["zh"]["all_1_to_43_cited"]
        and report["en"]["placeholder_count"] == report["zh"]["placeholder_count"] == 0
    )
    out = {"schema": "local.language_structure_audit.v1", **report, "verdict": "PASS" if ok else "FAIL"}
    write("language_structure_audit.json", out)
    return out["verdict"]


def audit_citations() -> str:
    def dois(text: str) -> set[str]:
        return {m.group(0).rstrip(TRAILING).lower() for m in DOI_RE.finditer(text)}

    sets = {
        "manuscript_en": dois(EN.read_text(encoding="utf-8")),
        "manuscript_zh": dois(ZH.read_text(encoding="utf-8")),
        "verified_references": dois(VERIFIED.read_text(encoding="utf-8")) if VERIFIED.exists() else set(),
        "bibtex": dois(BIB.read_text(encoding="utf-8")),
    }
    canonical = sets["manuscript_en"]
    en_zh_parity = sets["manuscript_en"] == sets["manuscript_zh"]
    verified_parity = sets["verified_references"] == canonical
    bib_superset = canonical <= sets["bibtex"]
    bib_extra = sorted(sets["bibtex"] - canonical)
    ok = en_zh_parity and verified_parity and bib_superset and len(canonical) == N_REFERENCES
    out = {
        "schema": "local.citation_inventory_audit.v1",
        "canonical_count": len(canonical),
        "canonical_count_is_43": len(canonical) == N_REFERENCES,
        "english_chinese_doi_parity": en_zh_parity,
        "verified_references_parity": verified_parity,
        "bibtex_is_superset_of_manuscript_dois": bib_superset,
        "bibtex_extra_dois_not_cited_in_manuscript": bib_extra,
        "verification_boundary": "Inventory parity only; final Crossmark/retraction screening remains required.",
        "verdict": "PASS" if ok else "FAIL",
    }
    write("citation_inventory_audit.json", out)
    return out["verdict"]


TOKEN_RE = re.compile(
    r"[^\W\d_]+(?:[-\u2013\u2014\u2019'][^\W\d_]+)*|"
    r"\d+(?:[,.]\d+)*(?:%|[A-Za-z]+)?|"
    r"[A-Za-z]*\d+[A-Za-z0-9]*"
)
IMAGE_RE = re.compile(r"!\[[^]]*\]\([^)]*\)")


def count(text: str) -> int:
    return len(TOKEN_RE.findall(IMAGE_RE.sub("", text)))


def audit_word_count() -> str:
    text = EN.read_text(encoding="utf-8")
    abstract = text.split("## Abstract", 1)[1].split("**Keywords:**", 1)[0]
    main = text.split("## 1. Introduction", 1)[1]
    out = {
        "schema": "local.manuscript_word_count.v1",
        "source": "manuscript/manuscript_en.md",
        "structured_abstract_excluding_keywords": count(abstract),
        "main_text_introduction_through_conclusions": count(main.split("## Declarations", 1)[0]),
        "main_text_including_declarations_excluding_references": count(main.split("## References", 1)[0]),
        "counting_boundary": "Journal-neutral regex estimate; recount after target-journal formatting.",
        "verdict": "INFORMATIONAL",
    }
    write("manuscript_word_count.json", out)
    return "INFORMATIONAL"


def audit_docx() -> str:
    records = {}
    for name in ("manuscript_bilingual.docx", "supplementary_tables_bilingual.docx"):
        path = ROOT / "manuscript" / name
        info: dict = {"path": str(path.relative_to(ROOT)), "sha256": sha256(path)}
        with zipfile.ZipFile(path) as zf:
            bad = zf.testzip()
            info["zip_crc_ok"] = bad is None
            xml_text = zf.read("word/document.xml").decode("utf-8")
            info["document_xml_parses"] = True
            try:
                minidom.parseString(xml_text)
            except Exception as exc:  # noqa: BLE001
                info["document_xml_parses"] = False
                info["xml_error"] = str(exc)
            info["paragraph_count"] = xml_text.count("<w:p ") + xml_text.count("<w:p>")
            info["table_count"] = xml_text.count("<w:tbl>")
            info["drawing_count"] = xml_text.count("<w:drawing>")
            info["media_files"] = [n for n in zf.namelist() if n.startswith("word/media/")]
        records[name] = info
    ok = all(r["zip_crc_ok"] and r["document_xml_parses"] for r in records.values())
    out = {"schema": "local.docx_package_audit.v1", "packages": records,
           "rendering_boundary": "No Word/LibreOffice renderer in this environment; page-level visual review is the author's task.",
           "verdict": "PASS" if ok else "FAIL"}
    write("docx_package_audit.json", out)
    return out["verdict"]


def main() -> int:
    verdicts = {
        "manuscript_consistency": audit_consistency(),
        "language_structure": audit_structure(),
        "citation_inventory": audit_citations(),
        "word_count": audit_word_count(),
        "docx_package": audit_docx(),
    }
    print(json.dumps(verdicts, indent=2))
    return 0 if all(v in ("PASS", "INFORMATIONAL") for v in verdicts.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
