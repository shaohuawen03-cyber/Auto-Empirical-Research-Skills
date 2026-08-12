# Claim–evidence ledger / 主张–证据台账（v0.5）

Every non-trivial claim in the manuscript maps to one of: [A] author source draft, [D] author docking note,
[L] independently cited literature, [R] deterministic recomputation in this project.

| # | Claim (manuscript location) | Evidence class | Source / boundary |
| --- | --- | --- | --- |
| 1 | Raw sORF libraries 11,269,961 / 11,721,988; supported 31,510 / 33,786 (Table 1) | A + R | author draft; recomputed passage rates (`revision_v2/statistics_audit.json`) |
| 2 | BBB counts 3,359/3,446/40/72 and 3,518 total (§3.2, §3.5) | A + R | author draft; arithmetic audit |
| 3 | NTxPred2 3,299 scored / 219 skipped / 923 positive (§3.6) | A | author draft; length gate ≥ 7 aa |
| 4 | mebipred 111; CHEL≥0.25 → 15; FRS<0.50 → 12; FRS<0.45 → 8 (§3.6) | A | author draft; 8-of-12 membership undeposited (`AUTHOR_INPUT_NEEDED`) |
| 5 | Twelve candidate sequences (Table 5) | D | author docking note Table 3-5 |
| 6 | Composition counts His 11/12, Cys 6/12, all basic, Leu-rich (§3.6, Table 5) | R | counted directly from the sequences |
| 7 | Vina scores −8.25…−9.60 kcal/mol, mean±SD; full box containment (§3.7) | D | author docking note; ranking language only |
| 8 | Gorge-spanning mode; PAS residues Tyr72/Asp74/Tyr124/Trp286/Tyr341; gorge aromatics; Ser203/His447 reach (§3.7) | D | author pose description; qualitative |
| 9 | 4EY6 = human AChE–galantamine, 2.40 Å, Cheung 2012; chain breaks near 259–262/492–495 (§2.10) | L + D | PDB record (verified) + author note |
| 10 | MD attempt failed at NPT (Z-axis pressure); causes & remediation (§2.11) | D | author note; no trajectory reported |
| 11 | PAS accelerates Aβ fibril assembly (§1.1) | L | refs 4–6 |
| 12 | Aβ residence patch 344–361 adjacent to PAS (§1.1) | L | refs 9–10 |
| 13 | tau26–44 neurotoxicity & Cu(II) binding (§1.4) | L | refs 27–28 (citations corrected 2026-08-12) |
| 14 | curli cross-seeding of α-synuclein (§1.4) | L | ref 29 |
| 15 | Exploratory Fisher/χ² values (§3.1–3.4) | A | author draft; labelled exploratory, donor clustering ignored |
| 16 | “Docking orders candidates; it does not certify them” (§4.2) | R | methodological boundary of Vina [35] |

## Wording boundaries enforced by audit / 审计强制的措辞边界

Prohibited (EN): “identified periodontitis-specific”, “p. gingivalis-derived candidates”, “proved that”,
“demonstrated that the candidates”, “experimentally confirmed”.
Prohibited (ZH): “牙周炎特异性微肽”, “牙龈卟啉单胞菌来源候选”, “证明这些候选”, “证实这些候选”, “实验证实”.
