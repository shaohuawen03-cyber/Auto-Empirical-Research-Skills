# A proteome-supported screen of periodontitis-specific sORF peptides yields twelve blood–brain-barrier and metal-binding candidates for Alzheimer-oriented follow-up

**Article type.** Computational research article (methods-heavy).  
**Version.** v0.3 (2026-08-12). Supersedes the bilingual archive draft v0.2.  
**Evidence spine.** Author file `材料与方法及结果_机制研究版` (methods and results only).  
**Target venues (realistic).** *Briefings in Bioinformatics*; *Computational and Structural Biotechnology Journal*; *Scientific Reports*; *Journal of Alzheimer’s Disease* (computational / microbiome section).  
**Citation style.** Vancouver.

---

## Abstract

Periodontitis is associated with Alzheimer’s disease (AD), yet most molecular accounts stop at intact *Porphyromonas gingivalis* cells or gingipain proteases. Short peptides encoded by oral small open reading frames (sORFs) are a larger, poorly counted cargo. We re-analysed a public oral metagenome collection (BioProject PRJNA678453; assembly set PRJEB65451) comprising 296 high-quality metagenome-assembled genomes from 24 healthy and 26 periodontitis donors. After length filtering (4–50 amino acids), group-specific sORF libraries contained 11,269,961 and 11,721,988 sequences. Exact identity matching to HOMD-linked oral proteomes left 31,510 and 33,786 non-redundant peptides (passage 0.2796% and 0.2882%). Peptides were scored with UniDL4BioPep at predicted probability ≥ 0.8, keeping short (5–30 aa) and long (31–50 aa) branches separate. Periodontitis contributed more blood–brain-barrier (BBB) calls in both branches (short 3,446 vs 3,359; long 72 vs 40). The 3,518 periodontitis-oriented BBB peptides—83.95% of the short branch at 8–15 aa—were passed to NTxPred2, mebipred and AnOxPePred. NTxPred2 scored 3,299 sequences (219 peptides were shorter than 7 aa) and called 923 neurotoxic, all ≤ 30 aa. Mebipred marked 111 Cu/Fe/Zn binders. AnOxPePred retained 15 peptides with chelator score ≥ 0.25; requiring a scavenger score < 0.50 left **12 main candidates**, and < 0.45 left **8**. These twelve sequences are a synthesis list, not proof of Fenton chemistry, AChE binding or plaque nucleation. Docking, molecular dynamics and wet assays are reserved for the next stage. Peptide-level 2 × 2 tests are exploratory: the independent experimental unit is the donor (24 vs 26).

**Keywords.** periodontitis; sORF; metaproteome; UniDL4BioPep; blood–brain barrier; metal binding; Alzheimer’s disease; computational triage

---

## 中文摘要

牙周炎与阿尔茨海默病相关，但分子叙述多停在完整牙龈卟啉单胞菌或牙龈蛋白酶。口腔小开放阅读框编码的短肽是更大、却很少被清点的货物。我们再分析公开口腔宏基因组（PRJNA678453 / PRJEB65451）：296 个高质量组装基因组，24 名健康对照与 26 名牙周炎患者。长度过滤（4–50 氨基酸）后，组特异 sORF 库分别为 11,269,961 与 11,721,988 条。与 HOMD 相关口腔蛋白质组精确匹配后，非冗余肽 31,510 与 33,786 条（通过率 0.2796% 与 0.2882%）。UniDL4BioPep 以预测概率 ≥ 0.8 打分，短肽与长肽分开统计。牙周炎组 BBB 阳性在两支都更多（短肽 3,446 对 3,359；长肽 72 对 40）。3,518 条 BBB 肽（短肽中 83.95% 为 8–15 aa）进入 NTxPred2、mebipred 与 AnOxPePred。NTxPred2 实际打分 3,299 条（219 条短于 7 aa），923 条判为神经毒性且全部 ≤ 30 aa。mebipred 标出 111 条 Cu/Fe/Zn 结合阳性。AnOxPePred 上 CHEL ≥ 0.25 者 15 条；FRS < 0.50 得 **主候选 12 条**，FRS < 0.45 得 **8 条**。这是合成名单，不是 Fenton、AChE 结合或成核的实验证明。对接、分子动力学与湿实验留到下一阶段。肽水平四格表检验只作探索：独立实验单位是供体（24 对 26）。

