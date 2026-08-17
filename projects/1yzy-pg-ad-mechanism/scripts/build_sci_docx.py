#!/usr/bin/env python3
"""Create an anonymised, journal-style DOCX with genuine three-line tables.

This dependency-free builder emits a standards-compliant OOXML package. It is
purpose-built for the final English manuscript and supplementary tables:
A4 paper, Times New Roman, reviewer line/page numbering, Vancouver references,
and tables with only top, header-separator, and bottom rules.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from html import escape
from pathlib import Path
import re
import zipfile

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"


def xml_escape(text: str) -> str:
    return escape(text, quote=True)


def run_xml(
    text: str,
    *,
    bold: bool = False,
    italic: bool = False,
    code: bool = False,
    size: int | None = None,
) -> str:
    if not text:
        return ""
    props: list[str] = []
    if bold:
        props.append("<w:b/><w:bCs/>")
    if italic:
        props.append("<w:i/><w:iCs/>")
    if code:
        props.append('<w:rFonts w:ascii="Courier New" w:hAnsi="Courier New"/>')
    if size is not None:
        props.append(f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>')
    rpr = f"<w:rPr>{''.join(props)}</w:rPr>" if props else ""
    preserve = ' xml:space="preserve"' if text[:1].isspace() or text[-1:].isspace() else ""
    return f"<w:r>{rpr}<w:t{preserve}>{xml_escape(text)}</w:t></w:r>"


def inline_runs(text: str, *, size: int | None = None, force_bold: bool = False) -> str:
    """Render conservative Markdown emphasis without nested markup."""
    token = re.compile(r"(\*\*.+?\*\*|(?<!\*)\*[^*]+?\*(?!\*)|`[^`]+?`)")
    out: list[str] = []
    pos = 0
    for match in token.finditer(text):
        if match.start() > pos:
            out.append(run_xml(text[pos : match.start()], bold=force_bold, size=size))
        raw = match.group(0)
        if raw.startswith("**"):
            out.append(run_xml(raw[2:-2], bold=True, size=size))
        elif raw.startswith("*"):
            out.append(run_xml(raw[1:-1], italic=True, size=size))
        else:
            out.append(run_xml(raw[1:-1], code=True, size=size))
        pos = match.end()
    if pos < len(text):
        out.append(run_xml(text[pos:], bold=force_bold, size=size))
    return "".join(out)


def paragraph_xml(
    text: str,
    style: str = "Normal",
    *,
    keep_next: bool = False,
    page_break_before: bool = False,
    align: str | None = None,
    size: int | None = None,
) -> str:
    props = [f'<w:pStyle w:val="{style}"/>']
    if keep_next:
        props.append("<w:keepNext/>")
    if page_break_before:
        props.append("<w:pageBreakBefore/>")
    if align:
        props.append(f'<w:jc w:val="{align}"/>')
    return f"<w:p><w:pPr>{''.join(props)}</w:pPr>{inline_runs(text, size=size)}</w:p>"


def split_table_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def is_separator(line: str) -> bool:
    cells = split_table_row(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in cells)


def column_alignments(separator: str) -> list[str]:
    aligns: list[str] = []
    for cell in split_table_row(separator):
        stripped = cell.replace(" ", "")
        if stripped.startswith(":") and stripped.endswith(":"):
            aligns.append("center")
        elif stripped.endswith(":"):
            aligns.append("right")
        else:
            aligns.append("left")
    return aligns


def column_widths(rows: list[list[str]], total: int = 9026) -> list[int]:
    cols = max(len(row) for row in rows)
    # Stable manuscript-specific layouts improve readability over equal columns.
    presets: dict[int, list[int]] = {
        3: [2400, 3550, 3076],
        4: [1800, 2300, 1250, 3676],
        5: [1300, 1650, 2200, 1450, 2426],
        9: [550, 880, 900, 700, 390, 390, 620, 1120, 3476],
    }
    if cols in presets:
        return presets[cols]
    weights: list[int] = []
    for ci in range(cols):
        longest = max(len(re.sub(r"[*`]", "", row[ci])) if ci < len(row) else 0 for row in rows)
        weights.append(max(6, min(longest, 32)))
    scale = total / sum(weights)
    widths = [max(450, int(weight * scale)) for weight in weights]
    widths[-1] += total - sum(widths)
    return widths


def three_line_table_xml(rows: list[list[str]], aligns: list[str]) -> str:
    cols = max(len(row) for row in rows)
    rows = [row + [""] * (cols - len(row)) for row in rows]
    aligns = aligns + ["left"] * (cols - len(aligns))
    widths = column_widths(rows)
    grid = "".join(f'<w:gridCol w:w="{width}"/>' for width in widths)
    cell_font = 15 if cols >= 8 else 18  # 7.5 pt for wide tables; otherwise 9 pt

    table_rows: list[str] = []
    for ri, row in enumerate(rows):
        cells: list[str] = []
        for ci, cell in enumerate(row):
            header_rule = (
                '<w:tcBorders><w:bottom w:val="single" w:sz="8" w:space="0" '
                'w:color="000000"/></w:tcBorders>'
                if ri == 0
                else ""
            )
            tcpr = (
                f'<w:tcPr><w:tcW w:w="{widths[ci]}" w:type="dxa"/>{header_rule}'
                '<w:vAlign w:val="center"/><w:tcMar>'
                '<w:top w:w="50" w:type="dxa"/><w:left w:w="45" w:type="dxa"/>'
                '<w:bottom w:w="50" w:type="dxa"/><w:right w:w="45" w:type="dxa"/>'
                '</w:tcMar></w:tcPr>'
            )
            ppr = (
                '<w:pPr><w:pStyle w:val="TableText"/><w:spacing w:before="0" '
                f'w:after="0" w:line="190" w:lineRule="auto"/><w:jc w:val="{aligns[ci]}"/>'
                '<w:keepLines/></w:pPr>'
            )
            content = inline_runs(cell.strip(), size=cell_font, force_bold=(ri == 0))
            cells.append(f"<w:tc>{tcpr}<w:p>{ppr}{content}</w:p></w:tc>")
        trpr = "<w:trPr><w:tblHeader/><w:cantSplit/></w:trPr>" if ri == 0 else "<w:trPr><w:cantSplit/></w:trPr>"
        table_rows.append(f"<w:tr>{trpr}{''.join(cells)}</w:tr>")

    # Three-line table: heavy top/bottom rules plus one light rule beneath header.
    borders = (
        '<w:tblBorders>'
        '<w:top w:val="single" w:sz="12" w:space="0" w:color="000000"/>'
        '<w:left w:val="nil"/><w:bottom w:val="single" w:sz="12" w:space="0" w:color="000000"/>'
        '<w:right w:val="nil"/><w:insideH w:val="nil"/><w:insideV w:val="nil"/>'
        '</w:tblBorders>'
    )
    tblpr = (
        '<w:tblPr><w:tblStyle w:val="ThreeLineTable"/><w:tblW w:w="5000" w:type="pct"/>'
        '<w:tblLayout w:type="fixed"/><w:tblLook w:val="04A0" w:firstRow="1" '
        f'w:lastRow="0" w:firstColumn="0" w:lastColumn="0" w:noHBand="1" w:noVBand="1"/>{borders}</w:tblPr>'
    )
    return f"<w:tbl>{tblpr}<w:tblGrid>{grid}</w:tblGrid>{''.join(table_rows)}</w:tbl>"


def parse_markdown(md_path: Path) -> tuple[str, dict[str, int]]:
    lines = md_path.read_text(encoding="utf-8").splitlines()
    body: list[str] = []
    stats = {"paragraphs": 0, "tables": 0, "references": 0}
    in_abstract = False
    in_references = False
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        if not line:
            i += 1
            continue

        if line.startswith("|") and i + 1 < len(lines) and is_separator(lines[i + 1]):
            rows = [split_table_row(line)]
            aligns = column_alignments(lines[i + 1])
            i += 2
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                rows.append(split_table_row(lines[i]))
                i += 1
            body.append(three_line_table_xml(rows, aligns))
            body.append('<w:p><w:pPr><w:spacing w:after="80"/></w:pPr></w:p>')
            stats["tables"] += 1
            continue

        heading = re.match(r"^(#{1,4})\s+(.+)$", line)
        if heading:
            level = len(heading.group(1))
            text = heading.group(2).strip()
            if level == 1:
                style = "Title"
            elif level == 2:
                style = "Heading1"
            else:
                style = "Heading2"
            in_abstract = text == "Abstract"
            in_references = text == "References"
            body.append(
                paragraph_xml(
                    text,
                    style,
                    keep_next=True,
                    page_break_before=in_references,
                )
            )
            stats["paragraphs"] += 1
            i += 1
            continue

        if in_references and re.match(r"^\d+\.\s+", line):
            body.append(paragraph_xml(line, "Reference"))
            stats["references"] += 1
            stats["paragraphs"] += 1
            i += 1
            continue

        if line.startswith("**Table ") or line.startswith("**Supplementary Table "):
            body.append(paragraph_xml(line, "TableCaption", keep_next=True))
        elif line.startswith("**Note.**"):
            body.append(paragraph_xml(line, "TableNote"))
        elif line.startswith("**Keywords:**"):
            body.append(paragraph_xml(line, "Keywords"))
        elif in_abstract:
            body.append(paragraph_xml(line, "AbstractText"))
        else:
            body.append(paragraph_xml(line, "Normal"))
        stats["paragraphs"] += 1
        i += 1
    return "".join(body), stats


def styles_xml() -> str:
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="{W}">
  <w:docDefaults>
    <w:rPrDefault><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:eastAsia="Times New Roman" w:cs="Times New Roman"/><w:sz w:val="24"/><w:szCs w:val="24"/><w:lang w:val="en-GB"/></w:rPr></w:rPrDefault>
    <w:pPrDefault><w:pPr><w:spacing w:before="0" w:after="0" w:line="480" w:lineRule="auto"/><w:jc w:val="both"/><w:widowControl/></w:pPr></w:pPrDefault>
  </w:docDefaults>
  <w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:qFormat/><w:pPr><w:spacing w:before="0" w:after="0" w:line="480" w:lineRule="auto"/><w:jc w:val="both"/><w:widowControl/></w:pPr></w:style>
  <w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:basedOn w:val="Normal"/><w:next w:val="Heading1"/><w:qFormat/><w:pPr><w:keepNext/><w:keepLines/><w:spacing w:before="0" w:after="240" w:line="360" w:lineRule="auto"/><w:jc w:val="center"/><w:outlineLvl w:val="0"/></w:pPr><w:rPr><w:b/><w:bCs/><w:sz w:val="32"/><w:szCs w:val="32"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="Heading 1"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/><w:pPr><w:keepNext/><w:keepLines/><w:spacing w:before="240" w:after="60" w:line="300" w:lineRule="auto"/><w:outlineLvl w:val="1"/></w:pPr><w:rPr><w:b/><w:bCs/><w:sz w:val="28"/><w:szCs w:val="28"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="Heading 2"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/><w:pPr><w:keepNext/><w:keepLines/><w:spacing w:before="180" w:after="30" w:line="276" w:lineRule="auto"/><w:outlineLvl w:val="2"/></w:pPr><w:rPr><w:b/><w:bCs/><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="AbstractText"><w:name w:val="Abstract Text"/><w:basedOn w:val="Normal"/><w:pPr><w:spacing w:before="0" w:after="80" w:line="300" w:lineRule="auto"/><w:jc w:val="both"/></w:pPr><w:rPr><w:sz w:val="22"/><w:szCs w:val="22"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Keywords"><w:name w:val="Keywords"/><w:basedOn w:val="AbstractText"/><w:pPr><w:spacing w:after="160" w:line="300" w:lineRule="auto"/></w:pPr></w:style>
  <w:style w:type="paragraph" w:styleId="TableCaption"><w:name w:val="Table Caption"/><w:basedOn w:val="Normal"/><w:pPr><w:keepNext/><w:keepLines/><w:spacing w:before="120" w:after="50" w:line="240" w:lineRule="auto"/><w:jc w:val="left"/></w:pPr><w:rPr><w:sz w:val="20"/><w:szCs w:val="20"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="TableNote"><w:name w:val="Table Note"/><w:basedOn w:val="Normal"/><w:pPr><w:spacing w:before="40" w:after="100" w:line="220" w:lineRule="auto"/><w:jc w:val="left"/></w:pPr><w:rPr><w:sz w:val="18"/><w:szCs w:val="18"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Reference"><w:name w:val="Reference"/><w:basedOn w:val="Normal"/><w:pPr><w:ind w:left="360" w:hanging="360"/><w:spacing w:before="0" w:after="40" w:line="240" w:lineRule="auto"/><w:jc w:val="left"/><w:widowControl/></w:pPr><w:rPr><w:sz w:val="20"/><w:szCs w:val="20"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="TableText"><w:name w:val="Table Text"/><w:basedOn w:val="Normal"/><w:pPr><w:spacing w:before="0" w:after="0" w:line="190" w:lineRule="auto"/><w:jc w:val="left"/></w:pPr><w:rPr><w:sz w:val="18"/><w:szCs w:val="18"/></w:rPr></w:style>
  <w:style w:type="table" w:styleId="ThreeLineTable"><w:name w:val="Three-line Table"/><w:uiPriority w:val="1"/><w:qFormat/><w:tblPr><w:tblCellMar><w:top w:w="50" w:type="dxa"/><w:left w:w="45" w:type="dxa"/><w:bottom w:w="50" w:type="dxa"/><w:right w:w="45" w:type="dxa"/></w:tblCellMar></w:tblPr></w:style>
</w:styles>'''


def build(md_path: Path, out_path: Path, *, title: str) -> dict[str, int]:
    body, stats = parse_markdown(md_path)
    section = (
        '<w:sectPr><w:footerReference w:type="default" r:id="rId4"/>'
        '<w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1440" w:right="1440" '
        'w:bottom="1440" w:left="1440" w:header="720" w:footer="720" w:gutter="0"/>'
        '<w:lnNumType w:countBy="1" w:distance="360" w:restart="continuous"/>'
        '<w:cols w:space="720"/><w:docGrid w:linePitch="312"/></w:sectPr>'
    )
    document = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        f'<w:document xmlns:w="{W}" xmlns:r="{R}"><w:body>{body}{section}</w:body></w:document>'
    )
    doc_rels = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/settings" Target="settings.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/fontTable" Target="fontTable.xml"/>
  <Relationship Id="rId4" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/>
</Relationships>'''
    content_types = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
  <Override PartName="/word/settings.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml"/>
  <Override PartName="/word/fontTable.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.fontTable+xml"/>
  <Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>
  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>'''
    root_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>'''
    settings = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:settings xmlns:w="{W}"><w:zoom w:percent="100"/><w:defaultTabStop w:val="720"/>
<w:updateFields w:val="true"/><w:doNotTrackFormatting/><w:characterSpacingControl w:val="doNotCompress"/>
<w:compat><w:compatSetting w:name="compatibilityMode" w:uri="http://schemas.microsoft.com/office/word" w:val="15"/></w:compat>
</w:settings>'''
    fonts = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:fonts xmlns:w="{W}"><w:font w:name="Times New Roman"/><w:font w:name="Courier New"/></w:fonts>'''
    footer = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:ftr xmlns:w="{W}"><w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:fldChar w:fldCharType="begin"/></w:r><w:r><w:instrText xml:space="preserve"> PAGE </w:instrText></w:r><w:r><w:fldChar w:fldCharType="separate"/></w:r><w:r><w:t>1</w:t></w:r><w:r><w:fldChar w:fldCharType="end"/></w:r></w:p></w:ftr>'''
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    core = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<dc:title>{xml_escape(title)}</dc:title><dc:subject>Blinded scientific manuscript</dc:subject><dc:creator></dc:creator><cp:lastModifiedBy></cp:lastModifiedBy>
<dcterms:created xsi:type="dcterms:W3CDTF">{now}</dcterms:created><dcterms:modified xsi:type="dcterms:W3CDTF">{now}</dcterms:modified>
</cp:coreProperties>'''
    app = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"><Application>Office Open XML</Application><DocSecurity>0</DocSecurity><ScaleCrop>false</ScaleCrop><Company></Company><LinksUpToDate>false</LinksUpToDate><SharedDoc>false</SharedDoc><HyperlinksChanged>false</HyperlinksChanged><AppVersion>16.0000</AppVersion></Properties>'''

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("[Content_Types].xml", content_types)
        archive.writestr("_rels/.rels", root_rels)
        archive.writestr("docProps/core.xml", core)
        archive.writestr("docProps/app.xml", app)
        archive.writestr("word/document.xml", document)
        archive.writestr("word/_rels/document.xml.rels", doc_rels)
        archive.writestr("word/styles.xml", styles_xml())
        archive.writestr("word/settings.xml", settings)
        archive.writestr("word/fontTable.xml", fonts)
        archive.writestr("word/footer1.xml", footer)
    return stats


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--title", required=True)
    args = parser.parse_args()
    stats = build(args.input.resolve(), args.output.resolve(), title=args.title)
    print(f"{args.output.resolve()} | {stats}")


if __name__ == "__main__":
    main()
