# A Proteome-Supported Screen of Periodontitis-Associated Oral sORF Peptides Yields Twelve Metal-Binding, Barrier-Passing Candidates That Dock to the Pathogenic Peripheral Anionic Site of Human Acetylcholinesterase

# 牙周炎相关口腔 sORF 肽的蛋白质组支持筛选：十二条金属结合、可过屏障候选多肽对接人乙酰胆碱酯酶致病性外周阴离子位点

**Bilingual section-parallel scientific-content draft / 中英文分节对照科学内容草案**

**Article type:** Original Research Article (computational screening with structure-based follow-up)  
**Draft status:** Submission-oriented scientific-content draft for accountable-author review. Author names, affiliations, correspondence details, journal-specific formatting, and author-approved declarations were not supplied and are not inferred.

**文章类型：** 原创研究论文（计算筛选 + 结构层面跟进）  
**稿件状态：** 面向投稿、供责任作者审核的科学内容草案。因未提供作者姓名、单位、通讯信息、期刊特定格式及经作者批准的声明，本稿不作推定或虚构补写。

## Abstract / 摘要

### English

**Background:** Periodontitis is epidemiologically associated with Alzheimer’s disease (AD), yet most molecular accounts stop at intact *Porphyromonas gingivalis* cells, gingipain proteases, or outer-membrane vesicles. Short peptides encoded by oral small open reading frames (sORFs) are a larger, poorly counted cargo, and the peripheral anionic site (PAS) of acetylcholinesterase (AChE)—the surface that accelerates amyloid-β (Aβ) fibril assembly—has not been used to triage them.

**Methods:** We re-analysed a public oral metagenome collection (BioProject PRJNA678453; assembly set PRJEB65451) comprising 296 high-quality metagenome-assembled genomes from 24 healthy and 26 periodontitis donors. Group-specific sORF libraries (4–50 amino acids) were collapsed by exact identity against HOMD-linked oral proteomes, scored with UniDL4BioPep at predicted probability ≥ 0.8 with short (5–30 aa) and long (31–50 aa) branches kept separate, and passed through NTxPred2, mebipred and AnOxPePred. The resulting candidates were docked with AutoDock Vina 1.2.5 into a 40 × 40 × 40 Å³ box centred on the PAS of human AChE (PDB 4EY6).

**Results:** Raw libraries contained 11,269,961 healthy and 11,721,988 periodontitis sORFs; proteomic support left 31,510 and 33,786 peptides (passage 0.2796% and 0.2882%). Periodontitis contributed more blood–brain-barrier (BBB) calls in both branches (short 3,446 vs 3,359; long 72 vs 40). Of 3,518 BBB-positive peptides, NTxPred2 called 923 of 3,299 scored sequences neurotoxic, mebipred marked 111 Cu/Fe/Zn binders, and a chelator-high / scavenger-low rule left 12 main candidates (8 at the stricter cut). All twelve are 7–9-mers; eleven carry histidine and six carry cysteine, matching the His/Cys anchoring chemistry of metal-binding neurotoxic peptide paradigms such as tau26–44. Every candidate docked fully inside the PAS-centred box with Vina scores of −8.25 to −9.60 kcal/mol, adopting gorge-spanning poses that contact PAS residues (Tyr72, Asp74, Tyr124, Trp286, Tyr341) and gorge aromatics (Trp86, Phe295, Tyr337, Phe338); several side chains reach the Ser203/His447 catalytic region.

**Conclusions:** The workflow converts an uncounted oral peptidome into a ranked, structurally plausible twelve-peptide shortlist positioned on a disease-relevant AChE surface. Docking scores rank poses; they are not binding constants. A 100-ns molecular dynamics check was attempted and excluded after pressure instabilities. Only metal binding, Cu/Fe-dependent reactive oxygen species, lipid peroxidation, cholinesterase activity, Aβ aggregation and neuronal viability assays can promote any candidate to a mechanistic claim.

**Keywords:** periodontitis; small open reading frame; metaproteome; blood–brain barrier; metal binding; acetylcholinesterase; peripheral anionic site; molecular docking; Alzheimer’s disease

### 中文

**背景：** 牙周炎与阿尔茨海默病（AD）存在流行病学关联，但多数分子机制叙述止步于完整牙龈卟啉单胞菌、牙龈蛋白酶或外膜囊泡。口腔小开放阅读框（sORF）编码的短肽是更大、却很少被清点的货物；乙酰胆碱酯酶（AChE）的外周阴离子位点（PAS）——加速 β-淀粉样肽（Aβ）纤毛组装的表面——从未被用于对这类肽进行分诊。

**方法：** 我们再分析公开口腔宏基因组（BioProject PRJNA678453；组装集 PRJEB65451），包含来自 24 名健康对照与 26 名牙周炎患者的 296 个高质量宏基因组组装基因组（MAG）。组特异 sORF 库（4–50 氨基酸）经 HOMD 相关口腔蛋白质组精确匹配塌缩，用 UniDL4BioPep 以预测概率 ≥ 0.8 打分（短肽支 5–30 aa 与长肽支 31–50 aa 分开），再经 NTxPred2、mebipred 与 AnOxPePred 过滤。所得候选以 AutoDock Vina 1.2.5 对接到人 AChE（PDB 4EY6）PAS 为中心的 40 × 40 × 40 Å³ 盒子。

**结果：** 原始库含健康 11,269,961 条与牙周炎 11,721,988 条 sORF；蛋白质组支持后分别剩 31,510 与 33,786 条（通过率 0.2796% 与 0.2882%）。牙周炎组血脑屏障（BBB）阳性在两支均更多（短肽 3,446 对 3,359；长肽 72 对 40）。3,518 条 BBB 阳性肽中，NTxPred2 对 3,299 条打分序列判出 923 条神经毒性，mebipred 标出 111 条 Cu/Fe/Zn 结合阳性，"螯合高/清除低"规则留下主候选 12 条（严格阈值下 8 条）。十二条均为 7–9 肽：11 条含组氨酸、6 条含半胱氨酸，与 tau26–44 等金属结合神经毒肽范例的 His/Cys 锚定化学一致。所有候选完整进入 PAS 中心盒子，Vina 打分 −8.25 至 −9.60 kcal/mol，呈跨越峡部的结合模式，接触 PAS 残基（Tyr72、Asp74、Tyr124、Trp286、Tyr341）与峡部芳香残基（Trp86、Phe295、Tyr337、Phe338）；部分侧链延伸至 Ser203/His447 催化区。

**结论：** 该流程把未被清点的口腔肽组转化为一个有排序、结构上合理的十二肽候选名单，且定位在疾病相关的 AChE 表面。对接打分是构象排序工具，不是结合常数。100 ns 分子动力学核查已尝试，因压力不稳定被排除。只有金属结合、Cu/Fe 依赖活性氧、脂质过氧化、胆碱酯酶活性、Aβ 聚集与神经元存活实验，才能把任何候选升格为机制结论。

**关键词：** 牙周炎；小开放阅读框；宏蛋白质组；血脑屏障；金属结合；乙酰胆碱酯酶；外周阴离子位点；分子对接；阿尔茨海默病

## 1. Introduction / 1 引言

### English

#### 1.1 Alzheimer’s disease and the non-canonical role of acetylcholinesterase

Alzheimer’s disease (AD) is neuropathologically defined by extracellular amyloid-β (Aβ) plaques, intracellular hyperphosphorylated tau neurofibrillary tangles, synapse loss and a progressive cholinergic deficit [1,2]. The amyloid cascade remains the most economical account of autosomal-dominant disease, while sporadic late-onset AD is better described as a convergence of several upstream processes [2]. Among those, the cholinergic hypothesis occupies a special place: it is the only one that has continuously produced approved symptomatic therapy. Acetylcholinesterase (AChE) inhibitors—donepezil, rivastigmine, galantamine—remain first-line treatment decades after introduction, precisely because the basal forebrain cholinergic projection is an early and persistent casualty of the disease [3].

AChE, however, is not only the enzyme that terminates cholinergic signalling. Since the mid-1990s, Inestrosa and colleagues have shown that AChE accelerates the assembly of Aβ peptides into Alzheimer-type fibrils, and that this “chaperone” activity resides at the peripheral anionic site (PAS), the entrance rim of the enzyme’s deep active-site gorge [4]. A conserved structural motif of the PAS is sufficient to promote fibril formation even when detached from catalysis [5], and human AChE-induced Aβ aggregation can be blocked by ligands that occupy the peripheral site [6]. Structural work on inhibitor complexes—from the donepezil-bound gorge [7] to the recombinant human enzyme panels crystallised by Cheung et al. [8]—established that the gorge is druggable at both ends: the catalytic anionic site (CAS) at the bottom, and the PAS at the rim. A long all-atom molecular dynamics study of the AChE–Aβ complex mapped the peptide’s main residence to AChE residues 344–361, a patch adjacent to the PAS and poorly covered by dual-site inhibitors [9]; accelerated-MD work converges on the same region [10]. The practical implication is that PAS occupancy is a disease-relevant event: anything that sits on the PAS may interfere with AChE-catalysed Aβ fibril growth, and the PAS is therefore a legitimate docking target even for molecules that are not classical substrates.

#### 1.2 The periodontitis–Alzheimer axis: cells, proteases, vesicles—and a missing peptide inventory

Chronic periodontitis is common in older adults and tracks with cognitive decline and dementia. In a longitudinal AD cohort, periodontitis at baseline was associated with a six-fold higher rate of cognitive decline over six months [11], and tooth loss predicted dementia and neuropathology in the Nun study [12]; text-mining and GEO-based analyses likewise place chronic periodontitis among AD risk conditions [13]. The mechanistic centre of gravity in this literature is *Porphyromonas gingivalis*, a keystone pathogen of the dysbiotic periodontal pocket. Dominy et al. recovered gingipain proteases and *P. gingivalis* DNA from AD cortex and cerebrospinal fluid, demonstrated gingipain-mediated tau cleavage, and reduced hippocampal injury in orally infected mice with brain-penetrant gingipain inhibitors [14]. *P. gingivalis* and its lipopolysaccharide have been detected directly in AD brain tissue [15], chronic oral application of the pathogen drives Aβ production and neuroinflammation in wild-type mice [16], and gingipain activity in infected neurons produces AD-like neurodegeneration that a gingipain inhibitor can blunt [17]. Two delivery vehicles deserve emphasis: outer-membrane vesicles carry gingipains at several-fold the surface density of the parent cell and are sized for tissue transit [18,19], and gingipains themselves act with surgical precision on some substrates while degrading others indiscriminately [20]. Clinical and review-level work continues to place *P. gingivalis* and its gingipains close to CSF Aβ and phospho-tau in AD patients with periodontitis [21–23], and serotype-dependent AD-like pathology has been reproduced in rats [24].

What this literature names are cells, proteases, lipopolysaccharide and vesicles. What it does not enumerate is the much larger set of short peptides that an inflamed periodontal metagenome can encode—peptides released by gingipain processing, by bacterial turnover, or translated from small open reading frames (sORFs) that never appear in gene catalogues. If the periodontitis–AD link is ever to be stated at peptide resolution, that inventory has to be counted, and the counts have to be filtered for the properties a neuroactive peptide would need: survival in the proteome record, barrier passage, metal handling, and plausible neural targets.

