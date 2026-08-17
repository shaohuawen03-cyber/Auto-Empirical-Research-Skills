# Supplementary Tables

**Linked manuscript:** Proteome-supported screening of periodontitis-associated peptides encoded by small open reading frames identifies candidates with predicted metal binding, blood–brain barrier permeability and acetylcholinesterase docking potential

## Supplementary Table S1. Long-peptide UniDL4BioPep high-confidence counts (*P* ≥ 0.8)

Background: healthy, 953; periodontitis, 1,032.

| Model | Healthy *n* (%) | Periodontitis *n* (%) |
| --- | ---: | ---: |
| ACP_Anticancer_alt | 91 (9.55) | 121 (11.72) |
| BBB_Peptides | 40 (4.20) | 72 (6.98) |
| Quorum_sensing | 173 (18.15) | 190 (18.41) |
| Antimicrobial | 206 (21.62) | 238 (23.06) |
| Antibacterial | 111 (11.65) | 153 (14.83) |
| Anti-MRSA | 47 (4.93) | 62 (6.01) |
| CPP | 15 (1.57) | 29 (2.81) |
| Antifungal | 73 (7.66) | 96 (9.30) |
| Toxicity | 13 (1.36) | 18 (1.74) |
| Umami | 17 (1.78) | 15 (1.45) |
| Antimalarial_alt | 12 (1.26) | 14 (1.36) |
| TTCA | 1 (0.10) | 1 (0.10) |
| Antioxidant_FRS | 43 (4.51) | 41 (3.97) |
| DPPIV | 0 (0.00) | 0 (0.00) |
| Antimalarial_main | 0 (0.00) | 0 (0.00) |
| Anti-parasitic | 288 (30.22) | 280 (27.13) |
| NeuroPred | 82 (8.60) | 77 (7.46) |
| ACP_Anticancer_main | 37 (3.88) | 31 (3.00) |
| ACE_inhibitory | 20 (2.10) | 14 (1.36) |
| Allergenicity | 16 (1.68) | 11 (1.07) |
| Antiviral | 55 (5.77) | 52 (5.04) |
| Bitter | 635 (66.63) | 641 (62.11) |

**Note.** Bitter is the most frequent call and is not treated as an AD phenotype; exploratory Fisher tests ignore donor clustering.

## Supplementary Table S2. Short-peptide UniDL4BioPep high-confidence counts (*P* ≥ 0.8)

Background: healthy, 30,557; periodontitis, 32,754.

| Model | Healthy *n* (%) | Periodontitis *n* (%) |
| --- | ---: | ---: |
| ACE_inhibitory_activity | 2,781 (9.10) | 2,856 (8.72) |
| TTCA | 9,123 (29.86) | 9,161 (27.97) |
| BBB_Peptides | 3,359 (10.99) | 3,446 (10.52) |
| APP_Anti-parasitic | 21,185 (69.33) | 22,010 (67.20) |
| NeuroPred | 3,876 (12.68) | 4,019 (12.27) |
| Antibacterial_AB | 9,269 (30.33) | 9,273 (28.31) |
| Antifungal_AF | 8,732 (28.58) | 8,475 (25.87) |
| AV_Antiviral | 7,501 (24.55) | 7,221 (22.05) |
| Toxicity_2021 | 2,770 (9.07) | 2,751 (8.40) |
| Antioxidant_FRS | 4,171 (13.65) | 4,093 (12.50) |
| Allergenicity | 8,599 (28.14) | 9,422 (28.77) |
| DPPIV_inhibitory_activity | 207 (0.68) | 266 (0.81) |
| CPP | 4,435 (14.51) | 4,133 (12.62) |
| Bitter | 5,037 (16.48) | 4,986 (15.22) |
| Umami | 6,095 (19.95) | 6,094 (18.61) |
| Antimicrobial_activity | 30,537 (99.93) | 32,721 (99.90) |
| Antimalarial_alt | 1,724 (5.64) | 1,695 (5.17) |
| Antimalarial_main | 6,496 (21.26) | 6,586 (20.11) |
| Quorum_sensing | 11,834 (38.73) | 12,674 (38.69) |
| ACP_Anticancer_alt | 7,878 (25.78) | 8,380 (25.58) |
| ACP_Anticancer_main | 11,370 (37.21) | 12,023 (36.71) |
| Anti-MRSA | 4,315 (14.12) | 4,728 (14.43) |