**关键词.** 牙周炎；sORF；宏蛋白质组；UniDL4BioPep；血脑屏障；金属结合；阿尔茨海默病；计算分诊

---

## 1. Introduction

Alzheimer’s disease is defined by extracellular amyloid-β (Aβ), intracellular hyperphosphorylated tau, synapse loss and a cholinergic deficit [1,2]. Autosomal-dominant cases still fit an amyloid-centred account [2]. Sporadic late-onset disease does not. Infectious and metal-ion modifiers have been proposed for decades. Both remain slogans unless a molecule can leave the mouth, enter brain and touch copper, iron, zinc, Aβ, tau or acetylcholinesterase (AChE).

Chronic periodontitis is common in older adults and tracks with cognitive decline [3,4]. *Porphyromonas gingivalis* is a keystone pathogen of that infection. Dominy and colleagues recovered gingipain antigens and bacterial DNA from AD cortex and cerebrospinal fluid, showed tau cleavage by gingipains, and reduced hippocampal injury in orally infected mice with brain-penetrant gingipain inhibitors [5]. Outer-membrane vesicles carry gingipains at several-fold the surface density of the parent cell [6,7]. Recent clinical work still places gingipain K next to cerebrospinal Aβ and phospho-tau in AD with periodontitis [8]. That literature names proteases and vesicles. It does not count the much larger set of short peptides that an inflamed periodontal metagenome can encode.

Two further constraints shape the present study. First, a six-frame translation of hundreds of metagenome-assembled genomes (MAGs) produces millions of sORF peptides; most will never be seen by a mass spectrometer. A screen that skips proteomic support is a screen of translation noise. Second, predicted bioactivity heads, including UniDL4BioPep [9], return many labels at once. Without an explicit stack—barrier passage, then metal binding, then a chelator-high / scavenger-low rule—the output cannot be synthesised.

This paper therefore asks a countable question. After a periodontitis-specific sORF library is restricted to peptides observed in oral proteomes, how many survive a BBB filter, a neurotoxicity filter, a Cu/Fe/Zn filter, and a chelator-high / scavenger-low rule? The answer is twelve peptides (eight at a stricter scavenger cut). The collection is a **community** oral metagenome [10], not a *P. gingivalis*-only peptidome. Assignment of the twelve sequences to a single species is not claimed. Docking to AChE, including the published Aβ residence patch at residues 344–361 [11], is listed as the next experiment, not as a result.

---

## 2. Methods

### 2.1 Study design and independent unit

This is a computational re-analysis of public assemblies. The independent experimental unit is the donor: 24 healthy controls and 26 periodontitis patients [10]. Peptides are nested within donors. Peptide-level contingency tests, when shown, are exploratory and ignore that clustering.

No new human sampling was performed. Source methods follow the author’s mechanism draft.

### 2.2 sORF libraries

Oral metagenomes were taken from BioProject PRJNA678453 [10] and the companion high-resolution assembly set PRJEB65451. The collection comprises 296 high-quality MAGs. Sample-specific mapping produced healthy-specific and periodontitis-specific sORF libraries. Translations of 4–50 amino acids were retained. Raw library sizes were 11,269,961 (healthy) and 11,721,988 (periodontitis).

### 2.3 Proteomic support

Candidates were matched by hash-indexed exact identity to oral metaproteome peptides. Short-branch proteomes were PXD003151, PXD004319 and PXD026727. The long branch used HOMD. After dereplication the healthy set contained 31,510 peptides (30,557 short + 953 long) and the periodontitis set 33,786 peptides (32,754 short + 1,032 long).

Before group-specific collapse, 98.98% of the short-branch proteome collection sat in 5–30 aa (462,257 / 467,002). HOMD was 98.40% longer than 50 aa, with 298,454 sequences in 31–50 aa. Downstream statistics never pool the two branches.

### 2.4 Length branches

After proteomic dereplication, 5–30 aa sequences form the short branch and 31–50 aa sequences form the long branch. Occasional boundary sequences may sit in files labelled “short”. All reported counts use the observed length bin.

### 2.5 UniDL4BioPep

Functional probabilities were computed with UniDL4BioPep, which embeds peptides with ESM-2 (`esm2_t6_8M_UR50D`) and classifies bioactivities with a convolutional head [9]. Categories included ACE inhibition, tumour T-cell antigen, BBB, antiparasitic, neurotoxicity, antibacterial, antifungal, antiviral, toxicity, antioxidant free-radical scavenging, allergenicity, DPP-IV inhibition, cell-penetrating peptide, bitter, umami, broad antimicrobial, antimalarial, quorum sensing, anticancer and anti-MRSA. For category *c*,