#### 1.3 The metal hypothesis needs a carrier

The second pillar of this study is the metal hypothesis of AD. Copper, iron and zinc accumulate in amyloid plaques and neurofibrillary tangles, their homeostatic machinery is disrupted in AD brain, and each ion can modulate Aβ and tau aggregation, redox chemistry and synaptic function [25]. In the elementomic framing of Lei, Ayton and Bush, iron, copper, zinc and selenium signatures are among the few AD-associated abnormalities that have already been translated into therapeutic attempts (clioquinol, PBT2, iron chelation), and iron-driven lipid peroxidation—ferroptosis—is now a recognised executor pathway in neurodegeneration [26]. The chemistry is straightforward in principle: Cu(I)/Cu(II) and Fe(II)/Fe(III) couples cycle electrons with H₂O₂ and O₂ (Fenton/Haber–Weiss chemistry), generating hydroxyl and other radicals that peroxidise membranes and cross-link proteins; Zn(II) is redox-silent but reorganises Aβ and tau assemblies.

The gap in that account is the carrier problem. Metal dyshomeostasis in AD is usually discussed as a failure of host transporters and storage proteins. A periodontitis-linked account additionally needs a molecule that can leave the mouth, survive serum, cross or bypass the blood–brain barrier (BBB), and present redox-active coordination chemistry inside brain parenchyma. Short, His/Cys-rich peptides are among the few molecular formats that plausibly do all of those things, which motivates screening the oral metaproteome for exactly that chemistry.

#### 1.4 Exogenous short peptides can be neuroactive: the tau26–44 paradigm

The idea that a short peptide can be a neurotoxic effector in its own right is not hypothetical. The best-characterised template comes not from a bacterium but from tau itself. The N-terminal tau fragment spanning residues 26–44 (tau26–44) is the minimal active moiety of a 20–22 kDa NH₂-derived tau peptide that accumulates at AD synapses; applied extracellularly it provokes presynaptic glutamate-release deficits, perturbs membrane nanomechanics, and at higher exposure drives NMDA-receptor-mediated, necrotic-type neuronal death [27,28]. Two properties of tau26–44 matter here. First, despite being only 19 residues long, it is intrinsically disordered yet structured enough to be toxic: atomic-force spectroscopy, small-angle X-ray scattering and molecular dynamics jointly revealed transient secondary and tertiary determinants that its inactive reverse-sequence control lacks [28]. Short neurotoxic peptides are therefore dynamic conformational ensembles, not single rigid keys. Second, tau26–44 coordinates Cu(II) through its histidine residue; the Cu(II) complex alters peptide conformation and differentially modulates copper-induced Aβ aggregation, placing a 19-mer peptide squarely at the intersection of tau biology, copper chemistry and amyloid pathology [27]. A complementary inorganic-chemistry literature shows the same His/Cys anchoring logic across tau fragments [27]. Outside the human proteome, bacterial amyloids provide an exogenous precedent: oral ingestion of the functional amyloid curli enhances α-synuclein aggregation in aged rats and *C. elegans*, evidence that bacterial peptide assemblies can cross-seed human amyloidogenic proteins in vivo [29].

These observations define the template against which our exogenous candidates should be read: a 7–20-residue peptide, His/Cys-equipped for metal coordination, conformationally dynamic, and experimentally falsifiable. They also fix the experimental bar: tau26–44 toxicity is a wet-lab statement (NMDA dependence, necrosis, membrane perturbation), and no computational predictor substitutes for it.

#### 1.5 Small open reading frames and the case for proteome-supported screening

The peptide inventory itself comes from sORF biology. Eukaryotic and microbial genomes translate thousands of short open reading frames into micropeptides with real functions, most of which were invisible to classical annotation [30]; ribosome-profiling and proteogenomic surveys keep expanding the translated landscape, including in the heart and other tissues previously thought peptide-silent [31]. Metagenomics amplifies this problem: six-frame translation of hundreds of metagenome-assembled genomes (MAGs) yields millions of hypothetical 4–50-residue sequences. Most of those translations will never be observed by a mass spectrometer; a screen that skips proteomic support is a screen of translation noise. Two consequences follow for study design. First, group-specific sORF libraries must be collapsed against oral metaproteomes before any bioactivity prediction. Second, predicted bioactivity is multivariate—barrier passage, metal binding, oxidative behaviour—so the output of deep-learning predictors such as UniDL4BioPep [32] is only usable through an explicit decision stack, not through single-head cut-offs.

#### 1.6 The present study

This paper has two stages. Stage one (Sections 2.2–2.9, 3.1–3.6) asks the countable question: after a periodontitis-associated sORF library is restricted to peptides observed in oral proteomes, how many survive a BBB filter, a neurotoxicity filter, a Cu/Fe/Zn filter, and a chelator-high / scavenger-low rule? The answer is twelve peptides (eight at a stricter scavenger cut). Stage two (Sections 2.10–2.11, 3.7) takes the twelve sequences—supplied by the author—to the structure level by PAS-focused molecular docking against human AChE (PDB 4EY6 [8]), the PAS being chosen because it is both the Aβ-accelerating site of AChE [4–6] and the neighbourhood of the published Aβ residence patch at residues 344–361 [9].

Three boundaries are stated up front. (i) The MAG collection is a **community** oral metagenome [33], not a *P. gingivalis*-only peptidome; assignment of the twelve sequences to a single species is not claimed. (ii) Docking scores are ranking heuristics with known scoring-function bias; they are used here to compare twelve candidates against one binding site, not to predict dissociation constants. (iii) Molecular dynamics, QM/MM and all wet assays remain future work (Sections 2.11 and 4.5); the stopping rule stands—only a peptide that raises reactive oxygen species (ROS) or lipid peroxidation **in the presence of metal** and damages neurons earns the phrase “metal-linked pro-oxidant neurotoxicity.”

### 中文

#### 1.1 阿尔茨海默病与乙酰胆碱酯酶的非经典角色

阿尔茨海默病（AD）的神经病理定义包括细胞外 β-淀粉样肽（Aβ）斑块、细胞内过度磷酸化 tau 神经原纤维缠结、突触丢失和进行性胆碱能缺损 [1,2]。对常染色体显性病例，淀粉样级联仍是最简洁的解释；散发性晚发型 AD 更适合被描述为多条上游通路的汇聚 [2]。其中胆碱能假说地位特殊：它是唯一持续产出获批对症治疗的假说。AChE 抑制剂——多奈哌齐、卡巴拉汀、加兰他敏——在引入数十年后仍是一线用药，正因为基底前脑胆碱能投射是该病最早、最持久的受害者之一 [3]。

然而 AChE 不只是终止胆碱能信号的酶。自 1990 年代中期起，Inestrosa 等证明 AChE 加速 Aβ 肽组装成阿尔茨海默型纤毛，且这种"分子伴侣"活性位于外周阴离子位点（PAS），即酶深活性峡部入口的边环 [4]。PAS 上一个保守结构基序即使脱离催化也足以促进纤毛形成 [5]；占据外周位点的配体可以阻断人 AChE 诱导的 Aβ 聚集 [6]。从多奈哌齐结合的峡部结构 [7] 到 Cheung 等结晶的重组人酶面板 [8]，结构工作确立了峡部两端皆可成药：底部的催化阴离子位点（CAS）与边沿的 PAS。一项长时间全原子分子动力学研究把 AChE–Aβ 复合物的 Aβ 主驻留区定位到 AChE 344–361 残基，这片区域紧邻 PAS 且双位点抑制剂覆盖不足 [9]；加速分子动力学工作收敛到同一区域 [10]。其实际含义是：PAS 占据是疾病相关事件——任何坐在 PAS 上的分子都可能干扰 AChE 催化的 Aβ 纤毛生长，因此 PAS 即使对非经典底物也是正当的对接靶点。

#### 1.2 牙周炎–阿尔茨海默轴：细胞、蛋白酶、囊泡——以及缺失的肽清单

慢性牙周炎在老年人中常见，并与认知下降和痴呆同步进展。一项纵向 AD 队列中，基线牙周炎与六个月内认知下降速率升高约六倍相关 [11]；修女研究中牙齿缺失可预测痴呆与神经病理 [12]；文本挖掘与 GEO 分析也把慢性牙周炎列入 AD 风险条件 [13]。这批文献的机制重心是牙龈卟啉单胞菌——失调牙周袋的关键病原体。Dominy 等从 AD 皮层与脑脊液中回收牙龈蛋白酶与牙龈卟啉单胞菌 DNA，证明牙龈蛋白酶切割 tau，并用可入脑的牙龈蛋白酶抑制剂减轻口腔感染小鼠的海马损伤 [14]。牙龈卟啉单胞菌及其脂多糖已在 AD 脑组织中被直接检出 [15]；慢性口服给予该病原体可在野生型小鼠中驱动 Aβ 产生与神经炎症 [16]；感染神经元中持续的牙龈蛋白酶活性产生可被抑制剂钝化的 AD 样神经退行 [17]。两种递送载体值得强调：外膜囊泡携带的牙龈蛋白酶密度是菌体表面的数倍且尺寸适合组织转运 [18,19]；牙龈蛋白酶本身对部分底物如外科手术般精确，对其余底物则无差别降解 [20]。临床与综述层面的工作继续把牙龈卟啉单胞菌及其牙龈蛋白酶与伴牙周炎 AD 患者的脑脊液 Aβ 及磷酸化 tau 联系在一起 [21–23]；大鼠模型中还重现了血清型依赖的 AD 样病理 [24]。

这些文献点名的是细胞、蛋白酶、脂多糖与囊泡；没有清点的是发炎牙周宏基因组能编码的、数量大得多的短肽——由牙龈蛋白酶加工、菌体周转释放，或来自从不出现在基因目录中的小开放阅读框（sORF）的翻译产物。若要把牙周炎–AD 关联说到肽的分辨率，就必须清点这份清单，并按神经活性肽所需的性质过滤：在蛋白质组记录中存活、过屏障、处理金属、有合理的神经靶点。

#### 1.3 金属假说需要一个载体

本研究第二支柱是 AD 的金属假说。铜、铁、锌在淀粉样斑块与神经原纤维缠结中富集，其稳态机制在 AD 脑中紊乱，每种离子都能调节 Aβ 与 tau 聚集、氧化还原化学与突触功能 [25]。在 Lei、Ayton 与 Bush 的元素组学框架中，铁、铜、锌、硒的特征性改变是少数已转化为治疗尝试（氯碘喹啉、PBT2、铁螯合）的 AD 相关异常，铁驱动的脂质过氧化——铁死亡——已是公认的神经退行执行通路 [26]。化学原理本身直接：Cu(I)/Cu(II) 与 Fe(II)/Fe(III) 电对与 H₂O₂ 和 O₂ 循环交换电子（Fenton/Haber–Weiss 化学），产生羟基自由基等活性物种，过氧化膜脂并交联蛋白；Zn(II) 无氧化还原活性，但能重组 Aβ 与 tau 组装体。

