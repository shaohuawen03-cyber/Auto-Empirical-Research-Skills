# Stage 7 — Nature-style writing rebuild / Nature 风格重写

Date: 2026-08-12 (v0.5). Follows AERS K-Dense scientific-writing conventions (IMRaD, full-paragraph prose,
Vancouver) and the Light-skills bilingual section-parallel layout.

## Deliverables / 交付

- `../manuscript/manuscript_en.md` — English master (8 top-level sections; structured abstract; 43 references).
- `../manuscript/manuscript_zh.md` — full Chinese parallel, same section order and identical numbers.
- `../manuscript/manuscript_bilingual.md` — machine-merged section-parallel draft (`../scripts/build_bilingual_markdown.py`).
- `../manuscript/manuscript_bilingual.docx` — stdlib OOXML build (`../scripts/build_docx_stdlib.py`); package-audited.
- `../manuscript/supplementary_tables_bilingual.{md,docx}` — Tables S1–S5 (full predictor heads, funnel, docking, evidence-boundary table).

## Writing decisions / 写作决定

- v0.3’s thin four-paragraph introduction is replaced by six subsections (~1,500 words) — the user’s core complaint.
- The author’s lab-notebook-style §4 (AlphaFold3, metals, FlexPepDock, GROMACS difficulties, wet cascade) is condensed into Discussion 4.5 roadmap; the MD failure is reported in Methods 2.11 with causes and remediation, not hidden.
- Docking results use ranking language only (“orders”, “occupies”, “contacts”); prohibited phrasing list enforced by audit.
- All numeric strings are shared verbatim between EN and ZH; the consistency audit locks them.
