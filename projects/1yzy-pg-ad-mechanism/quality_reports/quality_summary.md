# Final quality summary / 最终质量汇总（v0.5）

Date / 日期: 2026-08-12

## Overall status / 总体状态

- **Bilingual scientific-content package / 中英文科学内容包:** PASS for accountable-author review / 可交责任作者审阅。
- **Author-approved pre-submission enquiry / 经作者批准的预投稿询问:** READY after correspondent fields are filled / 补齐通讯作者字段后可用。
- **Immediate formal SCI submission / 立即正式 SCI 投稿:** NOT READY / 尚未就绪（行政与部分技术参数缺口，见下）。
- **Rendered visual review / 渲染视觉审查:** UNAVAILABLE in this environment; no claim of page-by-page Word/PDF validation is made / 本环境无 Word/LibreOffice 渲染，不声称逐页验证。

## Current deterministic checks / 当前确定性检查

| Check | Result | Interpretation |
| --- | --- | --- |
| Manuscript consistency (EN/ZH) | PASS | `manuscript_consistency.json`: all locked screening and docking values present in both languages; prohibited mechanism/specificity claims absent; references 1–43 sequential in both. |
| Language structure | PASS | `language_structure_audit.json`: 8 parallel H2 sections per language; all 43 references cited before the reference list; no TODO/TBD placeholders; 8 intentional `AUTHOR_INPUT_NEEDED` flags per language inventoried. |
| Citation inventory | PASS | `citation_inventory_audit.json`: identical 43-DOI set across EN, ZH and `references/verified_references.md`; BibTeX is a documented superset. Two author-supplied citations were corrected on 2026-08-12 (Di Natale 2018 DOI/PMID; Perini 2019 journal). |
| Aggregate statistics | PASS | `revision_v2/statistics_audit.json`: `all_checks_pass=true`; one documented truncation convention (48.25/51.75 shares). |
| DOCX package audit | PASS | `docx_package_audit.json`: ZIP CRC, XML parse, paragraph/table counts for both packages. No renderer available — page-level review is the author’s task. |
| Word-count estimate | INFORMATIONAL | `manuscript_word_count.json`; recount after journal formatting. |
| Excluded-source containment | PASS | GSE42872 identity appears only in the boundary statements (Methods 2.7 / Limitations) and the exclusion record. |

## Scientific-integrity boundaries / 科学诚信边界

The twelve boundaries enforced in wording:

1. BBB model output is not measured BBB transport or brain exposure.
2. NTxPred2 positivity is not experimental neurotoxicity.
3. Mebipred positivity is not affinity, stoichiometry, or coordination evidence.
4. CHEL-high/FRS-lower output is not demonstrated pro-oxidant activity.
5. A periodontitis analysis branch is not a periodontitis-specific sequence set.
6. An oral candidate is not a taxonomically assigned *Porphyromonas gingivalis* candidate.
7. Candidate counts are computational accounting units, not independent biological replicates.
8. Observational periodontitis–cognition/AD associations are not evidence of causation.
9. **Vina scores rank poses; they are not binding constants, and docking was not validated by MD or experiment.**
10. **The absent MD trajectory means no dynamics statement is made; the failure is reported with causes.**
11. Aggregate computational prioritization is not candidate validation or an established disease mechanism.
12. The tau26–44/curli precedents are templates; no behavioural equivalence is claimed for the twelve candidates.

## Remaining blockers / 剩余阻断项

### Author-input (administrative) / 作者行政项

Author names/affiliations/ORCIDs, corresponding author, CRediT, ethics wording, funding, competing interests,
journal selection, Crossmark/retraction screening of the 43 references, figure-spec compliance.

### Author-input (technical) / 作者技术项

`AUTHOR_INPUT_NEEDED` markers: UniDL4BioPep / NTxPred2 / mebipred / AnOxPePred versions and seeds; docking
exhaustiveness/run count/seeds; receptor–ligand preparation toolchain; the 8-of-12 strict-subset labels.

### Scientific (cannot be fixed by editing) / 科学项（非编辑可解）

Experimental validation cascade (metal binding, Cu/Fe-dependent ROS, lipid peroxidation, AChE/BChE activity,
Aβ aggregation, neuronal viability) under the stopping rule; production MD after pressure-stability fixes;
donor-by-peptide matrix for donor-level inference.