该叙事的缺口是"载体问题"。AD 中的金属稳态失衡通常被讨论为宿主转运与储存蛋白的故障；牙周炎关联的叙事还需要一个分子：能离开口腔、在血清中存活、跨越或绕过血脑屏障（BBB）、并在脑实质内呈现氧化还原活性配位化学。短而富含 His/Cys 的肽是少数能同时满足这些条件的分子形式之一——这正是按该化学筛查口腔宏蛋白质组的动机。

#### 1.4 外源短肽可以有神经活性：tau26–44 范例

短肽本身可以成为神经毒性效应分子，这一点并非假设。最完整的模板不来自细菌，而来自 tau 自身。tau 蛋白 N 端 26–44 片段（tau26–44）是一个 20–22 kDa NH₂ 端 tau 肽的最小活性单元，后者在 AD 突触处累积；胞外施加时它引起突触前谷氨酸释放缺陷、扰动膜纳米力学，高暴露时驱动 NMDA 受体介导的坏死型神经元死亡 [27,28]。tau26–44 有两个性质与本工作相关。第一，它仅 19 个残基，本质无序却"结构足够"而有毒：原子力谱、小角 X 射线散射与分子动力学共同揭示了其无活性反序对照所缺乏的瞬时二级与三级结构决定簇 [28]。短神经毒肽因此是动态构象系综，不是单一刚性钥匙。第二，tau26–44 经组氨酸配位 Cu(II)；Cu(II) 复合物改变肽构象并差异性调节铜诱导的 Aβ 聚集，把一条 19 肽恰好放在 tau 生物学、铜化学与淀粉样病理的交点 [27]。互补的无机化学文献显示同样的 His/Cys 锚定逻辑普遍存在于 tau 片段 [27]。在人蛋白质组之外，细菌淀粉样蛋白提供了外源先例：口服功能性淀粉样蛋白 curli 可增强老年大鼠与秀丽隐杆线虫的 α-突触核蛋白聚集，证明细菌肽组装体可在体内交叉播种人淀粉样蛋白 [29]。

这些观察定义了阅读我们外源候选的模板：7–20 残基、具备 His/Cys 金属配位能力、构象动态、可实验证伪。它们也定下实验门槛：tau26–44 的毒性是湿实验陈述（NMDA 依赖、坏死、膜扰动），任何计算预测器都不能替代。

#### 1.5 小开放阅读框与蛋白质组支持筛选的必要性

肽清单本身来自 sORF 生物学。真核与微生物基因组翻译成千上万条有真实功能的微肽，其中多数对经典注释不可见 [30]；核糖体图谱与蛋白质基因组学调查不断扩展翻译景观，包括心脏等曾被认为"肽沉默"的组织 [31]。宏基因组放大了这一问题：数百个 MAG 的六框翻译产生数百万条假想的 4–50 残基序列，其中多数永远不会被质谱看到；跳过蛋白质组支持的筛选是对翻译噪声的筛选。由此得出两条研究设计推论：其一，任何生物活性预测之前，组特异 sORF 库必须先对口腔宏蛋白质组塌缩；其二，预测的生物活性是多变量的——过屏障、金属结合、氧化行为——因此 UniDL4BioPep [32] 等深度学习预测器的输出只能通过显式决策栈使用，不能靠单头阈值。

#### 1.6 本研究

本文分两个阶段。阶段一（2.2–2.9、3.1–3.6）问一个可计数的问题：牙周炎相关 sORF 库被口腔蛋白质组实际观察到的肽限制后，还有多少能通过 BBB 过滤、神经毒性过滤、Cu/Fe/Zn 过滤与"螯合高/清除低"规则？答案是 12 条（更严格清除阈值下 8 条）。阶段二（2.10–2.11、3.7）把这十二条作者提供的序列带到结构层面：对人 AChE（PDB 4EY6 [8]）做 PAS 聚焦分子对接。选 PAS 是因为它既是 AChE 加速 Aβ 的位点 [4–6]，又紧邻已发表的 Aβ 驻留区 344–361 [9]。

三条边界先行声明。（i）该 MAG 集合是**社区性**口腔宏基因组 [33]，不是牙龈卟啉单胞菌专属肽组；不声称把十二条序列归属到单一物种。（ii）对接打分是带有已知打分函数偏倚的排序启发式；此处用于在同一结合位点上比较十二条候选，而非预测解离常数。（iii）分子动力学、QM/MM 与所有湿实验均为未来工作（2.11 与 4.5 节）；终止规则不变——只有在金属存在下升高活性氧（ROS）或脂质过氧化并损伤神经元的肽，才配得上"金属相关促氧化神经毒性"这一表述。

## 2. Materials and Methods / 2 材料与方法

### English

#### 2.1 Study design and independent unit

This is a computational re-analysis of public assemblies plus a structure-based docking stage on the resulting candidates. The independent experimental unit of the screening stage is the donor: 24 healthy controls and 26 periodontitis patients [33]. Peptides are nested within donors; peptide-level contingency tests are exploratory and ignore that clustering. No new human sampling was performed. Screening methods follow the author’s mechanism draft; docking parameters follow the author’s PAS docking note.

#### 2.2 sORF libraries

Oral metagenomes were taken from BioProject PRJNA678453 [33] and the companion high-resolution assembly set PRJEB65451, comprising 296 high-quality MAGs. Sample-specific mapping produced healthy-specific and periodontitis-specific sORF libraries. Translations of 4–50 amino acids were retained. Raw library sizes were 11,269,961 (healthy) and 11,721,988 (periodontitis).

#### 2.3 Proteomic support

Candidates were matched by hash-indexed exact identity to oral metaproteome peptides. Short-branch proteomes were PXD003151, PXD004319 and PXD026727; the long branch used HOMD. After dereplication the healthy set contained 31,510 peptides (30,557 short + 953 long) and the periodontitis set 33,786 peptides (32,754 short + 1,032 long). Before group-specific collapse, 98.98% of the short-branch proteome collection sat in 5–30 aa (462,257 / 467,002); HOMD was 98.40% longer than 50 aa, with 298,454 sequences in 31–50 aa. Downstream statistics never pool the two branches.

#### 2.4 Length branches

After proteomic dereplication, 5–30 aa sequences form the short branch and 31–50 aa sequences form the long branch. Occasional boundary sequences may sit in files labelled “short”; all reported counts use the observed length bin.

#### 2.5 UniDL4BioPep scoring

Functional probabilities were computed with UniDL4BioPep, which embeds peptides with ESM-2 (`esm2_t6_8M_UR50D`) and classifies bioactivities with a convolutional head [32]. Categories included ACE inhibition, tumour T-cell antigen, BBB, antiparasitic, neurotoxicity, antibacterial, antifungal, antiviral, toxicity, antioxidant free-radical scavenging, allergenicity, DPP-IV inhibition, cell-penetrating peptide, bitter, umami, broad antimicrobial, antimalarial, quorum sensing, anticancer and anti-MRSA. For category *c*,

N_high(c) = Σ_i 1{P_i(c) ≥ 0.8}

The 0.8 cut is an operational high-confidence rule, not a calibrated posterior of wet-lab activity. Software version and random seeds were not stated in the source draft (`AUTHOR_INPUT_NEEDED`).

#### 2.6 Three-model filter

Only peptides with BBB probability ≥ 0.8 entered NTxPred2, mebipred and AnOxPePred. NTxPred2 was run on sequences ≥ 7 aa. AnOxPePred supplied a free-radical scavenging score (FRS) and a chelator score (CHEL). Mebipred scored metal-binding potential; Cu, Fe and Zn were retained. High CHEL and modest FRS defined priority for later metal-linked oxidative-stress work; the source draft states that this class is not experimental pro-oxidant activity.

#### 2.7 Structural targets and what was computed at this stage

The source draft lists AChE, butyrylcholinesterase, Aβ42, tau, ApoE4, ferritin and transferrin as structural targets, with AChE attention on the CAS, the PAS and the AChE–Aβ interface. PAS-focused docking of the twelve main candidates against human AChE (PDB 4EY6) has now been completed and is reported in Section 3.7. The remaining targets, full metal-ion coordination modelling, production molecular dynamics and QM/MM/DFT are future work (Section 4.5). GSE42872 (vemurafenib in BRAF-V600E A375 melanoma [34]) and a Chinese translation of a 1 μs AChE–Aβ trajectory [9] are archived beside this project and are not inputs to the screening tables; the GSE42872 files are documented in the excluded-source record.

#### 2.8 Exploratory statistics

Donor-level mixed models were not possible from the deposited tables. For description only, two-sided Fisher’s exact tests and χ² tests were computed on peptide 2 × 2 tables (SciPy 1.17). Odds ratios are periodontitis versus healthy unless noted. No multiple-comparison correction was applied across UniDL4BioPep heads. These *P* values do not replace a donor-level analysis.

#### 2.9 Figures

Figures were drawn in Python 3 (matplotlib) with a colour-blind-safe pair (blue `#0072B2`, vermillion `#D55E00`). Vector PDFs are the submission masters; PNGs are previews.

#### 2.10 PAS-focused molecular docking (AutoDock Vina 1.2.5)

**Receptor.** The receptor was recombinant human AChE in complex with (−)-galantamine (PDB 4EY6; 2.40 Å resolution; expressed in HEK-293 cells [8]). The co-crystallised ligand, waters and non-protein entities were removed during preparation; polar hydrogens and partial charges were assigned in the standard AutoDock preparation workflow (preparation toolchain details: `AUTHOR_INPUT_NEEDED`). 4EY6 carries chain breaks with unresolved loop segments near residues 259–262 and 492–495; these segments were not modelled at this stage and are treated as a limitation (Section 4.4).

**Ligands.** The twelve main-candidate peptides (Table 5) were built as flexible linear chains and energy-minimised before docking (`AUTHOR_INPUT_NEEDED` for the exact builder/minimiser). No metal ion was present in the docking runs; metal coordination is addressed separately in the roadmap (Section 4.5).

**Search space and search.** A cubic grid of 40 × 40 × 40 Å³ was centred on the PAS region of 4EY6, covering the PAS rim (Tyr72, Asp74, Tyr124, Trp286, Tyr341) and the entrance of the active-site gorge. Docking was performed with AutoDock Vina v1.2.5 [35,36], with peptide side-chain and backbone flexibility enabled (`AUTHOR_INPUT_NEEDED` for exhaustiveness, number of runs and seed settings). Vina scores are reported as mean ± SD in kcal/mol. Vina is a scoring-function ranking tool: its scores correlate with, but are not, experimental binding free energies, and comparisons across very different ligand chemistries are discouraged by the method itself [35]; here all twelve ligands are closely related 7–9-mers, so within-set comparison is the intended use.

**Pose analysis.** Top poses were inspected for (i) full containment within the box (no pose truncated at the box edge), (ii) contacts with PAS core residues (Tyr72, Asp74, Tyr124, Trp286, Tyr341), (iii) contacts with gorge aromatic residues (Trp86, Phe295, Tyr337, Phe338), and (iv) reach of side chains toward the catalytic region (Ser203, His447). Interaction tallies are qualitative at this stage; per-peptide interaction tables will accompany the MD stage. Rosetta FlexPepDocking [37] is the literature-preferred protocol for peptide–protein docking and is listed as the upgrade path (Section 4.5); at the current stage its C++ command-line parameter system and large-scale flexible sampling are still being mastered, so the validated Vina pipeline was used for the reported runs.

