# Stage 8 — Language polishing / 学术润色

Date: 2026-08-12 (v0.5).

## Deterministic checks / 确定性检查

- Bilingual consistency audit: PASS (`../quality_reports/manuscript_consistency.json`) — all locked numbers present in both languages, prohibited claims absent, references 1–43 sequential in both.
- Language structure audit: PASS — 8 parallel H2 sections, all 43 references cited before the reference list in both languages, no TODO/TBD placeholders.
- Citation inventory: PASS — 43-DOI set identical across EN/ZH/verified list; BibTeX is a documented superset.
- Word count (informational): see `../quality_reports/manuscript_word_count.json`.

## Style policy / 润色策略

- Passive voice is tolerated in Methods where the actor is the pipeline; active voice preferred elsewhere.
- Chinese text follows `skills/48-copaper-ai-chinese-de-aigc` conventions (avoid four-character boilerplate and sentence-initial “此外/因此” stacking); claims are downgraded to their evidence level.
- `AUTHOR_INPUT_NEEDED` markers are intentional pre-submission flags, not lint failures; they are inventoried in the structure audit.