\[
N_{\mathrm{high}}(c)=\sum_i \mathbf{1}\{P_i(c)\ge 0.8\}.
\]

The 0.8 cut is an operational high-confidence rule. It is not a calibrated posterior of wet-lab activity. Software version and random seeds were not stated in the source draft (`AUTHOR_INPUT_NEEDED`).

### 2.6 Three-model filter

Only peptides with BBB probability ≥ 0.8 entered NTxPred2, mebipred and AnOxPePred. NTxPred2 was run on sequences ≥ 7 aa. AnOxPePred supplied a free-radical scavenging score (FRS) and a chelator score (CHEL). Mebipred scored metal-binding potential; Cu, Fe and Zn were retained.

High CHEL and modest FRS defined priority for later metal-linked oxidative-stress work. The source draft states that this class is not experimental pro-oxidant activity.

### 2.7 What was not computed

The source draft lists AChE, butyrylcholinesterase, Aβ42, tau, ApoE4, ferritin and transferrin as structural targets. It then states that the present stage does **not** perform docking, molecular dynamics or QM/MM/DFT. Section 4 of that draft is a protocol for the next version.

GSE42872 (vemurafenib in BRAF-V600E A375 melanoma [12]) and a translation of a 1 μs AChE–Aβ trajectory [11] are archived beside this manuscript. They are not inputs to Tables 1–4.

### 2.8 Exploratory statistics

Donor-level mixed models were not possible from the deposited tables. For description only, two-sided Fisher’s exact tests and χ² tests were computed on peptide 2 × 2 tables (SciPy 1.17). Odds ratios are periodontitis versus healthy unless noted. No multiple-comparison correction was applied across UniDL4BioPep heads. These *P* values do not replace a donor-level analysis.

### 2.9 Figures

Figures were drawn in Python 3 (matplotlib) with a colour-blind-safe pair (blue `#0072B2`, vermillion `#D55E00`). Vector PDFs are the submission masters; PNGs are previews.

---

## 3. Results

### 3.1 Proteomes discard more than 99.7% of translated sORFs

Raw sORF libraries contained 11,269,961 healthy and 11,721,988 periodontitis sequences. Exact proteomic support left 31,510 and 33,786 unique peptides (Table 1). Passage rates were 0.2796% and 0.2882%. Periodontitis contributed 51.75% of the combined confirmed library (65,296 peptides).

**Table 1.** Proteomic support of group-specific sORFs.

| Group | Specific sORFs | Unique supported peptides | Passage (%) | Share of confirmed library (%) |
| --- | ---: | ---: | ---: | ---: |
| Healthy | 11,269,961 | 31,510 | 0.2796 | 48.25 |
| Periodontitis | 11,721,988 | 33,786 | 0.2882 | 51.75 |
| Total | 22,991,949 | 65,296 | 0.2839 | 100.00 |

A peptide-level χ² test on passage is statistically significant because the denominators are huge (χ² = 15.1, *P* = 1.0 × 10⁻⁴). The absolute difference is 0.0086 percentage points. We do not interpret that *P* value as a biological effect. The confirmed sets are the only denominators used below.

### 3.2 BBB calls: counts rise in periodontitis; only the long branch changes in rate

At BBB probability ≥ 0.8 the short branch yielded 3,359 healthy and 3,446 periodontitis peptides (10.99% vs 10.52% of each proteome-supported short set). The long branch yielded 40 and 72 (4.20% vs 6.98%).

An exploratory Fisher test on the long-branch 2 × 2 table gives OR = 1.71 for periodontitis versus healthy (*P* = 0.0084). The corresponding short-branch test is not significant (OR = 0.95 for periodontitis, *P* = 0.056). Absolute periodontitis excess, plus the long-branch rate, is what feeds the AD-oriented funnel. Short-branch BBB **percentages** do not support a “more BBB-positive periodontitis peptidome” slogan.

### 3.3 Long peptides: barrier and antibacterial heads move together

Backgrounds are 953 healthy and 1,032 periodontitis long peptides. Table 2 reports every UniDL4BioPep head at *P* ≥ 0.8. Periodontitis is higher for BBB, antibacterial, anti-MRSA, cell-penetrating and antifungal calls (Fig. 2a). An exploratory Fisher test on long-branch antibacterial calls gives OR = 1.32 (*P* = 0.040). Bitter is the most frequent call in both groups (66.63% and 62.11%) and is not treated as an AD phenotype.