**Note.** `Antimicrobial_activity` saturation (99.93% / 99.90%) is a property of that classifier head, not a census of oral antibiotics.

## Supplementary Table S3. Three-model funnel with denominators

| Stage | Rule | *n* | Denominator basis |
| --- | --- | ---: | --- |
| BBB short | BBB ≥ 0.8, 5–30 aa | 3,446 | periodontitis-supported short set |
| BBB long | BBB ≥ 0.8, 31–50 aa | 72 | periodontitis-supported long set |
| BBB total | BBB ≥ 0.8 | 3,518 | 3,446 + 72 |
| NTxPred2 skipped | < 7 aa | 219 | 3,518 − 3,299 |
| NTxPred2 scored | ≥ 7 aa | 3,299 | length gate |
| Neurotoxic | NTxPred2 = Neurotoxic | 923 | all ≤ 30 aa |
| Cu/Fe/Zn binders | mebipred 0.5 | 111 | of 3,299 scored |
| CHEL ≥ 0.25 | AnOxPePred | 15 | of 111 |
| Main set | CHEL ≥ 0.25 and FRS < 0.50 | **12** | of 15 |
| High-confidence subset | CHEL ≥ 0.25 and FRS < 0.45 | **8** | of 15 |

## Supplementary Table S4. Twelve main candidates — sequences, composition and PAS-focused docking

Receptor: human AChE, PDB 4EY6 [8]; search box: 40 × 40 × 40 Å³ centred on the PAS; engine: AutoDock Vina 1.2.5 [34,35].

| Rank | Peptide ID | Sequence | Length (aa) | His | Cys | Arg+Lys | Aromatic (F/Y/W) | Vina score mean ± SD (kcal/mol) |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | fllhttr | FLLHTTR | 7 | 1 | 0 | 1 | 1 (F) | −9.60 ± 0.08 |
| 2 | ylsllqr | YLSLLQR | 7 | 0 | 0 | 1 | 1 (Y) | −9.49 ± 0.05 |
| 3 | alllhrc | ALLLHRC | 7 | 1 | 1 | 1 | 0 | −9.29 ± 0.11 |
| 4 | fclhlqlr | FCLHLQLR | 8 | 1 | 1 | 1 | 1 (F) | −9.27 ± 0.09 |
| 5 | yhhllcrr | YHHLLCRR | 8 | 2 | 1 | 2 | 1 (Y) | −9.03 ± 0.07 |
| 6 | llhlpkrtt | LLHLPKRTT | 9 | 1 | 0 | 2 | 0 | −9.01 ± 0.06 |
| 7 | llhplrl | LLHPLRL | 7 | 1 | 0 | 1 | 0 | −8.94 ± 0.10 |
| 8 | wllvhlkk | WLLVHLKK | 8 | 1 | 0 | 2 | 1 (W) | −8.94 ± 0.04 |
| 9 | llhplrc | LLHPLRC | 7 | 1 | 1 | 1 | 0 | −8.91 ± 0.08 |
| 10 | hlltlkkhv | HLLTLKKHV | 9 | 2 | 0 | 2 | 0 | −8.88 ± 0.05 |
| 11 | hlpllhrcc | HLPLLHRCC | 9 | 1 | 2 | 1 | 0 | −8.35 ± 0.12 |
| 12 | hvlllrqca | HVLLLRQCA | 9 | 1 | 1 | 1 | 0 | −8.25 ± 0.09 |

**Note.** Composition columns were counted directly from the sequences. Pose contacts were inspected qualitatively at the PAS core (Tyr72, Asp74, Tyr124, Trp286 and Tyr341), gorge aromatics (Trp86, Phe295, Tyr337 and Phe338), and catalytic region (Ser203 and His447). Vina scores are pose-ranking outputs, not binding constants.

## Supplementary Table S5. Evidence boundaries for predicted labels

| Predictor output | It is | It is not |
| --- | --- | --- |
| UniDL4BioPep BBB ≥ 0.8 | a classifier call on sequence | measured BBB transport or brain exposure |
| NTxPred2 = Neurotoxic | a predictor label | experimental neurotoxicity |
| mebipred Cu/Fe/Zn positive | a metal-binding potential call | affinity, stoichiometry or coordination evidence |
| CHEL-high / FRS-low | a priority rule for synthesis | demonstrated pro-oxidant activity |
| Vina score ≤ −8 kcal/mol | a within-set pose ranking | a dissociation constant or binding free energy |

*References are listed in the main manuscript.*
