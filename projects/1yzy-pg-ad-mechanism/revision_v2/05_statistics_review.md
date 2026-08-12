# Stage 5 — Statistics review / 统计审查

Date: 2026-08-12 (v0.5). Machine-readable audit: `statistics_audit.json` (`all_checks_pass=true`).

## P0 (design-level) / P0 设计级

- Independent experimental units are donors (24 vs 26). Peptide counts are nested observations; every peptide-level 2×2 test in the manuscript is labelled exploratory and non-confirmatory.
- Vina scores are a within-set ranking; no inferential statistics were applied to docking.
- The MD trajectory is excluded; no MD-derived statistic is reported.

## P1 (arithmetic) / P1 算术级

All aggregate percentages in Tables 1–5 were independently recomputed from the author’s aggregate counts
(`../scripts/stage5_statistics_audit.py`). One rounding convention was documented: the confirmed-library
shares 48.25 / 51.75 follow the author’s table, which truncates to two decimals; recomputation gives
48.257 / 51.743 (tolerance 0.011, documented in the audit).

## Known uncheckable items / 无法核查项

- Row-level predictor scores, per-sequence CHEL/FRS values and the 8-of-12 strict-subset membership were not deposited.
- Donor-level mixed models are impossible without a donor-by-peptide matrix.
- The χ² on passage (P ≈ 1×10⁻⁴) is an artefact of huge denominators and is flagged as such in the text.