**Table 2.** Long-peptide high-confidence UniDL4BioPep counts (background 953 / 1,032).

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

### 3.4 Short peptides: counts track library size; one head saturates

Backgrounds are 30,557 healthy and 32,754 periodontitis short peptides. The source draft highlights periodontitis **counts** for BBB (3,446), NeuroPred (4,019), Anti-MRSA (4,728) and quorum sensing (12,674) (Fig. 2b). Percentages in those four rows are similar across groups (Table 3). Exploratory Fisher tests on NeuroPred, Anti-MRSA and quorum sensing are all *P* > 0.11.

Broad `Antimicrobial_activity` is called on 99.93% and 99.90% of the two short sets. That ceiling is a property of the classifier head. It is not a census of oral antibiotics.

**Table 3.** Short-peptide high-confidence UniDL4BioPep counts (background 30,557 / 32,754).

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

### 3.5 The BBB set is mostly 8–15 aa

Restricting the periodontitis-oriented joint library to BBB ≥ 0.8 gave 3,518 peptides: 3,446 short and 72 long. Of the short BBB set, 2,893 (83.95%) were 8–15 aa, 547 were 5–7 aa and 6 were 16–30 aa (Fig. 4). All 72 long peptides sit in 31–50 aa. An AD-oriented wet list will therefore be dominated by 8–15-mer chemistry. HOMD long peptides are a small, separate branch.

### 3.6 Three models collapse 3,518 peptides to 12 (8)

The 3,518 BBB peptides entered NTxPred2, mebipred and AnOxPePred (Table 4; Fig. 3).

NTxPred2 does not accept sequences shorter than 7 aa, so 219 peptides were skipped and 3,299 were scored. Of those, 923 were called neurotoxic, all ≤ 30 aa. Subsequent metal and antioxidant tallies use the 3,299 scored sequences as background.

Mebipred at 0.5 marked 111 Cu/Fe/Zn-positive peptides. Those 111 were submitted to AnOxPePred. Three batches of `Chelator_All.txt` and `Scavenger_All.txt` were merged on SeqID so each peptide carried both CHEL and FRS.

CHEL ≥ 0.25 selected 15 peptides. Adding FRS < 0.50 left **12 main candidates**. Tightening to FRS < 0.45 left **8 high-confidence peptides**.

**Table 4.** Three-model funnel.

| Stage | Rule | *n* |
| --- | --- | ---: |
| BBB short | BBB ≥ 0.8, 5–30 aa | 3,446 |
| BBB long | BBB ≥ 0.8, 31–50 aa | 72 |
| BBB total | BBB ≥ 0.8 | 3,518 |
| NTxPred2 output | scored sequences | 3,299 |
| Neurotoxic | NTxPred2 = Neurotoxic (all ≤ 30 aa) | 923 |
| Cu/Fe/Zn binders | mebipred 0.5 | 111 |
| CHEL ≥ 0.25 | AnOxPePred | 15 |
| Main set | CHEL ≥ 0.25 and FRS < 0.50 | **12** |
| High-confidence subset | CHEL ≥ 0.25 and FRS < 0.45 | **8** |

The twelve sequences are not printed in the deposited Word/PDF tables and are not invented here (`AUTHOR_INPUT_NEEDED` for v0.4).

---

## 4. Discussion

The operational product of this stage is a twelve-peptide list. Two facts are required to read it. Proteomes throw away more than 99.7% of translated sORFs, so AD claims that skip that collapse are claims about six-frame noise. A BBB-first, metal-second, scavenger-low stack then reduces 33,786 periodontitis-supported peptides to 12. That is a prioritisation result. It is the correct grain size for a manuscript that has not docked anything.

The companion review’s chain—oral peptide, metal coordination, Fenton chemistry, neurotoxicity—explains why the CHEL-high / FRS-low cut exists [5–8,13]. A peptide predicted to bind copper or iron, and not predicted to be a strong radical scavenger, is the peptide a chemist should make next. The cut is not ROS.

Short-branch BBB and NeuroPred **percentages** barely move between groups. What moves is the absolute periodontitis count and the long-branch BBB rate. Sentences that say “periodontitis peptides are more BBB-positive” should point to those two observations only.

