# v0.3 skill run (2026-08-12)

Detected journals/skills (online GitHub, then local AERS mirrors):

| Step | User name | Skill used | Source |
| --- | --- | --- | --- |
| 1 选题 | scientific Brainstorming | K-Dense `scientific-brainstorming` / hypothesis-generation | https://github.com/K-Dense-AI/claude-scientific-skills |
| 2 文献检索 | nature academic search | `nature-academic-search` | https://github.com/Yuan1z0825/nature-skills |
| 3 写综述 | literature review | AERS `36-taoyunudt` + K-Dense literature-review | vendored |
| 4 全流程 | academic research suite | Imbad0202 academic-paper / academic-pipeline | https://github.com/Imbad0202/academic-research-skills |
| 5 统计审查 | nature statistics | `nature-statistics` | Yuan1z0825/nature-skills |
| 6 绘图 | scientific visualization / nature-figure | `nature-figure` (Python backend) | Yuan1z0825/nature-skills |
| 7 写作 | nature writing | `nature-writing` research + IMRaD | Yuan1z0825/nature-skills |
| 8 润色 | nature polishing | `nature-polishing` (≤30-word sentences, claim/evidence/boundary) | Yuan1z0825/nature-skills |
| 9 投稿 | nature-writing submission-package | cover letter, highlights, DAS | Yuan1z0825/nature-skills |

## 1 Brainstorming (locked claim)

- **Claim:** A periodontitis-specific, proteome-supported sORF library can be reduced to a 12-peptide (8-peptide) computational shortlist by stacking BBB, metal-binding and chelator-high / scavenger-low filters.
- **Not the claim:** These 12 peptides are *P. gingivalis* gingipains; they generate ROS; they bind AChE. The MAG collection is a **community** oral metagenome (PRJNA678453), not a *P. gingivalis*-only peptidome.
- **Boundary:** No docking, MD or wet assay in this stage (author draft §2.6 / §4).
- **Independent n:** 24 healthy vs 26 periodontitis donors. Peptide 2×2 tests are exploratory and ignore donor clustering.

## 5 Statistics review (P0)

- P0: Do not treat 11 million sORFs or 33,786 peptides as independent experimental units.
- P1: Short-branch BBB/NeuroPred **percentages** do not differ; only long-branch BBB rate does (exploratory Fisher *P* = 0.0084, OR 1.71 for periodontitis).
- P1: Proteome passage *P* = 1×10⁻⁴ is an artefact of huge denominators (0.280% vs 0.288%).
- AUTHOR_INPUT_NEEDED: donor-level peptide presence/absence matrix; UniDL4BioPep software version; random seeds; 12 sequences.

## Axes (nature-writing)

`task=manuscript+submission-package; paper_type=research (methods-heavy); language=zh-to-en; journal=generic` (realistic venues: *Brief. Bioinform.*, *Comput. Struct. Biotechnol. J.*, *J. Alzheimers Dis.*, *Sci. Rep.*).
