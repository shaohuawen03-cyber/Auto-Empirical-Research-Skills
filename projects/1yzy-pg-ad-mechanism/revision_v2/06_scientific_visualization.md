# Stage 6 — Scientific visualization / 科学绘图

Date: 2026-08-12 (v0.5).

## Figures in v0.5 / v0.5 图形清单

| Figure | File | Claim binding |
| --- | --- | --- |
| Fig. 1 screening design | `figures/fig1_design.{pdf,png}` | workflow overview only; no quantitative claim |
| Fig. 2 UniDL4BioPep heads | `figures/fig2_long_functions.*`, `fig2b_short_counts.*` | Tables 2–3 / S1–S2 |
| Fig. 3 funnel | `figures/fig3_funnel.{pdf,png}` | Table 4 / S3 |
| Fig. 4 BBB length mix | `figures/fig4_bbb_length.{pdf,png}` | Section 3.5 |
| Fig. 5 docking scores (new) | `figures/fig5_docking_scores.{pdf,png}` | Table 5 / S4; script `../scripts/fig5_docking_scores.py` |

## Rules / 规则

- Colour-blind-safe pair continued from v0.3 (blue `#0072B2`, vermillion `#D55E00`); top-ranked peptide in blue, remainder vermillion.
- Vector PDF is the submission master; PNG is a preview.
- No figure is generated from data that is not in the manuscript tables; Fig. 5 plots exactly the twelve mean±SD values of Table 5.
- Per-journal figure specifications (dpi, fonts, colour mode) remain an author-side pre-upload task.