#### 2.11 Attempted molecular dynamics (reported, not included)

Following the 100-ns simulation protocol established for the AChE–Aβ system [9], we attempted all-atom MD of the best-docked peptide–AChE complex using GROMACS 2025 [38] with the AMBER99SB-ILDN force field [39], the TIP3P water model [40] and a triclinic periodic box. During the NPT pressure-equilibration stage (Berendsen barostat [41]), the system developed severe anisotropic pressure oscillations along the Z axis and ultimately failed (box blow-up). Two proximate causes were identified: (i) the local chain breaks of 4EY6 (unresolved segments near residues 259–262 and 492–495) create internal strain once solvent pressure is applied; (ii) rigid insertion of the docked peptide leaves residual interfacial stress. Remediation in progress includes Z-axis pressure-coupling parameters (compressibility, τ_p) and relaxation schedules, ACE/NME capping of the broken loop segments, and side-chain debumping of the peptide–protein interface. No production trajectory is therefore included in this version; the 100-ns analysis remains a deliverable of the next stage.

### 中文

#### 2.1 研究设计与独立单位

本研究是对公开组装数据的计算再分析，外加对所得候选的结构层面对接阶段。筛选阶段的独立实验单位是供体：24 名健康对照与 26 名牙周炎患者 [33]。肽嵌套于供体之内；肽水平列联检验为探索性，忽略该聚类。未进行新的人体采样。筛选方法遵循作者的机制研究稿；对接参数遵循作者的 PAS 对接说明。

#### 2.2 sORF 库

口腔宏基因组取自 BioProject PRJNA678453 [33] 与配套高分辨率组装集 PRJEB65451，共 296 个高质量 MAG。按样本特异映射分别构建健康组与牙周炎组 sORF 库，保留翻译长度 4–50 氨基酸。原始库规模：健康 11,269,961 条，牙周炎 11,721,988 条。

#### 2.3 蛋白质组支持

候选序列以哈希索引精确匹配对口腔宏蛋白质组肽段。短肽支蛋白质组为 PXD003151、PXD004319 与 PXD026727；长肽支使用 HOMD。去重后健康组 31,510 条（短 30,557 + 长 953），牙周炎组 33,786 条（短 32,754 + 长 1,032）。组内塌缩前，短肽支蛋白质组的 98.98% 位于 5–30 aa（462,257 / 467,002）；HOMD 的 98.40% 长于 50 aa，31–50 aa 有 298,454 条。下游统计从不合并两支。

#### 2.4 长度分支

蛋白质组去重后，5–30 aa 为短肽支，31–50 aa 为长肽支。标为"短肽"的文件中可能有少量边界序列；所有计数按实际长度分箱。

#### 2.5 UniDL4BioPep 打分

功能概率用 UniDL4BioPep 计算：以 ESM-2（`esm2_t6_8M_UR50D`）嵌入肽段，卷积头做生物活性二分类 [32]。类别包括 ACE 抑制、肿瘤 T 细胞抗原、BBB、抗寄生虫、神经毒性、抗菌、抗真菌、抗病毒、毒性、抗氧化自由基清除、致敏性、DPP-IV 抑制、细胞穿透肽、苦味、鲜味、广谱抗微生物、抗疟、群体感应、抗癌与抗 MRSA。对类别 *c*：

N_high(c) = Σ_i 1{P_i(c) ≥ 0.8}

0.8 阈值为操作性高置信规则，不是湿实验活性的校准后验。软件版本与随机种子在源稿中未说明（`AUTHOR_INPUT_NEEDED`）。

#### 2.6 三模型过滤

仅 BBB 概率 ≥ 0.8 的肽进入 NTxPred2、mebipred 与 AnOxPePred。NTxPred2 对 ≥ 7 aa 序列运行。AnOxPePred 给出自由基清除分（FRS）与螯合分（CHEL）；mebipred 评估金属结合潜力，保留 Cu、Fe、Zn。"高 CHEL、适度 FRS"定义为后续金属相关氧化应激研究的优先级；源稿明确该类计算标签不是实验性促氧化活性。

#### 2.7 结构靶点与本阶段计算范围

源稿列出 AChE、丁酰胆碱酯酶、Aβ42、tau、ApoE4、铁蛋白与转铁蛋白为结构靶点，AChE 关注 CAS、PAS 与 AChE–Aβ 界面。十二条主候选对人 AChE（PDB 4EY6）的 PAS 聚焦对接已完成，见 3.7 节。其余靶点、完整金属离子配位建模、生产分子动力学与 QM/MM/DFT 为未来工作（4.5 节）。GSE42872（BRAF-V600E A375 黑色素瘤的维莫非尼研究 [34]）与一份 1 μs AChE–Aβ 轨迹的中文翻译 [9] 存档于本项目旁，不作为筛选表的输入；GSE42872 文件记录在排除材料记录中。

#### 2.8 探索性统计

存档表中无法拟合供体水平混合模型。仅作描述用途，对肽水平 2 × 2 表计算双侧 Fisher 精确检验与 χ² 检验（SciPy 1.17）。除注明外，比值比为牙周炎对健康。未对 UniDL4BioPep 各头做多比较校正。这些 *P* 值不能替代供体水平分析。

#### 2.9 图形

图形用 Python 3（matplotlib）绘制，采用色盲安全配色（蓝 `#0072B2`、朱红 `#D55E00`）。矢量 PDF 为投稿母版；PNG 为预览。

#### 2.10 PAS 聚焦分子对接（AutoDock Vina 1.2.5）

**受体。** 受体为与 (−)-加兰他敏复合的重组人 AChE（PDB 4EY6；分辨率 2.40 Å；HEK-293 细胞表达 [8]）。准备时移除共晶配体、水分子与非蛋白实体；按标准 AutoDock 准备流程添加极性氢并指派部分电荷（准备工具链细节：`AUTHOR_INPUT_NEEDED`）。4EY6 存在链断裂，残基 259–262 与 492–495 附近的环区未解析；本阶段未建模这些片段，作为局限处理（4.4 节）。

**配体。** 十二条主候选肽（表 5）构建为柔性线性链并在对接前能量最小化（具体构建/最小化工具：`AUTHOR_INPUT_NEEDED`）。对接运行中不含金属离子；金属配位另行列入路线图（4.5 节）。

**搜索空间与搜索。** 40 × 40 × 40 Å³ 立方网格以 4EY6 的 PAS 区为中心，覆盖 PAS 边环（Tyr72、Asp74、Tyr124、Trp286、Tyr341）与活性位点峡部入口。对接用 AutoDock Vina v1.2.5 [35,36]，开启肽侧链与主链柔性（exhaustiveness、运行次数与种子设置：`AUTHOR_INPUT_NEEDED`）。Vina 打分以 mean ± SD（kcal/mol）报告。Vina 是打分函数排序工具：其分数与实验结合自由能相关但不等同，方法本身也不鼓励跨化学差异很大的配体比较 [35]；此处十二条配体是 closely related 的 7–9 肽，集合内比较正是其预期用途。

**构象分析。** 检查最优构象的：（i）盒子内完整容纳（构象未在盒边被截断）；（ii）与 PAS 核心残基（Tyr72、Asp74、Tyr124、Trp286、Tyr341）的接触；（iii）与峡部芳香残基（Trp86、Phe295、Tyr337、Phe338）的接触；（iv）侧链对催化区（Ser203、His447）的可及性。相互作用统计本阶段为定性；逐肽相互作用表将随 MD 阶段给出。Rosetta FlexPepDocking [37] 是文献首选的肽–蛋白对接协议，列为升级路径（4.5 节）；当前阶段其 C++ 命令行参数体系与大规模柔性采样仍在学习掌握中，故已报告的运行采用经验证的 Vina 流程。

#### 2.11 已尝试的分子动力学（报告但不纳入）

按 AChE–Aβ 体系建立的 100 ns 模拟规范 [9]，我们尝试对最佳对接肽–AChE 复合物做全原子 MD：GROMACS 2025 [38]、AMBER99SB-ILDN 力场 [39]、TIP3P 水模型 [40]、三斜周期盒子。NPT 压力平衡阶段（Berendsen 压浴 [41]）出现剧烈 Z 轴各向异性压力震荡并最终失败（爆框）。两个近因：（i）4EY6 的局部链断裂（残基 259–262 与 492–495 附近未解析片段）在溶剂压力施加后产生内应力；（ii）对接肽的刚性插入留下残余界面应力。正在推进的修复包括：Z 轴压力耦合参数（压缩率、τ_p）与松弛梯度、断裂环段的 ACE/NME 封端、肽–蛋白界面的侧链去碰撞（debumping）。因此本版本不含生产轨迹；100 ns 分析仍是下一阶段交付物。

## 3. Results / 3 结果

### English

#### 3.1 Proteomes discard more than 99.7% of translated sORFs

Raw sORF libraries contained 11,269,961 healthy and 11,721,988 periodontitis sequences. Exact proteomic support left 31,510 and 33,786 unique peptides (Table 1). Passage rates were 0.2796% and 0.2882%. Periodontitis contributed 51.75% of the combined confirmed library (65,296 peptides).

**Table 1.** Proteomic support of group-specific sORFs.

| Group | Specific sORFs | Unique supported peptides | Passage (%) | Share of confirmed library (%) |
| --- | ---: | ---: | ---: | ---: |
| Healthy | 11,269,961 | 31,510 | 0.2796 | 48.25 |
| Periodontitis | 11,721,988 | 33,786 | 0.2882 | 51.75 |
| Total | 22,991,949 | 65,296 | 0.2839 | 100.00 |

A peptide-level χ² test on passage is statistically significant because the denominators are huge (χ² = 15.1, *P* = 1.0 × 10⁻⁴). The absolute difference is 0.0086 percentage points; we do not interpret that *P* value as a biological effect. The confirmed sets are the only denominators used below.

#### 3.2 BBB calls: counts rise in periodontitis; only the long branch changes in rate

At BBB probability ≥ 0.8 the short branch yielded 3,359 healthy and 3,446 periodontitis peptides (10.99% vs 10.52% of each proteome-supported short set). The long branch yielded 40 and 72 (4.20% vs 6.98%). An exploratory Fisher test on the long-branch 2 × 2 table gives OR = 1.71 for periodontitis versus healthy (*P* = 0.0084); the corresponding short-branch test is not significant (OR = 0.95, *P* = 0.056). Absolute periodontitis excess, plus the long-branch rate, is what feeds the AD-oriented funnel. Short-branch BBB **percentages** do not support a “more BBB-positive periodontitis peptidome” slogan.

#### 3.3 Long peptides: barrier and antibacterial heads move together

Backgrounds are 953 healthy and 1,032 periodontitis long peptides. Table 2 reports every UniDL4BioPep head at *P* ≥ 0.8 (full version in Supplementary Table S1). Periodontitis is higher for BBB, antibacterial, anti-MRSA, cell-penetrating and antifungal calls (Fig. 2a). An exploratory Fisher test on long-branch antibacterial calls gives OR = 1.32 (*P* = 0.040). Bitter is the most frequent call in both groups (66.63% and 62.11%) and is not treated as an AD phenotype.