UniDL4BioPep labels are transferred from heterogeneous training sets [9]. A 99.9% antimicrobial call on short peptides is a prior of that head. NTxPred2’s length gate drops 219 BBB peptides before neurotoxicity is asked. Mebipred at 0.5 is another operational knife. None of the twelve sequences has, in this draft, an ITC *K*d, a DCFH-DA fold-change or an AChE IC50.

Gingipain neuropathology [5,8] and AChE-accelerated Aβ fibril growth [11,14,15] remain backdrop. Atanasova and colleagues kept Aβ on AChE for 1 μs and mapped the main residence to residues 344–361, adjacent to the peripheral anionic site and poorly covered by dual-site inhibitors [11]. That patch is where the twelve peptides should be docked next. It is not where they have been docked.

The MAG collection is a community oral metagenome [10]. Calling the twelve peptides “*P. gingivalis* peptides” would be a taxonomy error until each sequence is assigned. GSE42872 is a six-sample melanoma microarray [12] and must not enter an AD contrast.

The source draft already writes the next protocol: multi-conformer models for 7–15 aa peptides; AlphaFold3 complexes with proteins and metal ions; docking to AChE (catalytic site, peripheral site, 344–361), Aβ42, tau, ApoE4, ferritin and transferrin; MD and MM/GBSA ranking; QM/MM only on stable coordination shells; then metal binding, Cu/Fe-dependent ROS, lipid peroxidation, cholinesterase activity, Aβ aggregation and neuronal toxicity. The draft’s stopping rule stands. Only a peptide that raises ROS or lipid peroxidation **in the presence of metal** and damages neurons earns the phrase “metal-linked pro-oxidant neurotoxicity.”

Limitations are those of a single 24-versus-26 donor collection, exact-match proteomics, black-box predictors at fixed cuts, missing sequence tables, and no new wet data. Peptide-level *P* values ignore donor clustering and are not confirmatory.

---

## 5. Conclusions

A periodontitis-specific sORF screen, collapsed by oral proteomes and filtered for predicted BBB passage, Cu/Fe/Zn binding and a chelator-high / scavenger-low profile, yields twelve peptides (eight at the stricter FRS cut). The list is large enough to be a project and small enough to synthesise. It is not an AChE structure paper, not a gingipain immunohistochemistry paper, and not a melanoma microarray paper. Those files share a folder because they share a desk.

---

## Statistical analysis (ready-to-paste)

Independent experimental units were donors (healthy *n* = 24; periodontitis *n* = 26). Peptide counts are nested observations. Descriptive statistics are counts and percentages of proteome-supported peptides within length branch. Exploratory two-sided Fisher’s exact tests on peptide 2 × 2 tables used SciPy 1.17; no multiplicity correction was applied across UniDL4BioPep categories. Donor-level mixed models were not fitted because a donor-by-peptide matrix was not deposited. Software versions for UniDL4BioPep, NTxPred2, mebipred and AnOxPePred were not stated in the source draft.

---

## Declarations

**Data availability.** PRJNA678453, PRJEB65451, PXD003151, PXD004319, PXD026727 and HOMD are public. Author tables are in `projects/1yzy-pg-ad-mechanism/source-docs/`.

**Code availability.** Figure scripts can be recovered from the commit that added `manuscript/figures/fig1_design.pdf` through `fig4_bbb_length.pdf`. UniDL4BioPep is described by Du et al. [9].

**Ethics.** No new human or animal work.

**Competing interests.** None recorded.

**Funding.** None recorded.

**Author contributions.** `AUTHOR_INPUT_NEEDED`.

**AI use.** An AI assistant assembled this manuscript from the author’s methods/results draft under the nature-skills / AERS workflow. The author remains responsible for every number and claim.

---

## Figure legends

**Figure 1.** Screening design. Two hundred and ninety-six MAGs from 24 healthy and 26 periodontitis donors were translated to 4–50 aa sORFs, collapsed by exact oral-proteome identity, scored with UniDL4BioPep, and filtered for BBB, neurotoxicity, metal binding and chelator/scavenger scores.

**Figure 2.** Selected UniDL4BioPep heads. (a) Long-peptide high-confidence rates (background 953 / 1,032). (b) Short-peptide high-confidence counts (background 30,557 / 32,754). Blue, healthy; vermillion, periodontitis.

**Figure 3.** Computational funnel from 33,786 periodontitis-supported peptides to 12 main and 8 high-confidence candidates. Horizontal axis is logarithmic.

