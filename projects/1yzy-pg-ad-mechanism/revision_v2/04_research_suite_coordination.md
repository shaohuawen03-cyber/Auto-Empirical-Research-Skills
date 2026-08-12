# Stage 4 — Research-suite coordination / 全流程研究方案

Date: 2026-08-12 (v0.5).

## Stage-one workflow (author pipeline, transcribed) / 阶段一流程（作者管线转录）

1. PRJNA678453 + PRJEB65451 → 296 MAGs → group-specific sORF libraries (4–50 aa).
2. Exact-identity collapse against PXD003151 / PXD004319 / PXD026727 (short) and HOMD (long).
3. UniDL4BioPep (ESM-2 `esm2_t6_8M_UR50D`) at P ≥ 0.8, branches kept separate.
4. BBB ≥ 0.8 → NTxPred2 (≥ 7 aa) → mebipred (0.5) → AnOxPePred (CHEL/FRS).
5. CHEL ≥ 0.25 ∧ FRS < 0.50 → 12 main; FRS < 0.45 → 8 strict.

## Stage-two workflow (author docking note, transcribed) / 阶段二流程（作者对接说明转录）

1. Receptor: 4EY6 (galantamine/waters removed; preparation toolchain `AUTHOR_INPUT_NEEDED`).
2. Ligands: twelve 7–9-mers, flexible, energy-minimised (builder `AUTHOR_INPUT_NEEDED`).
3. Box: 40 × 40 × 40 Å³ centred on PAS (Tyr72/Asp74/Tyr124/Trp286/Tyr341); Vina 1.2.5 (exhaustiveness/seeds `AUTHOR_INPUT_NEEDED`).
4. Pose analysis: containment, PAS contacts, gorge aromatics, catalytic reach.
5. MD attempt: GROMACS 2025 / AMBER99SB-ILDN / TIP3P / Berendsen NPT → Z-axis pressure instability → excluded with remediation plan.

## Reproducibility gaps (documented, not hidden) / 可复现性缺口

Software versions and random seeds for UniDL4BioPep / NTxPred2 / mebipred / AnOxPePred; docking exhaustiveness,
run count and seeds; receptor/ligand preparation toolchain; the 8-of-12 strict-subset labels; donor-by-peptide
matrix for donor-level inference. All marked `AUTHOR_INPUT_NEEDED` in the manuscript.