**Table 2.** Selected long-peptide high-confidence UniDL4BioPep counts (background 953 / 1,032).

| Model | Healthy n (%) | Periodontitis n (%) |
| --- | ---: | ---: |
| BBB_Peptides | 40 (4.20) | 72 (6.98) |
| Antimicrobial | 206 (21.62) | 238 (23.06) |
| Antibacterial | 111 (11.65) | 153 (14.83) |
| Anti-MRSA | 47 (4.93) | 62 (6.01) |
| CPP | 15 (1.57) | 29 (2.81) |
| Antifungal | 73 (7.66) | 96 (9.30) |
| NeuroPred | 82 (8.60) | 77 (7.46) |
| Antioxidant_FRS | 43 (4.51) | 41 (3.97) |
| Bitter | 635 (66.63) | 641 (62.11) |

#### 3.4 Short peptides: counts track library size; one head saturates

Backgrounds are 30,557 healthy and 32,754 periodontitis short peptides (full head-by-head counts in Supplementary Table S2). The source draft highlights periodontitis **counts** for BBB (3,446), NeuroPred (4,019), Anti-MRSA (4,728) and quorum sensing (12,674) (Fig. 2b). Percentages in those four rows are similar across groups (Table 3). Exploratory Fisher tests on NeuroPred, Anti-MRSA and quorum sensing are all *P* > 0.11. Broad `Antimicrobial_activity` is called on 99.93% and 99.90% of the two short sets—a property of that classifier head, not a census of oral antibiotics.

**Table 3.** Selected short-peptide high-confidence UniDL4BioPep counts (background 30,557 / 32,754).

| Model | Healthy n (%) | Periodontitis n (%) |
| --- | ---: | ---: |
| BBB_Peptides | 3,359 (10.99) | 3,446 (10.52) |
| NeuroPred | 3,876 (12.68) | 4,019 (12.27) |
| Anti-MRSA | 4,315 (14.12) | 4,728 (14.43) |
| Quorum_sensing | 11,834 (38.73) | 12,674 (38.69) |
| Antioxidant_FRS | 4,171 (13.65) | 4,093 (12.50) |
| CPP | 4,435 (14.51) | 4,133 (12.62) |
| Antimicrobial_activity | 30,537 (99.93) | 32,721 (99.90) |

#### 3.5 The BBB set is mostly 8–15 aa

Restricting the periodontitis-oriented joint library to BBB ≥ 0.8 gave 3,518 peptides: 3,446 short and 72 long. Of the short BBB set, 2,893 (83.95%) were 8–15 aa, 547 were 5–7 aa and 6 were 16–30 aa (Fig. 4). All 72 long peptides sit in 31–50 aa. An AD-oriented wet list is therefore dominated by 8–15-mer chemistry; the twelve docking candidates (7–9 aa) sit squarely inside that mode.

#### 3.6 Three models collapse 3,518 peptides to 12 (8)—and the sequences are now known

The 3,518 BBB peptides entered NTxPred2, mebipred and AnOxPePred (Table 4; Fig. 3). NTxPred2 does not accept sequences shorter than 7 aa, so 219 peptides were skipped and 3,299 were scored; 923 were called neurotoxic, all ≤ 30 aa. Mebipred at 0.5 marked 111 Cu/Fe/Zn-positive peptides, which were submitted to AnOxPePred. Three batches of `Chelator_All.txt` and `Scavenger_All.txt` were merged on SeqID. CHEL ≥ 0.25 selected 15 peptides; adding FRS < 0.50 left **12 main candidates**; tightening to FRS < 0.45 left **8 high-confidence peptides**.

The author supplied the twelve sequences (Table 5, column 2). They are 7–9 residues long, leucine-rich (every sequence carries ≥ 2 leucines), predominantly basic (all 12 carry ≥ 1 Arg/Lys; none carries Asp/Glu), with His in 11 of 12 and Cys in 6 of 12. That composition is exactly the His/Cys anchoring chemistry of the metal-binding filter that selected them, and it parallels the His-dependent Cu(II) coordination of the tau26–44 template [27].

**Table 4.** Three-model funnel.

| Stage | Rule | n |
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

Membership of the 8-peptide high-confidence subset among the twelve sequences: `AUTHOR_INPUT_NEEDED` (the stricter FRS cut was applied upstream; the subset labels were not deposited with the sequences).

#### 3.7 PAS-focused docking: all twelve candidates occupy the PAS–gorge interface of human AChE

The twelve main candidates were docked into a 40 × 40 × 40 Å³ box centred on the PAS of 4EY6 [8] using AutoDock Vina 1.2.5. Every peptide’s top pose was fully contained within the box—no pose was truncated at a box edge—so the PAS-focused search space was large enough for these 7–9-mers. Vina scores spanned −8.25 to −9.60 kcal/mol with tight run-to-run dispersion (SD 0.04–0.12), indicating a consistent binding solution rather than a flat energy landscape (Table 5; Fig. 5).

**Table 5.** The twelve main candidates: sequences, metal-relevant composition and PAS-focused Vina docking scores against 4EY6.

| Rank | Peptide ID | Sequence | Length (aa) | His | Cys | Arg+Lys | Aromatic (F/Y/W) | Vina score, mean ± SD (kcal/mol) |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | fllhttr | FLLHTTR | 7 | 1 | 0 | 1 | 1 (F) | **−9.60 ± 0.08** |
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

Composition columns are counted directly from the sequences. Vina scores are the author’s reported means ± SD; docking protocol, Section 2.10.

Three features of the binding solutions are reported qualitatively. First, all twelve peptides adopted a **gorge-spanning mode**: density over the PAS rim combined with extension down the aromatic gorge toward the CAS, rather than shallow surface adsorption at the rim alone. Second, poses make dense hydrogen-bond and π–π stacking networks with the PAS core residues Tyr72, Asp74, Tyr124, Trp286 and Tyr341, and with the gorge aromatics Trp86, Phe295, Tyr337 and Phe338—the same aromatic ladder that guides substrates and classical inhibitors down the gorge [7,8]. Third, in several top poses side chains reach the catalytic region around Ser203 and His447, which is why these candidates should also be scored against the CAS in the follow-up panel (Section 4.5).

Ranking is internally consistent: the three best scorers (FLLHTTR −9.60; YLSLLQR −9.49; ALLLHRC −9.29) are separated from the weakest two (HLPLLHRCC −8.35; HVLLLRQCA −8.25) by more than 1 kcal/mol, well outside the per-peptide SD, while the middle of the table is a near-degenerate cluster (−8.88 to −9.29). Two caveats travel with this ranking: Vina scores of flexible 7–9-mers are sensitive to starting conformations, and scores for a PAS-only box say nothing about CAS-only or exosite binding; both are on the follow-up list.

### 中文

#### 3.1 蛋白质组丢弃了 99.7% 以上的翻译 sORF

原始 sORF 库含健康 11,269,961 条与牙周炎 11,721,988 条。精确蛋白质组支持后留下 31,510 与 33,786 条唯一肽（表 1），通过率 0.2796% 与 0.2882%。牙周炎组贡献合并确认库的 51.75%（65,296 条）。

**表 1.** 组特异 sORF 的蛋白质组支持。

| 组 | 特异 sORF | 唯一支持肽 | 通过率 (%) | 占确认库比例 (%) |
| --- | ---: | ---: | ---: | ---: |
| 健康 | 11,269,961 | 31,510 | 0.2796 | 48.25 |
| 牙周炎 | 11,721,988 | 33,786 | 0.2882 | 51.75 |
| 合计 | 22,991,949 | 65,296 | 0.2839 | 100.00 |

肽水平 χ² 检验因分母巨大而显著（χ² = 15.1，*P* = 1.0 × 10⁻⁴），但绝对差异仅 0.0086 个百分点；我们不把该 *P* 值解读为生物学效应。下文只使用确认集作为分母。

#### 3.2 BBB 判读：牙周炎计数上升；只有长肽支速率改变

BBB 概率 ≥ 0.8 时，短肽支为健康 3,359 条、牙周炎 3,446 条（各占蛋白质组支持短肽集的 10.99% 与 10.52%）；长肽支为 40 与 72（4.20% 与 6.98%）。长肽支 2 × 2 表的探索性 Fisher 检验给出牙周炎对健康 OR = 1.71（*P* = 0.0084）；短肽支对应检验不显著（OR = 0.95，*P* = 0.056）。喂养 AD 导向漏斗的是牙周炎的绝对超额与长肽支速率。短肽支 BBB **百分比**不支持"牙周炎肽组更 BBB 阳性"这种口号。

#### 3.3 长肽：屏障与抗菌头同步移动

背景为健康 953 条、牙周炎 1,032 条长肽。表 2 报告 *P* ≥ 0.8 的部分 UniDL4BioPep 头（全表见补充表 S1）。牙周炎组 BBB、抗菌、抗 MRSA、细胞穿透与抗真菌判读更高（图 2a）。长肽支抗菌判读的探索性 Fisher 检验给出 OR = 1.32（*P* = 0.040）。苦味在两组都是最高频判读（66.63% 与 62.11%），不作为 AD 表型处理。

**表 2.** 长肽高置信 UniDL4BioPep 计数选摘（背景 953 / 1,032）。

| 模型 | 健康 n (%) | 牙周炎 n (%) |
| --- | ---: | ---: |
| BBB_Peptides | 40 (4.20) | 72 (6.98) |
| Antimicrobial | 206 (21.62) | 238 (23.06) |
| Antibacterial | 111 (11.65) | 153 (14.83) |
| Anti-MRSA | 47 (4.93) | 62 (6.01) |
| CPP | 15 (1.57) | 29 (2.81) |
| Antifungal | 73 (7.66) | 96 (9.30) |
| NeuroPred | 82 (8.60) | 77 (7.46) |
| Antioxidant_FRS | 43 (4.51) | 41 (3.97) |
| Bitter | 635 (66.63) | 641 (62.11) |

#### 3.4 短肽：计数随库规模移动；一个头饱和

背景为健康 30,557 条、牙周炎 32,754 条短肽（逐头计数全表见补充表 S2）。源稿强调牙周炎的 **计数**：BBB（3,446）、NeuroPred（4,019）、抗 MRSA（4,728）与群体感应（12,674）（图 2b）。这四行的百分比在两组相近（表 3）。NeuroPred、抗 MRSA 与群体感应的探索性 Fisher 检验均 *P* > 0.11。广谱 `Antimicrobial_activity` 在两个短肽集上分别判给 99.93% 与 99.90%——这是该分类头的性质，不是口腔抗生素普查。

**表 3.** 短肽高置信 UniDL4BioPep 计数选摘（背景 30,557 / 32,754）。

| 模型 | 健康 n (%) | 牙周炎 n (%) |
| --- | ---: | ---: |
| BBB_Peptides | 3,359 (10.99) | 3,446 (10.52) |
| NeuroPred | 3,876 (12.68) | 4,019 (12.27) |
| Anti-MRSA | 4,315 (14.12) | 4,728 (14.43) |
| Quorum_sensing | 11,834 (38.73) | 12,674 (38.69) |
| Antioxidant_FRS | 4,171 (13.65) | 4,093 (12.50) |
| CPP | 4,435 (14.51) | 4,133 (12.62) |
| Antimicrobial_activity | 30,537 (99.93) | 32,721 (99.90) |