**Figure 4.** Length mix of 3,518 BBB-positive peptides. Most short BBB peptides are 8–15 aa.

---

## References

1. Scheltens P, De Strooper B, Kivipelto M, Holstege H, Chételat G, Teunissen CE, et al. Alzheimer's disease. Lancet. 2021;397(10284):1577-1590. doi:10.1016/S0140-6736(20)32205-4  
2. Selkoe DJ, Hardy J. The amyloid hypothesis of Alzheimer's disease at 25 years. EMBO Mol Med. 2016;8(6):595-608. doi:10.15252/emmm.201606210  
3. Ide M, Harris M, Stevens A, Sussams R, Hopkins V, Culliford D, et al. Periodontitis and cognitive decline in Alzheimer's disease. PLoS One. 2016;11(3):e0151081. doi:10.1371/journal.pone.0151081  
4. Sparks Stein P, Desrosiers M, Donegan SJ, Yepes JF, Kryscio RJ. Tooth loss, dementia and neuropathology in the Nun study. J Am Dent Assoc. 2007;138(10):1314-1322. doi:10.14219/jada.archive.2007.0046  
5. Dominy SS, Lynch C, Ermini F, Benedyk M, Marczyk A, Konradi A, et al. *Porphyromonas gingivalis* in Alzheimer's disease brains: evidence for disease causation and treatment with small-molecule inhibitors. Sci Adv. 2019;5(1):eaau3333. doi:10.1126/sciadv.aau3333  
6. Ho MH, Chen CH, Goodwin JS, Wang BY, Xie H. Functional advantages of *Porphyromonas gingivalis* vesicles. PLoS One. 2015;10(4):e0123448. doi:10.1371/journal.pone.0123448  
7. Nara PL, Sindelar D, Penn MS, Potempa J, Griffin WST. *Porphyromonas gingivalis* outer membrane vesicles as the major driver of and explanation for neuropathogenesis, the cholinergic hypothesis, iron dyshomeostasis, and salivary lactoferrin in Alzheimer's disease. J Alzheimers Dis. 2021;82(4):1417-1450. doi:10.3233/JAD-210448  
8. Frontiers in Aging Neuroscience. Different stages of Alzheimer’s disease with periodontitis: clinical features and potential mechanisms involving gingipains. 2026. doi:10.3389/fnagi.2026.1737524. Confirm author line on the publisher PDF before submission.  
9. Du Z, Ding X, Xu Y, Li Y. UniDL4BioPep: a universal deep learning architecture for binary classification in peptide bioactivity. Brief Bioinform. 2023;24(3):bbad135. doi:10.1093/bib/bbad135  
10. Belstrøm D, Constancias F, Markvart M, Sikora M, Sørensen CE, Givskov M. Periodontitis associates with species-specific gene expression of the oral microbiota. npj Biofilms Microbiomes. 2021;7:76. doi:10.1038/s41522-021-00247-y  
11. Atanasova M, Dimitrov I, Ivanov S. Molecular dynamics simulations of acetylcholinesterase – beta-amyloid peptide complex. Cybern Inf Technol. 2020;20(6):140-154. doi:10.2478/cait-2020-0068  
12. Parmenter TJ, Kleinschmidt M, Kinross KM, Bond ST, Li J, Kaadige MR, et al. Response of BRAF-mutant melanoma to BRAF inhibition is mediated by a network of transcriptional regulators of glycolysis. Cancer Discov. 2014;4(4):423-433. doi:10.1158/2159-8290.CD-13-0440  
13. Kanagasingam S, Chukkapalli SS, Welbury R, Singhrao SK. *Porphyromonas gingivalis* is a strong risk factor for Alzheimer's disease. J Alzheimers Dis Rep. 2020;4(1):501-511. doi:10.3233/ADR-200250  
14. Inestrosa NC, Alvarez A, Pérez CA, Moreno RD, Vicente M, Linker C, et al. Acetylcholinesterase accelerates assembly of amyloid-β-peptides into Alzheimer's fibrils: possible role of the peripheral site of the enzyme. Neuron. 1996;16(4):881-891. doi:10.1016/s0896-6273(00)80108-7  
15. De Ferrari GV, Canales MA, Shin I, Weiner LM, Silman I, Inestrosa NC. A structural motif of acetylcholinesterase that promotes amyloid β-peptide fibril formation. Biochemistry. 2001;40(35):10447-10457. doi:10.1021/bi0101392  
