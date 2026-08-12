# Supplementary Tables / 补充表

**Linked manuscript:** manuscript_bilingual.md（A Proteome-Supported Screen of Periodontitis-Associated Oral sORF Peptides…）  
**Bilingual format:** column headers are bilingual; counts are identical to the main text. / 列名双语；全部数值与正文一致。

## Table S1. Long-peptide UniDL4BioPep high-confidence counts (P ≥ 0.8) / 表 S1. 长肽 UniDL4BioPep 高置信计数（P ≥ 0.8）

Backgrounds / 背景: healthy / 健康 953; periodontitis / 牙周炎 1,032.

| Model / 模型 | Healthy n (%) / 健康 n (%) | Periodontitis n (%) / 牙周炎 n (%) |
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

Interpretation boundary / 解读边界: Bitter is the most frequent call and is not treated as an AD phenotype; exploratory Fisher tests ignore donor clustering. / 苦味为最高频判读，不作为 AD 表型；探索性 Fisher 检验忽略供体聚类。

## Table S2. Short-peptide UniDL4BioPep high-confidence counts (P ≥ 0.8) / 表 S2. 短肽 UniDL4BioPep 高置信计数（P ≥ 0.8）

Backgrounds / 背景: healthy / 健康 30,557; periodontitis / 牙周炎 32,754.

| Model / 模型 | Healthy n (%) / 健康 n (%) | Periodontitis n (%) / 牙周炎 n (%) |
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

Interpretation boundary / 解读边界: `Antimicrobial_activity` saturation (99.93% / 99.90%) is a property of that classifier head, not a census of oral antibiotics. / 广谱抗微生物头饱和是该分类头性质，不是口腔抗生素普查。

## Table S3. Three-model funnel with denominators / 表 S3. 三模型漏斗（含分母）

| Stage / 阶段 | Rule / 规则 | n | Denominator basis / 分母依据 |
| --- | --- | ---: | --- |
| BBB short / BBB 短肽 | BBB ≥ 0.8, 5–30 aa | 3,446 | periodontitis-supported short set / 牙周炎支持短肽集 |
| BBB long / BBB 长肽 | BBB ≥ 0.8, 31–50 aa | 72 | periodontitis-supported long set / 牙周炎支持长肽集 |
| BBB total / BBB 合计 | BBB ≥ 0.8 | 3,518 | 3,446 + 72 |
| NTxPred2 skipped / NTxPred2 跳过 | < 7 aa | 219 | 3,518 − 3,299 |
| NTxPred2 scored / NTxPred2 打分 | ≥ 7 aa | 3,299 | length gate / 长度门 |
| Neurotoxic / 神经毒性 | NTxPred2 = Neurotoxic | 923 | all ≤ 30 aa |
| Cu/Fe/Zn binders / Cu/Fe/Zn 结合 | mebipred 0.5 | 111 | of 3,299 scored / 于 3,299 条打分序列 |
| CHEL ≥ 0.25 | AnOxPePred | 15 | of 111 / 于 111 条 |
| Main set / 主集 | CHEL ≥ 0.25 and FRS < 0.50 | **12** | of 15 / 于 15 条 |
| High-confidence subset / 高置信子集 | CHEL ≥ 0.25 and FRS < 0.45 | **8** | of 15 / 于 15 条 |

## Table S4. Twelve main candidates — sequences, composition and PAS-focused docking / 表 S4. 十二条主候选——序列、组成与 PAS 聚焦对接

Receptor / 受体: human AChE, PDB 4EY6 [8]; box / 盒子: 40 × 40 × 40 Å³ centred on the PAS / 以 PAS 为中心; engine / 引擎: AutoDock Vina 1.2.5 [35,36].

| Rank / 排名 | Peptide ID / 肽 ID | Sequence / 序列 | Length (aa) / 长度 | His | Cys | Arg+Lys | Aromatic (F/Y/W) / 芳香族 | Vina score mean ± SD (kcal/mol) / Vina 打分 |
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

Composition columns counted directly from the sequences / 组成列由序列直接计数. Qualitative pose contacts / 构象定性接触: PAS core / PAS 核心 — Tyr72, Asp74, Tyr124, Trp286, Tyr341; gorge aromatics / 峡部芳香族 — Trp86, Phe295, Tyr337, Phe338; catalytic reach / 催化区可及 — Ser203, His447. Vina scores rank poses; they are not binding constants / Vina 打分为构象排序，不是结合常数.

## Table S5. Evidence boundaries for predicted labels / 表 S5. 预测标签的证据边界

| Predictor output / 预测器输出 | It is / 它是 | It is not / 它不是 |
| --- | --- | --- |
| UniDL4BioPep BBB ≥ 0.8 | a classifier call on sequence / 序列层面的分类器判读 | measured BBB transport or brain exposure / 实测 BBB 转运或脑暴露 |
| NTxPred2 = Neurotoxic | a predictor label / 预测器标签 | experimental neurotoxicity / 实验神经毒性 |
| mebipred Cu/Fe/Zn positive | a metal-binding potential call / 金属结合潜力判读 | affinity, stoichiometry or coordination evidence / 亲和力、化学计量或配位证据 |
| CHEL-high / FRS-low | a priority rule for synthesis / 合成优先级规则 | demonstrated pro-oxidant activity / 已证明的促氧化活性 |
| Vina score ≤ −8 kcal/mol | a within-set pose ranking / 集合内构象排序 | a dissociation constant or binding free energy / 解离常数或结合自由能 |

*Shared reference list with the main manuscript. / 与主稿共用同一参考文献表。*