#### 3.5 BBB 集以 8–15 aa 为主

把牙周炎导向合并库限制到 BBB ≥ 0.8，得 3,518 条：短肽 3,446、长肽 72。短肽 BBB 集中 2,893 条（83.95%）为 8–15 aa，547 条为 5–7 aa，6 条为 16–30 aa（图 4）。全部 72 条长肽位于 31–50 aa。AD 导向的湿实验名单因此以 8–15 肽化学为主；十二条对接候选（7–9 aa）恰好落在该主峰内。

#### 3.6 三个模型把 3,518 条塌缩到 12 条（8 条）——序列现已公开

3,518 条 BBB 肽进入 NTxPred2、mebipred 与 AnOxPePred（表 4；图 3）。NTxPred2 不接收短于 7 aa 的序列，故 219 条被跳过、3,299 条被打分；923 条判为神经毒性，全部 ≤ 30 aa。mebipred 阈值 0.5 标出 111 条 Cu/Fe/Zn 阳性肽并送入 AnOxPePred。三批 `Chelator_All.txt` 与 `Scavenger_All.txt` 按 SeqID 合并。CHEL ≥ 0.25 选出 15 条；加 FRS < 0.50 留下 **主候选 12 条**；收紧到 FRS < 0.45 留下 **高置信 8 条**。

作者提供了十二条序列（表 5 第 2 列）。它们为 7–9 残基、富亮氨酸（每条 ≥ 2 个亮氨酸）、以碱性为主（12 条均含 ≥ 1 个 Arg/Lys；无一含 Asp/Glu），11/12 含 His、6/12 含 Cys。该组成正是选出它们的金属结合过滤器的 His/Cys 锚定化学，并与 tau26–44 模板的 His 依赖 Cu(II) 配位平行 [27]。

**表 4.** 三模型漏斗。

| 阶段 | 规则 | n |
| --- | --- | ---: |
| BBB 短肽 | BBB ≥ 0.8，5–30 aa | 3,446 |
| BBB 长肽 | BBB ≥ 0.8，31–50 aa | 72 |
| BBB 合计 | BBB ≥ 0.8 | 3,518 |
| NTxPred2 输出 | 被打分序列 | 3,299 |
| 神经毒性 | NTxPred2 = 神经毒性（全部 ≤ 30 aa） | 923 |
| Cu/Fe/Zn 结合 | mebipred 0.5 | 111 |
| CHEL ≥ 0.25 | AnOxPePred | 15 |
| 主集 | CHEL ≥ 0.25 且 FRS < 0.50 | **12** |
| 高置信子集 | CHEL ≥ 0.25 且 FRS < 0.45 | **8** |

八条高置信子集在十二条序列中的归属：`AUTHOR_INPUT_NEEDED`（更严格 FRS 阈值在上游应用；子集标签未随序列存档）。

#### 3.7 PAS 聚焦对接：十二条候选全部占据人 AChE 的 PAS–峡部界面

十二条主候选以 AutoDock Vina 1.2.5 对接到以 4EY6 [8] PAS 为中心的 40 × 40 × 40 Å³ 盒子。每条肽的最优构象都完整位于盒内——没有构象在盒边被截断——说明 PAS 聚焦搜索空间对这些 7–9 肽足够大。Vina 打分跨度 −8.25 至 −9.60 kcal/mol，运行间离散很小（SD 0.04–0.12），提示一致的结合解而非平坦能量面（表 5；图 5）。

**表 5.** 十二条主候选：序列、金属相关组成与对 4EY6 的 PAS 聚焦 Vina 对接打分。

| 排名 | 肽 ID | 序列 | 长度 (aa) | His | Cys | Arg+Lys | 芳香 (F/Y/W) | Vina 打分 mean ± SD (kcal/mol) |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | fllhttr | FLLHTTR | 7 | 1 | 0 | 1 | 1 (F) | **−9.60 ± 0.08** |
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

组成列直接由序列计数。Vina 打分为作者报告的 mean ± SD；对接方案见 2.10 节。

结合解有三个定性特征。第一，十二条肽均采取**跨峡部模式**：密度覆盖 PAS 边环并沿芳香峡部向 CAS 延伸，而非仅在边环做浅表吸附。第二，构象与 PAS 核心残基 Tyr72、Asp74、Tyr124、Trp286、Tyr341 及峡部芳香残基 Trp86、Phe295、Tyr337、Phe338 形成密集氢键与 π–π 堆积网络——这正是引导底物与经典抑制剂下行峡部的同一芳香阶梯 [7,8]。第三，若干最优构象的侧链可及 Ser203 与 His447 附近的催化区，因此后续面板也应把 CAS 纳入打分（4.5 节）。

排序内部一致：三个最高分（FLLHTTR −9.60；YLSLLQR −9.49；ALLLHRC −9.29）与两个最低分（HLPLLHRCC −8.35；HVLLLRQCA −8.25）相差超过 1 kcal/mol，远超逐肽 SD；中段为近简并簇（−8.88 至 −9.29）。两点注意随排序同行：柔性 7–9 肽的 Vina 分数对起始构象敏感；PAS 单盒分数不能说明 CAS 单盒或外位点结合——两者都在后续清单上。

## 4. Discussion / 4 讨论

### English

#### 4.1 The funnel is a triage result, and its grain size is now right for docking

The operational product of the screening stage is a prioritisation result: oral proteomes discard more than 99.7% of translated sORFs, and a BBB-first, metal-second, scavenger-low stack reduces 33,786 periodontitis-supported peptides to 12 (8 at the stricter cut). What the structure stage adds is the readout that makes the list actionable: every one of the twelve candidates can physically occupy the PAS–gorge interface of human AChE with plausible chemistry and Vina scores below −8 kcal/mol. A twelve-peptide list with poses is a project; a twelve-peptide list without poses was an inventory.

#### 4.2 What PAS docking adds—and what it does not

The PAS was chosen as the docking target for two documented reasons: it is the AChE surface that accelerates Aβ fibril assembly [4–6], and it borders the 344–361 Aβ residence patch identified by a microsecond simulation [9]. The docking result therefore positions the oral candidates on the exact surface where AChE–Aβ cross-talk is believed to begin. The cationic, aromatic, His-rich composition of the twelve peptides fits that surface: the PAS is an anionic, aromatic rim, and every candidate carries at least one Arg/Lys while eleven of twelve carry His, a residue that can simultaneously participate in PAS stacking networks and in later Cu/Fe/Zn coordination [27]. That dual use of His—surface anchoring and metal anchoring—is precisely the chemistry the CHEL-high / FRS-low filter was designed to enrich, and the docking stage shows it is spatially compatible with a disease-relevant AChE site.

None of this is a binding constant. Vina’s scoring function is a fast approximation calibrated for enrichment, not affinity [35]; a single rigid receptor conformation was used; 4EY6’s missing loops (near residues 259–262 and 492–495) and its glycosylation state are not represented in the docking; no explicit water or metal ion was present; peptide protonation states were not sampled. The MD attempt (Section 2.11) exists precisely because we do not treat −9.60 kcal/mol as a measured free energy—it failed at pressure equilibration for the structural reasons above, and no trajectory is reported. Readers should carry one sentence forward: **the docking orders twelve candidates; it does not certify any of them.**

#### 4.3 Reading the candidates against the exogenous-peptide neurotoxicity template

The closest structural precedent for a short, metal-binding, neuroactive peptide is tau26–44: 19 residues, intrinsically disordered, toxic through NMDA-receptor-mediated necrotic-type pathways, and Cu(II)-binding via histidine with measurable effects on copper-induced Aβ aggregation [27,28]. Our candidates are shorter (7–9 aa) and exogenous to the human proteome, with two consequences. In their favour, size places them in the window where predicted BBB passage is most credible (the BBB-positive short set is 83.95% 8–15 aa; Fig. 4), and His/Cys density gives them the same metal-anchoring handles that make tau26–44 copper-active. Against them, nothing is known: no NMDA dependence, no membrane perturbation, no aggregation cross-seeding has been tested, and the bacterial-amyloid precedent (curli feeding α-synuclein aggregation after oral exposure [29]) is a different protein system entirely. The honest statement is that the twelve peptides are *formatted like* known short neuroactive peptides, not that they behave like them.

#### 4.4 Limitations

Screening limitations are those of a single 24-versus-26 donor collection, exact-match proteomics, black-box predictors at fixed cut-offs, and peptide-level *P* values that ignore donor clustering. Structure-stage limitations add: a single receptor conformation without the unresolved loop segments of 4EY6; no glycans, no crystallographic waters, no metal ion in the box; Vina scoring without re-scoring by MM/GBSA (deferred); starting-conformation sensitivity of flexible peptides; and taxonomy—the MAG collection is a community oral metagenome [33], so calling the twelve sequences “*P. gingivalis* peptides” remains a taxonomy error until each sequence is assigned. Software versions/seeds for UniDL4BioPep, NTxPred2, mebipred, AnOxPePred, and the docking exhaustiveness/seed settings, are marked `AUTHOR_INPUT_NEEDED` for the submission version. GSE42872 is a six-sample melanoma microarray [34] and must not enter an AD contrast.

#### 4.5 Roadmap for the mechanism stage

The author’s forward protocol is adopted as the continuation plan, condensed here. **(i) Peptide structures.** Multi-conformer modelling of the 7–9-mers rather than single static structures; AlphaFold3 [42] for peptide–protein and peptide–metal complex modelling, used as a reference framework to be validated by conformational sampling, confidence metrics and MD—not as a substitute for experimental structures. **(ii) Target panel.** Beyond PAS: AChE CAS and the 344–361 Aβ-residence patch, then BChE, Aβ42, tau, ApoE4, ferritin and transferrin—Aβ/tau targets test effects on pathological aggregation or conformational stability; ferritin/transferrin test crosstalk with iron-homeostasis machinery. **(iii) Metals.** Cu²⁺, Fe²⁺/Fe³⁺ and Zn²⁺: docking and structural modelling to screen coordination geometries; MD for metal–ligand distances, coordination number and stability; MM/GBSA or MM/PBSA for relative binding free energies [43]; QM/MM or DFT only on stable coordination shells, for geometry, coordination energy, charge distribution and possible electron-transfer character. **(iv) Docking upgrade.** Rosetta FlexPepDocking [37] once its parameter system and flexible sampling are fully operational; the present Vina stage is the validated interim. **(v) MD.** The 100-ns AChE–Aβ protocol [9] in GROMACS [38], after fixing the Z-axis pressure instability via compressibility/τ_p relaxation schedules, ACE/NME capping of the broken loop segments, and peptide debumping. **(vi) Wet validation cascade.** Metal binding (ITC/spectroscopy), Cu/Fe-dependent ROS, lipid peroxidation, AChE/BChE activity, Aβ aggregation and neuronal viability—under the stopping rule that only metal-conditioned ROS/lipid-peroxidation increases accompanied by neuronal injury support the phrase “metal-linked pro-oxidant neurotoxicity.”

### 中文

#### 4.1 漏斗是分诊结果，其粒度现在适合对接

