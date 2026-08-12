# v0.4 skill run (2026-08-12)

User complaint against v0.3: “内容太少太简单了，引言部分太少了吧” — the manuscript was too thin for an SCI submission, and the Introduction was too short. v0.4 expands the Introduction to full SCI length, integrates the author’s new PAS docking results (their Table 3-5) and forward protocol (their §4.1–4.5), and integrates the author’s exogenous-toxic-peptide literature frame.

## Skills used this round (found in repo, per `SKILL.md` routing)

| Step | Task | Skill | Location |
| --- | --- | --- | --- |
| 1 | 综述/文献框架写法（五步法：检索–筛选–争议/空白–主题组织–写作） | literature-review | `skills/36-taoyunudt-literature-review-skill/SKILL.md` |
| 2 | 综述类 skill（多库检索、主题综合、引用核验、Vancouver） | literature-review | `skills/04-K-Dense-AI-claude-scientific-writer/literature-review/SKILL.md` |
| 3 | SCI 写作（IMRAD、整段散文、图表、报告规范） | scientific-writing | `skills/04-K-Dense-AI-claude-scientific-writer/scientific-writing/SKILL.md` + `skills/03-K-Dense-AI-claude-scientific-skills/scientific-writing` |
| 4 | 引用核验（PubMed/PDB 逐条比对，纠正 DOI/PMID） | citation-management | `skills/04-K-Dense-AI-claude-scientific-writer/citation-management/SKILL.md` |
| 5 | 统计口径延续 v0.3（供体为独立单位；肽水平检验仅探索） | nature-statistics（v0.3 记录） | `pipeline/00_skill_run.md` |
| 6 | 绘图（Fig. 5 Vina 打分条形图，色盲安全配色延续 v0.3） | nature-figure（Python 后端） | `scripts/fig5_docking_scores.py` |

## What changed v0.3 → v0.4

1. **Introduction ×~6.** Six subsections (1.1 AD & non-canonical AChE/PAS; 1.2 periodontitis–AD axis incl. gingipains/OMVs; 1.3 metal hypothesis & the carrier problem; 1.4 exogenous short-peptide neurotoxicity template — tau26–44/Cu(II), Perini AFM/SAXS/MD, curli cross-seeding; 1.5 sORF/micropeptide rationale; 1.6 aims & boundaries).
2. **Sequences resolved.** The twelve main-candidate sequences (author Table 3-5) are now printed in Table 5; v0.3’s `AUTHOR_INPUT_NEEDED` for sequences is closed. New `AUTHOR_INPUT_NEEDED`: which 8 of the 12 are the FRS < 0.45 subset; docking exhaustiveness/seeds; receptor/ligand prep toolchain; UniDL4BioPep versions.
3. **New Methods 2.10–2.11.** PAS-focused Vina 1.2.5 docking (4EY6, 40×40×40 Å³ box, PAS-centred; pose analysis criteria); attempted 100-ns GROMACS MD reported honestly (Z-axis pressure instability at NPT; 4EY6 chain breaks near 259–262/492–495; remediation list) — excluded from results.
4. **New Results 3.7.** Table 5 with length/His/Cys/basic/aromatic composition + Vina mean±SD (−8.25…−9.60 kcal/mol); qualitative gorge-spanning mode; PAS residues Tyr72/Asp74/Tyr124/Trp286/Tyr341; gorge aromatics Trp86/Phe295/Tyr337/Phe338; Ser203/His447 reach. Figure 5 added.
5. **Discussion rebuilt.** 4.1 triage reading; 4.2 what docking does/does not add; 4.3 candidates vs tau26–44 template; 4.4 limitations (single rigid receptor, missing loops, no glycans/waters/metals, Vina caveats, taxonomy); 4.5 roadmap condensed from author §4.1–4.5 (AF3 multi-conformer, target panel, Cu/Fe/Zn + MM/GBSA + QM/MM, FlexPepDock upgrade, MD fixes, wet-assay cascade with stopping rule).
6. **Reference list 15 → 43**, all new citations checked against PubMed/PDB.

## Citation verification log (citation-management step)

| Author table entry | Verified as | Action |
| --- | --- | --- |
| Di Natale G et al., ICA 2018, “DOI 10.1016/j.ica.2017.12.012, PMID 29289679”, title incl. “and toxicity” | Inorg Chim Acta 2018;472:82–92, **doi:10.1016/j.ica.2017.09.061**; title “Effects on Amyloid-β aggregation”; PMID 29289679 resolves to an unrelated postural-control article | Corrected; wrong PMID discarded |
| Perini/Amadoro et al., “Sci Rep 2019, DOI 10.1038/s41598-019-48745-0, PMID 31470053” | **Int J Biol Macromol** 2019;141:278–289, **doi:10.1016/j.ijbiomac.2019.08.220**, PMID 31470053 | Corrected (journal was wrong) |
| Lei P, Ayton S, Bush AI, JBC 2021, DOI 10.1074/jbc.REV120.008207, PMID 33219130 | Verified identical | Kept |
| PDB 4EY6 (no citation given) | Cheung J et al., J Med Chem 2012;55:10282–10286, doi:10.1021/jm300871x, PMID 23035744 (4EY6 = hAChE + (−)-galantamine, 2.40 Å) | Added as ref 8 |

## Statistics review (continuing P0/P1 from v0.3)

- P0 unchanged: donors (24 vs 26) are the independent units; peptide 2×2 tests exploratory.
- New P1: Vina scores are a within-set ranking only — no inferential statistics applied; docking does not certify binding.
- New P1: MD excluded due to instability (reported in Methods 2.11, not hidden).

## Deliverables

- `manuscript/sci_v04_en.md` (main, supersedes `sci_v03_en.md`)
- `manuscript/figures/fig5_docking_scores.{pdf,png}` + script `scripts/fig5_docking_scores.py`
- `manuscript/references.bib` (19 new entries, corrections noted in `note` fields)
- `submission/highlights.md`, `submission/cover_letter.md` (updated for v0.4)