筛选阶段的操作性产物是优先级排序：口腔蛋白质组丢弃 99.7% 以上的翻译 sORF，"BBB 优先、金属其次、清除低"的决策栈把 33,786 条牙周炎支持肽塌缩到 12 条（严格阈值下 8 条）。结构阶段补充的是让名单可执行的读数：十二条候选都能以合理化学占据人 AChE 的 PAS–峡部界面，Vina 打分均低于 −8 kcal/mol。带构象的十二肽名单是一个课题；不带构象的十二肽名单只是一张清单。

#### 4.2 PAS 对接补充了什么——以及没有补充什么

选 PAS 作对接靶点有两个已记录的理由：它是 AChE 上加速 Aβ 纤毛组装的表面 [4–6]，又紧邻微秒级模拟识别出的 344–361 Aβ 驻留区 [9]。对接结果因此把口腔候选定位在 AChE–Aβ 交互被认为起始的同一表面。十二条肽的阳离子、芳香、富 His 组成与该表面匹配：PAS 是阴离子芳香边环，每条候选至少带一个 Arg/Lys，11/12 带 His——His 既能参与 PAS 堆积网络，又能参与后续 Cu/Fe/Zn 配位 [27]。His 的这种双重用途——表面锚定与金属锚定——正是 CHEL 高/FRS 低过滤器被设计来富集的化学；对接阶段显示它与疾病相关 AChE 位点在空间上相容。

这些都不是结合常数。Vina 打分函数是为富集而非亲和力校准的快速近似 [35]；使用单一刚性受体构象；4EY6 的缺失环（残基 259–262 与 492–495 附近）与糖基化状态未在对接近中表现；盒内无显式水与金属离子；未采样肽的质子化状态。MD 尝试（2.11 节）的存在恰因我们不把 −9.60 kcal/mol 当作测得的自由能——它因上述结构原因在压力平衡时失败，故无轨迹可报。读者只需记住一句：**对接给十二条候选排序；它没有认证任何一条。**

#### 4.3 把候选放进外源肽神经毒性模板里读

最接近"短、金属结合、神经活性肽"的结构先例是 tau26–44：19 残基、本质无序、经 NMDA 受体介导的坏死型通路产生毒性、经组氨酸结合 Cu(II) 并对铜诱导的 Aβ 聚集产生可测影响 [27,28]。我们的候选更短（7–9 aa）且在人蛋白质组之外，由此带来两个后果。有利的一面：尺寸落在预测 BBB 通过最可信的窗口（BBB 阳性短肽集 83.95% 为 8–15 aa；图 4），His/Cys 密度赋予它们与 tau26–44 相同的金属锚定把手。不利的一面：一切未知——没有检验过 NMDA 依赖、膜扰动或聚集交叉播种；细菌淀粉样蛋白先例（口服 curli 喂养 α-突触核蛋白聚集 [29]）是另一套蛋白系统。诚实的表述是：十二条肽在**格式上像**已知的短神经活性肽，而不是在**行为上像**。

#### 4.4 局限

筛选阶段的局限：单一 24 对 26 供体集合、精确匹配蛋白质组、固定阈值下的黑箱预测器、忽略供体聚类的肽水平 *P* 值。结构阶段追加：单一受体构象且不含 4EY6 未解析环段；无糖链、无晶体水、盒内无金属离子；Vina 打分未经 MM/GBSA 复打分（推迟）；柔性肽的起始构象敏感性；分类学——MAG 集合是社区性口腔宏基因组 [33]，在每条序列被归属之前，称十二条序列为"牙龈卟啉单胞菌肽"仍是分类学错误。UniDL4BioPep、NTxPred2、mebipred、AnOxPePred 的软件版本/种子与对接 exhaustiveness/种子设置在投稿版中标记为 `AUTHOR_INPUT_NEEDED`。GSE42872 是六样本黑色素瘤芯片 [34]，不得进入 AD 对比。

#### 4.5 机制阶段路线图

采纳作者的前进方案，压缩如下。**（i）肽结构。** 对 7–9 肽做多构象建模而非单一静态结构；用 AlphaFold3 [42] 做肽–蛋白与肽–金属复合物建模，作为参考框架，经构象采样、置信指标与 MD 验证——不能替代实验结构。**（ii）靶点面板。** PAS 之外：AChE CAS 与 344–361 Aβ 驻留区，再及 BChE、Aβ42、tau、ApoE4、铁蛋白与转铁蛋白——Aβ/tau 靶点检验对病理性聚集或构象稳定性的影响；铁蛋白/转铁蛋白检验与铁稳态机制的交互。**（iii）金属。** Cu²⁺、Fe²⁺/Fe³⁺、Zn²⁺：对接与结构建模筛查配位构象；MD 分析金属–配体距离、配位数与稳定性；MM/GBSA 或 MM/PBSA 做相对结合自由能比较 [43]；仅对稳定配位壳层做 QM/MM 或 DFT，分析几何、配位能、电荷分布与可能的电子转移特征。**（iv）对接升级。** 待参数体系与柔性采样完全掌握后改用 Rosetta FlexPepDocking [37]；本阶段 Vina 为经验证的过渡。**（v）MD。** 在修复 Z 轴压力不稳定（压缩率/τ_p 松弛梯度、断裂环段 ACE/NME 封端、肽去碰撞）后，按 100 ns AChE–Aβ 方案 [9] 于 GROMACS [38] 执行。**（vi）湿实验验证级联。** 金属结合（ITC/光谱）、Cu/Fe 依赖 ROS、脂质过氧化、AChE/BChE 活性、Aβ 聚集与神经元活力——终止规则：只有金属条件下 ROS/脂质过氧化升高并伴随神经元损伤，才支持"金属相关促氧化神经毒性"的表述。

## 5. Conclusions / 5 结论

### English

A periodontitis-associated, proteome-supported sORF screen, filtered for predicted BBB passage, Cu/Fe/Zn binding and a chelator-high / scavenger-low profile, yields twelve 7–9-residue candidates whose sequences are public in this manuscript. PAS-focused docking against human AChE (4EY6) shows that all twelve physically occupy the PAS–gorge interface with −8.25 to −9.60 kcal/mol Vina scores and residue contacts overlapping the Aβ-accelerating surface of the enzyme. The result is a ranked, structurally plausible shortlist for the metal hypothesis of the periodontitis–AD link—nothing more. The upgrade path is equally clear: multi-conformer peptide models, a full target panel, explicit metal coordination, production MD after the current pressure-stability fixes, and the wet-assay cascade with its stopping rule. When those assays speak, this paper’s twelve names will either become twelve hypotheses or be retired as twelve well-formatted negatives. Either outcome is progress over an uncounted peptidome.

### 中文

一次牙周炎相关、蛋白质组支持的 sORF 筛选，经预测 BBB 通过、Cu/Fe/Zn 结合与"螯合高/清除低"过滤，产出十二条 7–9 残基候选，其序列已随本稿公开。对人 AChE（4EY6）的 PAS 聚焦对接显示：十二条全部物理占据 PAS–峡部界面，Vina 打分 −8.25 至 −9.60 kcal/mol，残基接触与酶的 Aβ 加速表面重叠。该结果是一个有排序、结构上合理的候选名单，服务于牙周炎–AD 关联的金属假说——仅此而已。升级路径同样清楚：多构象肽模型、完整靶点面板、显式金属配位、压力稳定性修复后的生产 MD，以及带终止规则的湿实验级联。当这些实验开口说话时，这十二个名字要么成为十二个假说，要么作为十二个体面的阴性退役。无论哪种，都好过一份未被清点的肽组。

## Declarations / 声明

### English

**Data availability.** PRJNA678453, PRJEB65451, PXD003151, PXD004319, PXD026727 and HOMD are public; PDB 4EY6 is public [8]. The twelve candidate sequences are in Table 5. Author screening tables are in the project’s `source-docs/` folder.

**Code availability.** Figure and audit scripts are in the project’s `scripts/` folder. UniDL4BioPep is described by Du et al. [32]; AutoDock Vina by Trott & Olson [35] and Eberhardt et al. [36].

**Ethics.** No new human or animal work was performed; the re-analysis uses public, de-identified assemblies.

**Competing interests.** None recorded (`AUTHOR_INPUT_NEEDED`).

**Funding.** None recorded (`AUTHOR_INPUT_NEEDED`).

**Author contributions.** `AUTHOR_INPUT_NEEDED` (CRediT).

**AI use.** An AI assistant assembled this manuscript from the author’s methods/results drafts under a documented skill-routed workflow, and verified the new citations against PubMed/PDB records (see the project’s provenance log). The authors remain responsible for every number and claim.

**Statistical analysis.** Independent experimental units were donors (healthy n = 24; periodontitis n = 26). Peptide counts are nested observations. Descriptive statistics are counts and percentages of proteome-supported peptides within length branch. Exploratory two-sided Fisher’s exact tests on peptide 2 × 2 tables used SciPy 1.17; no multiplicity correction was applied across UniDL4BioPep categories. Donor-level mixed models were not fitted because a donor-by-peptide matrix was not deposited. Docking scores (Table 5) are reported as mean ± SD; no inferential statistics were applied to a within-set ranking. Software versions for UniDL4BioPep, NTxPred2, mebipred, AnOxPePred and docking search parameters were not stated in the source drafts.

### 中文

**数据可用性。** PRJNA678453、PRJEB65451、PXD003151、PXD004319、PXD026727 与 HOMD 为公开数据；PDB 4EY6 公开 [8]。十二条候选序列见表 5。作者筛选表存于项目 `source-docs/` 目录。

**代码可用性。** 图形与审计脚本存于项目 `scripts/` 目录。UniDL4BioPep 见 Du 等 [32]；AutoDock Vina 见 Trott 与 Olson [35] 及 Eberhardt 等 [36]。

**伦理。** 未进行新的人体或动物实验；再分析使用公开、去标识化的组装数据。

**利益冲突。** 未记录（`AUTHOR_INPUT_NEEDED`）。

**经费。** 未记录（`AUTHOR_INPUT_NEEDED`）。

**作者贡献。** `AUTHOR_INPUT_NEEDED`（CRediT）。

**AI 使用。** AI 助手在文档化的技能路由工作流下，由作者的方法/结果草案组装本稿，并对新增引用逐条核验 PubMed/PDB 记录（见项目溯源日志）。作者对每个数字与论断负责。

**统计分析。** 独立实验单位为供体（健康 n = 24；牙周炎 n = 26）。肽计数为嵌套观测。描述性统计为长度支内蛋白质组支持肽的计数与百分比。肽水平 2 × 2 表的双侧 Fisher 精确检验为探索性（SciPy 1.17），未对 UniDL4BioPep 各类别做多比较校正。因未存档供体×肽矩阵，未拟合供体水平混合模型。对接打分（表 5）以 mean ± SD 报告；集合内排序未做推断统计。源稿未说明 UniDL4BioPep、NTxPred2、mebipred、AnOxPePred 的软件版本与对接搜索参数。

## References / 参考文献

1. Scheltens P, De Strooper B, Kivipelto M, Holstege H, Chételat G, Teunissen CE, et al. Alzheimer's disease. Lancet. 2021;397(10284):1577-1590. doi:10.1016/S0140-6736(20)32205-4
2. Selkoe DJ, Hardy J. The amyloid hypothesis of Alzheimer's disease at 25 years. EMBO Mol Med. 2016;8(6):595-608. doi:10.15252/emmm.201606210
3. Hampel H, Mesulam MM, Cuello AC, Farlow MR, Giacobini E, Grossberg GT, et al. The cholinergic system in the pathophysiology and treatment of Alzheimer's disease. Brain. 2018;141(7):1917-1933. doi:10.1093/brain/awy132
4. Inestrosa NC, Alvarez A, Pérez CA, Moreno RD, Vicente M, Linker C, et al. Acetylcholinesterase accelerates assembly of amyloid-β-peptides into Alzheimer's fibrils: possible role of the peripheral site of the enzyme. Neuron. 1996;16(4):881-891. doi:10.1016/s0896-6273(00)80108-7
5. De Ferrari GV, Canales MA, Shin I, Weiner LM, Silman I, Inestrosa NC. A structural motif of acetylcholinesterase that promotes amyloid β-peptide fibril formation. Biochemistry. 2001;40(35):10447-10457. doi:10.1021/bi0101392
6. Bartolini M, Bertucci C, Cavrini V, Andrisano V. β-Amyloid aggregation induced by human acetylcholinesterase: inhibition studies. Biochem Pharmacol. 2003;65(3):407-416. doi:10.1016/s0006-2952(02)01514-9
7. Kryger G, Silman I, Sussman JL. Structure of acetylcholinesterase complexed with E2020 (Aricept): implications for the design of new anti-Alzheimer drugs. Structure. 1999;7(3):297-307. doi:10.1016/s0969-2126(99)80040-9
8. Cheung J, Rudolph MJ, Burshteyn F, Cassidy MS, Gary EN, Love J, et al. Structures of human acetylcholinesterase in complex with pharmacologically important ligands. J Med Chem. 2012;55(23):10282-10286. doi:10.1021/jm300871x
9. Atanasova M, Dimitrov I, Ivanov S. Molecular dynamics simulations of acetylcholinesterase – beta-amyloid peptide complex. Cybern Inf Technol. 2020;20(6):140-154. doi:10.2478/cait-2020-0068
10. Lushchekina SV, Kots ED, Novichkova DA, Petrov KA, Masson P. Role of acetylcholinesterase in β-amyloid aggregation studied by accelerated molecular dynamics. BioNanoScience. 2017;7:396-402. doi:10.1007/s12668-016-0375-x
11. Ide M, Harris M, Stevens A, Sussams R, Hopkins V, Culliford D, et al. Periodontitis and cognitive decline in Alzheimer's disease. PLoS One. 2016;11(3):e0151081. doi:10.1371/journal.pone.0151081
12. Sparks Stein P, Desrosiers M, Donegan SJ, Yepes JF, Kryscio RJ. Tooth loss, dementia and neuropathology in the Nun study. J Am Dent Assoc. 2007;138(10):1314-1322. doi:10.14219/jada.archive.2007.0046
13. Jiang Z, Shi Y, Zhao W, Zhou L, Zhang B, Xie Y, et al. Association between chronic periodontitis and the risk of Alzheimer's disease: combination of text mining and GEO dataset. BMC Oral Health. 2021;21:466. doi:10.1186/s12903-021-01827-2
14. Dominy SS, Lynch C, Ermini F, Benedyk M, Marczyk A, Konradi A, et al. Porphyromonas gingivalis in Alzheimer's disease brains: evidence for disease causation and treatment with small-molecule inhibitors. Sci Adv. 2019;5(1):eaau3333. doi:10.1126/sciadv.aau3333
15. Poole S, Singhrao SK, Kesavalu L, Curtis MA, Crean S. Determining the presence of Porphyromonas gingivalis in Alzheimer's disease brain. J Alzheimers Dis. 2013;33(3):665-678. doi:10.3233/JAD-2012-121149
16. Ilievski V, Zuchowska PK, Green SJ, Toth PT, Ragozzino ME, Le K, et al. Chronic oral application of a periodontal pathogen results in brain inflammation, neurodegeneration and amyloid beta production in wild type mice. PLoS One. 2018;13(10):e0204941. doi:10.1371/journal.pone.0204941
17. Haditsch U, Roth T, Rodriguez L, Hancock S, Cecere T, Nguyen M, et al. Alzheimer's disease-like neurodegeneration in Porphyromonas gingivalis infected neurons with persistent expression of active gingipains. J Alzheimers Dis. 2020;75(4):1361-1376. doi:10.3233/JAD-200393
18. Ho MH, Chen CH, Goodwin JS, Wang BY, Xie H. Functional advantages of Porphyromonas gingivalis vesicles. PLoS One. 2015;10(4):e0123448. doi:10.1371/journal.pone.0123448
19. Nara PL, Sindelar D, Penn MS, Potempa J, Griffin WST. Porphyromonas gingivalis outer membrane vesicles as the major driver of and explanation for neuropathogenesis, the cholinergic hypothesis, iron dyshomeostasis, and salivary lactoferrin in Alzheimer's disease. J Alzheimers Dis. 2021;82(4):1417-1450. doi:10.3233/JAD-210448
20. Guo Y, Nguyen KA, Potempa J. Dichotomy of gingipains action as virulence factors: from cleaving substrates with the precision of a surgeon's knife to a meat chopper-like brutal degradation of proteins. Periodontol 2000. 2010;54(1):15-44. doi:10.1111/j.1600-0757.2010.00377.x
21. Ryder MI. Porphyromonas gingivalis and Alzheimer disease: recent findings and potential therapies. J Periodontol. 2020;91(Suppl 1):S45-S49. doi:10.1002/JPER.20-0104
22. Kanagasingam S, Chukkapalli SS, Welbury R, Singhrao SK. Porphyromonas gingivalis is a strong risk factor for Alzheimer's disease. J Alzheimers Dis Rep. 2020;4(1):501-511. doi:10.3233/ADR-200250
23. Frontiers in Aging Neuroscience. Different stages of Alzheimer's disease with periodontitis: clinical features and potential mechanisms involving gingipains. 2026. doi:10.3389/fnagi.2026.1737524. Confirm author line on the publisher PDF before submission.
24. Díaz-Zúñiga J, More J, Melgar-Rodríguez S, Jiménez-Unión M, Villalobos-Orchard F, Muñoz-Manríquez C, et al. Alzheimer's disease-like pathology triggered by Porphyromonas gingivalis in wild type rats is serotype dependent. Front Immunol. 2020;11:588036. doi:10.3389/fimmu.2020.588036
25. Bush AI. The metal theory of Alzheimer's disease. J Alzheimers Dis. 2013;33 Suppl 1:S277-281. doi:10.3233/JAD-2012-129011
26. Lei P, Ayton S, Bush AI. The essential elements of Alzheimer's disease. J Biol Chem. 2021;296:100105. doi:10.1074/jbc.REV120.008207
27. Di Natale G, Bellia F, Sciacca MFM, Campagna T, Pappalardo G. Tau-peptide fragments and their copper(II) complexes: effects on amyloid-β aggregation. Inorg Chim Acta. 2018;472:82-92. doi:10.1016/j.ica.2017.09.061
28. Perini G, Ciasca G, Minelli E, Papi M, Palmieri V, Maulucci G, et al. Dynamic structural determinants underlie the neurotoxicity of the N-terminal tau 26-44 peptide in Alzheimer's disease and other human tauopathies. Int J Biol Macromol. 2019;141:278-289. doi:10.1016/j.ijbiomac.2019.08.220
29. Chen SG, Stribinskis V, Rane MJ, Gozal D, Friedland RP. Exposure to the functional bacterial amyloid protein curli enhances alpha-synuclein aggregation in aged Fischer 344 rats and Caenorhabditis elegans. Sci Rep. 2016;6:34477. doi:10.1038/srep34477
30. Couso JP, Patra P. Short ORFs: finding gems in hidden places. Curr Opin Genet Dev. 2017;45:14-21. doi:10.1016/j.gde.2017.04.002
31. van Heesch S, Wit F, Botter J, Brakel J, et al. The translational landscape of the human heart. Cell. 2019;178(1):236-251.e24. doi:10.1016/j.cell.2019.05.010
32. Du Z, Ding X, Xu Y, Li Y. UniDL4BioPep: a universal deep learning architecture for binary classification in peptide bioactivity. Brief Bioinform. 2023;24(3):bbad135. doi:10.1093/bib/bbad135
33. Belstrøm D, Constancias F, Markvart M, Sikora M, Sørensen CE, Givskov M. Periodontitis associates with species-specific gene expression of the oral microbiota. npj Biofilms Microbiomes. 2021;7:76. doi:10.1038/s41522-021-00247-y
34. Parmenter TJ, Kleinschmidt M, Kinross KM, Bond ST, Li J, Kaadige MR, et al. Response of BRAF-mutant melanoma to BRAF inhibition is mediated by a network of transcriptional regulators of glycolysis. Cancer Discov. 2014;4(4):423-433. doi:10.1158/2159-8290.CD-13-0440
35. Trott O, Olson AJ. AutoDock Vina: improving the speed and accuracy of docking with a new scoring function, efficient optimization, and multithreading. J Comput Chem. 2010;31(2):455-461. doi:10.1002/jcc.21334
36. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. J Chem Inf Model. 2021;61(8):3891-3898. doi:10.1021/acs.jcim.1c00203
37. London N, Raveh B, Cohen E, Fathi G, Schueler-Furman O. Rosetta FlexPepDock web server—high resolution modeling of peptide–protein interactions. Nucleic Acids Res. 2011;39(Web Server issue):W249-W253. doi:10.1093/nar/gkr326
38. Abraham MJ, Murtola T, Schulz R, Páll S, Smith JC, Hess B, et al. GROMACS: high performance molecular simulations through multi-level parallelism from laptops to supercomputers. SoftwareX. 2015;1-2:19-25. doi:10.1016/j.softx.2015.06.001
39. Hornak V, Abel R, Okur A, Strockbine R, Roitberg A, Simmerling C. Comparison of multiple Amber force fields and development of improved protein backbone parameters. Proteins. 2006;65(3):712-725. doi:10.1002/prot.21123
40. Jorgensen WL, Chandrasekhar J, Madura JD, Impey RW, Klein ML. Comparison of simple potential functions for simulating liquid water. J Chem Phys. 1983;79(2):926-935. doi:10.1063/1.445869
41. Berendsen HJC, Postma JPM, van Gunsteren WF, DiNola A, Haak JR. Molecular dynamics with coupling to an external bath. J Chem Phys. 1984;81(8):3684-3690. doi:10.1063/1.448118
42. Abramson J, Adler J, Dunger J, Evans R, Green T, et al. Accurate structure prediction of biomolecular interactions with AlphaFold 3. Nature. 2024;630(8016):493-500. doi:10.1038/s41586-024-07487-w
43. Genheden S, Ryde U. The MM/PBSA and MM/GBSA methods to estimate ligand-binding affinities. Expert Opin Drug Discov. 2015;10(5):449-461. doi:10.1517/17460441.2015.1032936

*The reference list is shared by both language versions. / 中英文版本共用同一参考文献表。*
