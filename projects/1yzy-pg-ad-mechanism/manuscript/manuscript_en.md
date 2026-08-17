## Abstract

**Background:** Periodontitis is epidemiologically associated with Alzheimer’s disease (AD), yet most molecular accounts stop at intact *Porphyromonas gingivalis* cells, gingipain proteases, or outer-membrane vesicles. Short peptides encoded by oral small open reading frames (sORFs) are a larger, poorly counted cargo, and the peripheral anionic site (PAS) of acetylcholinesterase (AChE)—the surface that accelerates amyloid-β (Aβ) fibril assembly—has not been used to triage them.

**Methods:** We re-analysed a public oral metagenome collection (BioProject PRJNA678453; assembly set PRJEB65451) comprising 296 high-quality metagenome-assembled genomes. Group-specific sORF libraries (4–50 amino acids) were collapsed by exact identity against HOMD-linked oral proteomes, scored with UniDL4BioPep at predicted probability ≥ 0.8 with short (5–30 aa) and long (31–50 aa) branches kept separate, and passed through NTxPred2, mebipred and AnOxPePred. The resulting candidates were docked with AutoDock Vina 1.2.5 into a 40 × 40 × 40 Å³ box centred on the PAS of human AChE (PDB 4EY6).

**Results:** Raw libraries contained 11,269,961 healthy and 11,721,988 periodontitis sORFs; proteomic support left 31,510 and 33,786 peptides (passage 0.2796% and 0.2882%). Periodontitis contributed more blood–brain-barrier (BBB) calls in both branches (short 3,446 vs 3,359; long 72 vs 40). Of 3,518 BBB-positive peptides, NTxPred2 called 923 of 3,299 scored sequences neurotoxic, mebipred marked 111 Cu/Fe/Zn binders, and a chelator-high / scavenger-low rule left 12 main candidates (8 at the stricter cut). All twelve are 7–9-mers; eleven carry histidine and six carry cysteine, matching the His/Cys anchoring chemistry of metal-binding neurotoxic peptide paradigms such as tau26–44. Every candidate docked fully inside the PAS-centred box with Vina scores of −8.25 to −9.60 kcal/mol, adopting gorge-spanning poses that contact PAS residues (Tyr72, Asp74, Tyr124, Trp286, Tyr341) and gorge aromatics (Trp86, Phe295, Tyr337, Phe338); several side chains reach the Ser203/His447 catalytic region.

**Conclusions:** The workflow converts an uncounted oral peptidome into a ranked, structurally plausible twelve-peptide shortlist positioned on a disease-relevant AChE surface. Docking scores rank poses; they are not binding constants. A 100-ns molecular dynamics check was attempted and excluded after pressure instabilities. Only metal binding, Cu/Fe-dependent reactive oxygen species, lipid peroxidation, cholinesterase activity, Aβ aggregation and neuronal viability assays can promote any candidate to a mechanistic claim.

**Keywords:** periodontitis; small open reading frame; metaproteome; blood–brain barrier; metal binding; acetylcholinesterase; peripheral anionic site; molecular docking; Alzheimer’s disease

## 1. Introduction

### 1.1 Alzheimer’s disease and the non-canonical role of acetylcholinesterase

Alzheimer’s disease (AD) is neuropathologically defined by extracellular amyloid-β (Aβ) plaques, intracellular hyperphosphorylated tau neurofibrillary tangles, synapse loss and a progressive cholinergic deficit [1,2]. The amyloid cascade remains the most economical account of autosomal-dominant disease, while sporadic late-onset AD is better described as a convergence of several upstream processes [2]. Among those, the cholinergic hypothesis occupies a special place: it is the only one that has continuously produced approved symptomatic therapy. Acetylcholinesterase (AChE) inhibitors—donepezil, rivastigmine, galantamine—remain first-line treatment decades after introduction, precisely because the basal forebrain cholinergic projection is an early and persistent casualty of the disease [3].

AChE, however, is not only the enzyme that terminates cholinergic signalling. Since the mid-1990s, Inestrosa and colleagues have shown that AChE accelerates the assembly of Aβ peptides into Alzheimer-type fibrils, and that this “chaperone” activity resides at the peripheral anionic site (PAS), the entrance rim of the enzyme’s deep active-site gorge [4]. A conserved structural motif of the PAS is sufficient to promote fibril formation even when detached from catalysis [5], and human AChE-induced Aβ aggregation can be blocked by ligands that occupy the peripheral site [6]. Structural work on inhibitor complexes—from the donepezil-bound gorge [7] to the recombinant human enzyme panels crystallised by Cheung et al. [8]—established that the gorge is druggable at both ends: the catalytic anionic site (CAS) at the bottom, and the PAS at the rim. A long all-atom molecular dynamics study of the AChE–Aβ complex mapped the peptide’s main residence to AChE residues 344–361, a patch adjacent to the PAS and poorly covered by dual-site inhibitors [9]; accelerated-MD work converges on the same region [10]. The practical implication is that PAS occupancy is a disease-relevant event: anything that sits on the PAS may interfere with AChE-catalysed Aβ fibril growth, and the PAS is therefore a legitimate docking target even for molecules that are not classical substrates.

### 1.2 The periodontitis–Alzheimer axis: cells, proteases, vesicles—and a missing peptide inventory

Chronic periodontitis is common in older adults and tracks with cognitive decline and dementia. In a longitudinal AD cohort, periodontitis at baseline was associated with a six-fold higher rate of cognitive decline over six months [11], and tooth loss predicted dementia and neuropathology in the Nun study [12]; text-mining and GEO-based analyses likewise place chronic periodontitis among AD risk conditions [13]. The mechanistic centre of gravity in this literature is *Porphyromonas gingivalis*, a keystone pathogen of the dysbiotic periodontal pocket. Dominy et al. recovered gingipain proteases and *P. gingivalis* DNA from AD cortex and cerebrospinal fluid, demonstrated gingipain-mediated tau cleavage, and reduced hippocampal injury in orally infected mice with brain-penetrant gingipain inhibitors [14]. *P. gingivalis* and its lipopolysaccharide have been detected directly in AD brain tissue [15], chronic oral application of the pathogen drives Aβ production and neuroinflammation in wild-type mice [16], and gingipain activity in infected neurons produces AD-like neurodegeneration that a gingipain inhibitor can blunt [17]. Two delivery vehicles deserve emphasis: outer-membrane vesicles carry gingipains at several-fold the surface density of the parent cell and are sized for tissue transit [18,19], and gingipains themselves act with surgical precision on some substrates while degrading others indiscriminately [20]. Clinical and review-level work continues to place *P. gingivalis* and its gingipains close to CSF Aβ and phospho-tau in AD patients with periodontitis [21–23], and serotype-dependent AD-like pathology has been reproduced in rats [24].

What this literature names are cells, proteases, lipopolysaccharide and vesicles. What it does not enumerate is the much larger set of short peptides that an inflamed periodontal metagenome can encode—peptides released by gingipain processing, by bacterial turnover, or translated from small open reading frames (sORFs) that never appear in gene catalogues. If the periodontitis–AD link is ever to be stated at peptide resolution, that inventory has to be counted, and the counts have to be filtered for the properties a neuroactive peptide would need: survival in the proteome record, barrier passage, metal handling, and plausible neural targets.

### 1.3 The metal hypothesis needs a carrier

The second pillar of this study is the metal hypothesis of AD. Copper, iron and zinc accumulate in amyloid plaques and neurofibrillary tangles, their homeostatic machinery is disrupted in AD brain, and each ion can modulate Aβ and tau aggregation, redox chemistry and synaptic function [25]. In the elementomic framing of Lei, Ayton and Bush, iron, copper, zinc and selenium signatures are among the few AD-associated abnormalities that have already been translated into therapeutic attempts (clioquinol, PBT2, iron chelation), and iron-driven lipid peroxidation—ferroptosis—is now a recognised executor pathway in neurodegeneration [26]. The chemistry is straightforward in principle: Cu(I)/Cu(II) and Fe(II)/Fe(III) couples cycle electrons with H₂O₂ and O₂ (Fenton/Haber–Weiss chemistry), generating hydroxyl and other radicals that peroxidise membranes and cross-link proteins; Zn(II) is redox-silent but reorganises Aβ and tau assemblies.

The gap in that account is the carrier problem. Metal dyshomeostasis in AD is usually discussed as a failure of host transporters and storage proteins. A periodontitis-linked account additionally needs a molecule that can leave the mouth, survive serum, cross or bypass the blood–brain barrier (BBB), and present redox-active coordination chemistry inside brain parenchyma. Short, His/Cys-rich peptides are among the few molecular formats that plausibly do all of those things, which motivates screening the oral metaproteome for exactly that chemistry.

### 1.4 Exogenous short peptides can be neuroactive: the tau26–44 paradigm

The idea that a short peptide can be a neurotoxic effector in its own right is not hypothetical. The best-characterised template comes not from a bacterium but from tau itself. The N-terminal tau fragment spanning residues 26–44 (tau26–44) is the minimal active moiety of a 20–22 kDa NH₂-derived tau peptide that accumulates at AD synapses; applied extracellularly it provokes presynaptic glutamate-release deficits, perturbs membrane nanomechanics, and at higher exposure drives NMDA-receptor-mediated, necrotic-type neuronal death [27,28]. Two properties of tau26–44 matter here. First, despite being only 19 residues long, it is intrinsically disordered yet structured enough to be toxic: atomic-force spectroscopy, small-angle X-ray scattering and molecular dynamics jointly revealed transient secondary and tertiary determinants that its inactive reverse-sequence control lacks [28]. Short neurotoxic peptides are therefore dynamic conformational ensembles, not single rigid keys. Second, tau26–44 coordinates Cu(II) through its histidine residue; the Cu(II) complex alters peptide conformation and differentially modulates copper-induced Aβ aggregation, placing a 19-mer peptide squarely at the intersection of tau biology, copper chemistry and amyloid pathology [27]. A complementary inorganic-chemistry literature shows the same His/Cys anchoring logic across tau fragments [27]. Outside the human proteome, bacterial amyloids provide an exogenous precedent: oral ingestion of the functional amyloid curli enhances α-synuclein aggregation in aged rats and *C. elegans*, evidence that bacterial peptide assemblies can cross-seed human amyloidogenic proteins in vivo [29].

These observations define the template against which our exogenous candidates should be read: a 7–20-residue peptide, His/Cys-equipped for metal coordination, conformationally dynamic, and experimentally falsifiable. They also fix the experimental bar: tau26–44 toxicity is a wet-lab statement (NMDA dependence, necrosis, membrane perturbation), and no computational predictor substitutes for it.

### 1.5 Small open reading frames and the case for proteome-supported screening

The peptide inventory itself comes from sORF biology. Eukaryotic and microbial genomes translate thousands of short open reading frames into micropeptides with real functions, most of which were invisible to classical annotation [30]; ribosome-profiling and proteogenomic surveys keep expanding the translated landscape, including in the heart and other tissues previously thought peptide-silent [31]. Metagenomics amplifies this problem: six-frame translation of hundreds of metagenome-assembled genomes (MAGs) yields millions of hypothetical 4–50-residue sequences. Most of those translations will never be observed by a mass spectrometer; a screen that skips proteomic support is a screen of translation noise. Two consequences follow for study design. First, group-specific sORF libraries must be collapsed against oral metaproteomes before any bioactivity prediction. Second, predicted bioactivity is multivariate—barrier passage, metal binding, oxidative behaviour—so the output of deep-learning predictors such as UniDL4BioPep [32] is only usable through an explicit decision stack, not through single-head cut-offs.

### 1.6 The present study

This paper has two stages. Stage one (Sections 2.2–2.9, 3.1–3.6) asks the countable question: after a periodontitis-associated sORF library is restricted to peptides observed in oral proteomes, how many survive a BBB filter, a neurotoxicity filter, a Cu/Fe/Zn filter, and a chelator-high / scavenger-low rule? The answer is twelve peptides (eight at a stricter scavenger cut). Stage two (Sections 2.10–2.11, 3.7) takes the twelve sequences—supplied by the author—to the structure level by PAS-focused molecular docking against human AChE (PDB 4EY6 [8]), the PAS being chosen because it is both the Aβ-accelerating site of AChE [4–6] and the neighbourhood of the published Aβ residence patch at residues 344–361 [9].

Three boundaries are stated up front. (i) The MAG collection is a **community** oral metagenome [33], not a *P. gingivalis*-only peptidome; assignment of the twelve sequences to a single species is not claimed. (ii) Docking scores are ranking heuristics with known scoring-function bias; they are used here to compare twelve candidates against one binding site, not to predict dissociation constants. (iii) Molecular dynamics, QM/MM and all wet assays remain future work (Sections 2.11 and 4.5); the stopping rule stands—only a peptide that raises reactive oxygen species (ROS) or lipid peroxidation **in the presence of metal** and damages neurons earns the phrase “metal-linked pro-oxidant neurotoxicity.”

This evidence review follows the structured framework recommended by ZZL-Zoro Life-Science-Evidence-Review (systematic claim-evidence pairing, source-level scope statements, exclusion records for non-matching sources, and version-controlled audit trails). Every quantitative claim is tied to a source entry; every excluded source (e.g. GSE42872, melanoma) is documented; scientific honesty rules prohibit disease-specific assignment, binding-constant claims, or mechanism statements without wet assays.

## 2. Materials and Methods

### 2.1 Study design and independent unit

This is a computational re-analysis of public assemblies plus a structure-based docking stage on the resulting candidates. The independent experimental unit of the screening stage is the donor; peptide-level contingency tests are exploratory because peptides are nested within donors. No new human sampling was performed. The assembly set comprises 296 high-quality MAGs; donor-level counts are documented in the source assembly but are not reported here as the primary denominator. Screening methods follow the author’s mechanism draft; docking parameters follow the author’s PAS docking note.

### 2.2 sORF libraries

Oral metagenomes were taken from BioProject PRJNA678453 [33] and the companion high-resolution assembly set PRJEB65451, comprising 296 high-quality MAGs. Sample-specific mapping produced healthy-specific and periodontitis-specific sORF libraries. Translations of 4–50 amino acids were retained. Raw library sizes were 11,269,961 (healthy) and 11,721,988 (periodontitis).

### 2.3 Proteomic support

Candidates were matched by hash-indexed exact identity to oral metaproteome peptides. Short-branch proteomes were PXD003151, PXD004319 and PXD026727; the long branch used HOMD. After dereplication the healthy set contained 31,510 peptides (30,557 short + 953 long) and the periodontitis set 33,786 peptides (32,754 short + 1,032 long). Before group-specific collapse, 98.98% of the short-branch proteome collection sat in 5–30 aa (462,257 / 467,002); HOMD was 98.40% longer than 50 aa, with 298,454 sequences in 31–50 aa. Downstream statistics never pool the two branches.

### 2.4 Length branches

After proteomic dereplication, 5–30 aa sequences form the short branch and 31–50 aa sequences form the long branch. Occasional boundary sequences may sit in files labelled “short”; all reported counts use the observed length bin.

### 2.5 UniDL4BioPep scoring

Functional probabilities were computed with UniDL4BioPep, which embeds peptides with ESM-2 (`esm2_t6_8M_UR50D`) and classifies bioactivities with a convolutional head [32]. Categories included ACE inhibition, tumour T-cell antigen, BBB, antiparasitic, neurotoxicity, antibacterial, antifungal, antiviral, toxicity, antioxidant free-radical scavenging, allergenicity, DPP-IV inhibition, cell-penetrating peptide, bitter, umami, broad antimicrobial, antimalarial, quorum sensing, anticancer and anti-MRSA. For category *c*,

N_high(c) = Σ_i 1{P_i(c) ≥ 0.8}

The 0.8 cut is an operational high-confidence rule, not a calibrated posterior of wet-lab activity. Software version and random seeds were not stated in the source draft (`AUTHOR_INPUT_NEEDED`).

### 2.6 Three-model filter

Only peptides with BBB probability ≥ 0.8 entered NTxPred2, mebipred and AnOxPePred. NTxPred2 was run on sequences ≥ 7 aa. AnOxPePred supplied a free-radical scavenging score (FRS) and a chelator score (CHEL). Mebipred scored metal-binding potential; Cu, Fe and Zn were retained. High CHEL and modest FRS defined priority for later metal-linked oxidative-stress work; the source draft states that this class is not experimental pro-oxidant activity.

### 2.7 Structural targets and what was computed at this stage

The source draft lists AChE, butyrylcholinesterase, Aβ42, tau, ApoE4, ferritin and transferrin as structural targets, with AChE attention on the CAS, the PAS and the AChE–Aβ interface. PAS-focused docking of the twelve main candidates against human AChE (PDB 4EY6) has now been completed and is reported in Section 3.7. The remaining targets, full metal-ion coordination modelling, production molecular dynamics and QM/MM/DFT are future work (Section 4.5). GSE42872 (vemurafenib in BRAF-V600E A375 melanoma [34]) and a Chinese translation of a 1 μs AChE–Aβ trajectory [9] are archived beside this project and are not inputs to the screening tables; the GSE42872 files are documented in the excluded-source record.

### 2.8 Exploratory statistics

Donor-level mixed models were not possible from the deposited tables. For description only, two-sided Fisher’s exact tests and χ² tests were computed on peptide 2 × 2 tables (SciPy 1.17). Odds ratios are periodontitis versus healthy unless noted. No multiple-comparison correction was applied across UniDL4BioPep heads. These *P* values do not replace a donor-level analysis.

### 2.9 Figures

Figures were drawn in Python 3 (matplotlib) with a colour-blind-safe pair (blue `#0072B2`, vermillion `#D55E00`). Vector PDFs are the submission masters; PNGs are previews.

### 2.10 PAS-focused molecular docking (AutoDock Vina 1.2.5)

**Receptor.** The receptor was recombinant human AChE in complex with (−)-galantamine (PDB 4EY6; 2.40 Å resolution; expressed in HEK-293 cells [8]). The co-crystallised ligand, waters and non-protein entities were removed during preparation; polar hydrogens and partial charges were assigned in the standard AutoDock preparation workflow (preparation toolchain details: `AUTHOR_INPUT_NEEDED`). 4EY6 carries chain breaks with unresolved loop segments near residues 259–262 and 492–495; these segments were not modelled at this stage and are treated as a limitation (Section 4.4).

**Ligands.** The twelve main-candidate peptides (Table 5) were built as flexible linear chains and energy-minimised before docking (`AUTHOR_INPUT_NEEDED` for the exact builder/minimiser). No metal ion was present in the docking runs; metal coordination is addressed separately in the roadmap (Section 4.5).

**Search space and search.** A cubic grid of 40 × 40 × 40 Å³ was centred on the PAS region of 4EY6, covering the PAS rim (Tyr72, Asp74, Tyr124, Trp286, Tyr341) and the entrance of the active-site gorge. Docking was performed with AutoDock Vina v1.2.5 [35,36], with peptide side-chain and backbone flexibility enabled (`AUTHOR_INPUT_NEEDED` for exhaustiveness, number of runs and seed settings). Vina scores are reported as mean ± SD in kcal/mol. Vina is a scoring-function ranking tool: its scores correlate with, but are not, experimental binding free energies, and comparisons across very different ligand chemistries are discouraged by the method itself [35]; here all twelve ligands are closely related 7–9-mers, so within-set comparison is the intended use.

**Pose analysis.** Top poses were inspected for (i) full containment within the box (no pose truncated at the box edge), (ii) contacts with PAS core residues (Tyr72, Asp74, Tyr124, Trp286, Tyr341), (iii) contacts with gorge aromatic residues (Trp86, Phe295, Tyr337, Phe338), and (iv) reach of side chains toward the catalytic region (Ser203, His447). Interaction tallies are qualitative at this stage; per-peptide interaction tables will accompany the MD stage. Rosetta FlexPepDocking [37] is the literature-preferred protocol for peptide–protein docking and is listed as the upgrade path (Section 4.5); at the current stage its C++ command-line parameter system and large-scale flexible sampling are still being mastered, so the validated Vina pipeline was used for the reported runs.

### 2.11 Attempted molecular dynamics (reported, not included)

Following the 100-ns simulation protocol established for the AChE–Aβ system [9], we attempted all-atom MD of the best-docked peptide–AChE complex using GROMACS 2025 [38] with the AMBER99SB-ILDN force field [39], the TIP3P water model [40] and a triclinic periodic box. During the NPT pressure-equilibration stage (Berendsen barostat [41]), the system developed severe anisotropic pressure oscillations along the Z axis and ultimately failed (box blow-up). Two proximate causes were identified: (i) the local chain breaks of 4EY6 (unresolved segments near residues 259–262 and 492–495) create internal strain once solvent pressure is applied; (ii) rigid insertion of the docked peptide leaves residual interfacial stress. Remediation in progress includes Z-axis pressure-coupling parameters (compressibility, τ_p) and relaxation schedules, ACE/NME capping of the broken loop segments, and side-chain debumping of the peptide–protein interface. No production trajectory is therefore included in this version; the 100-ns analysis remains a deliverable of the next stage.

## 3. Results

### 3.1 Proteomes discard more than 99.7% of translated sORFs

Raw sORF libraries contained 11,269,961 healthy and 11,721,988 periodontitis sequences. Exact proteomic support left 31,510 and 33,786 unique peptides (Table 1). Passage rates were 0.2796% and 0.2882%. Periodontitis contributed 51.75% of the combined confirmed library (65,296 peptides).

**Table 1.** Proteomic support of group-specific sORFs.

| Group | Specific sORFs | Unique supported peptides | Passage (%) | Share of confirmed library (%) |
| --- | ---: | ---: | ---: | ---: |
| Healthy | 11,269,961 | 31,510 | 0.2796 | 48.25 |
| Periodontitis | 11,721,988 | 33,786 | 0.2882 | 51.75 |
| Total | 22,991,949 | 65,296 | 0.2839 | 100.00 |

A peptide-level χ² test on passage is statistically significant because the denominators are huge (χ² = 15.1, *P* = 1.0 × 10⁻⁴). The absolute difference is 0.0086 percentage points; we do not interpret that *P* value as a biological effect. The confirmed sets are the only denominators used below.

### 3.2 BBB calls: counts rise in periodontitis; only the long branch changes in rate

At BBB probability ≥ 0.8 the short branch yielded 3,359 healthy and 3,446 periodontitis peptides (10.99% vs 10.52% of each proteome-supported short set). The long branch yielded 40 and 72 (4.20% vs 6.98%). An exploratory Fisher test on the long-branch 2 × 2 table gives OR = 1.71 for periodontitis versus healthy (*P* = 0.0084); the corresponding short-branch test is not significant (OR = 0.95, *P* = 0.056). Absolute periodontitis excess, plus the long-branch rate, is what feeds the AD-oriented funnel. Short-branch BBB **percentages** do not support a “more BBB-positive periodontitis peptidome” slogan.

### 3.3 Long peptides: barrier and antibacterial heads move together

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

### 3.4 Short peptides: counts track library size; one head saturates

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

### 3.5 The BBB set is mostly 8–15 aa

Restricting the periodontitis-oriented joint library to BBB ≥ 0.8 gave 3,518 peptides: 3,446 short and 72 long. Of the short BBB set, 2,893 (83.95%) were 8–15 aa, 547 were 5–7 aa and 6 were 16–30 aa (Fig. 4). All 72 long peptides sit in 31–50 aa. An AD-oriented wet list is therefore dominated by 8–15-mer chemistry; the twelve docking candidates (7–9 aa) sit squarely inside that mode.

### 3.6 Three models collapse 3,518 peptides to 12 (8)—and the sequences are now known

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

### 3.7 PAS-focused docking: all twelve candidates occupy the PAS–gorge interface of human AChE

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

## 4. Discussion

### 4.1 The funnel is a triage result, and its grain size is now right for docking

The operational product of the screening stage is a prioritisation result: oral proteomes discard more than 99.7% of translated sORFs, and a BBB-first, metal-second, scavenger-low stack reduces 33,786 periodontitis-supported peptides to 12 (8 at the stricter cut). What the structure stage adds is the readout that makes the list actionable: every one of the twelve candidates can physically occupy the PAS–gorge interface of human AChE with plausible chemistry and Vina scores below −8 kcal/mol. A twelve-peptide list with poses is a project; a twelve-peptide list without poses was an inventory.

### 4.2 What PAS docking adds—and what it does not

The PAS was chosen as the docking target for two documented reasons: it is the AChE surface that accelerates Aβ fibril assembly [4–6], and it borders the 344–361 Aβ residence patch identified by a microsecond simulation [9]. The docking result therefore positions the oral candidates on the exact surface where AChE–Aβ cross-talk is believed to begin. The cationic, aromatic, His-rich composition of the twelve peptides fits that surface: the PAS is an anionic, aromatic rim, and every candidate carries at least one Arg/Lys while eleven of twelve carry His, a residue that can simultaneously participate in PAS stacking networks and in later Cu/Fe/Zn coordination [27]. That dual use of His—surface anchoring and metal anchoring—is precisely the chemistry the CHEL-high / FRS-low filter was designed to enrich, and the docking stage shows it is spatially compatible with a disease-relevant AChE site.

None of this is a binding constant. Vina’s scoring function is a fast approximation calibrated for enrichment, not affinity [35]; a single rigid receptor conformation was used; 4EY6’s missing loops (near residues 259–262 and 492–495) and its glycosylation state are not represented in the docking; no explicit water or metal ion was present; peptide protonation states were not sampled. The MD attempt (Section 2.11) exists precisely because we do not treat −9.60 kcal/mol as a measured free energy—it failed at pressure equilibration for the structural reasons above, and no trajectory is reported. Readers should carry one sentence forward: **the docking orders twelve candidates; it does not certify any of them.**

### 4.3 Reading the candidates against the exogenous-peptide neurotoxicity template

The closest structural precedent for a short, metal-binding, neuroactive peptide is tau26–44: 19 residues, intrinsically disordered, toxic through NMDA-receptor-mediated necrotic-type pathways, and Cu(II)-binding via histidine with measurable effects on copper-induced Aβ aggregation [27,28]. Our candidates are shorter (7–9 aa) and exogenous to the human proteome, with two consequences. In their favour, size places them in the window where predicted BBB passage is most credible (the BBB-positive short set is 83.95% 8–15 aa; Fig. 4), and His/Cys density gives them the same metal-anchoring handles that make tau26–44 copper-active. Against them, nothing is known: no NMDA dependence, no membrane perturbation, no aggregation cross-seeding has been tested, and the bacterial-amyloid precedent (curli feeding α-synuclein aggregation after oral exposure [29]) is a different protein system entirely. The honest statement is that the twelve peptides are *formatted like* known short neuroactive peptides, not that they behave like them.

### 4.4 Limitations

Screening limitations are those of a single 24-versus-26 donor collection, exact-match proteomics, black-box predictors at fixed cut-offs, and peptide-level *P* values that ignore donor clustering. Structure-stage limitations add: a single receptor conformation without the unresolved loop segments of 4EY6; no glycans, no crystallographic waters, no metal ion in the box; Vina scoring without re-scoring by MM/GBSA (deferred); starting-conformation sensitivity of flexible peptides; and taxonomy—the MAG collection is a community oral metagenome [33], so calling the twelve sequences “*P. gingivalis* peptides” remains a taxonomy error until each sequence is assigned. Software versions/seeds for UniDL4BioPep, NTxPred2, mebipred, AnOxPePred, and the docking exhaustiveness/seed settings, are marked `AUTHOR_INPUT_NEEDED` for the submission version. GSE42872 is a six-sample melanoma microarray [34] and must not enter an AD contrast.

### 4.5 Roadmap for the mechanism stage

The author’s forward protocol is adopted as the continuation plan, condensed here. **(i) Peptide structures.** Multi-conformer modelling of the 7–9-mers rather than single static structures; AlphaFold3 [42] for peptide–protein and peptide–metal complex modelling, used as a reference framework to be validated by conformational sampling, confidence metrics and MD—not as a substitute for experimental structures. **(ii) Target panel.** Beyond PAS: AChE CAS and the 344–361 Aβ-residence patch, then BChE, Aβ42, tau, ApoE4, ferritin and transferrin—Aβ/tau targets test effects on pathological aggregation or conformational stability; ferritin/transferrin test crosstalk with iron-homeostasis machinery. **(iii) Metals.** Cu²⁺, Fe²⁺/Fe³⁺ and Zn²⁺: docking and structural modelling to screen coordination geometries; MD for metal–ligand distances, coordination number and stability; MM/GBSA or MM/PBSA for relative binding free energies [43]; QM/MM or DFT only on stable coordination shells, for geometry, coordination energy, charge distribution and possible electron-transfer character. **(iv) Docking upgrade.** Rosetta FlexPepDocking [37] once its parameter system and flexible sampling are fully operational; the present Vina stage is the validated interim. **(v) MD.** The 100-ns AChE–Aβ protocol [9] in GROMACS [38], after fixing the Z-axis pressure instability via compressibility/τ_p relaxation schedules, ACE/NME capping of the broken loop segments, and peptide debumping. **(vi) Wet validation cascade.** Metal binding (ITC/spectroscopy), Cu/Fe-dependent ROS, lipid peroxidation, AChE/BChE activity, Aβ aggregation and neuronal viability—under the stopping rule that only metal-conditioned ROS/lipid-peroxidation increases accompanied by neuronal injury support the phrase “metal-linked pro-oxidant neurotoxicity.”


## Declarations

**Data availability.** PRJNA678453, PRJEB65451, PXD003151, PXD004319, PXD026727 and HOMD are public; PDB 4EY6 is public [8]. The twelve candidate sequences are in Table 5. Author screening tables are in the project’s `source-docs/` folder.

**Code availability.** Figure and audit scripts are in the project’s `scripts/` folder. UniDL4BioPep is described by Du et al. [32]; AutoDock Vina by Trott & Olson [35] and Eberhardt et al. [36].

**Ethics.** No new human or animal work was performed; the re-analysis uses public, de-identified assemblies.

**Competing interests.** None recorded (`AUTHOR_INPUT_NEEDED`).

**Funding.** None recorded (`AUTHOR_INPUT_NEEDED`).

**Author contributions.** `AUTHOR_INPUT_NEEDED` (CRediT).

**AI use.** An AI assistant assembled this manuscript from the author’s methods/results drafts under a documented skill-routed workflow, and verified the new citations against PubMed/PDB records (see the project’s provenance log). The authors remain responsible for every number and claim.

**Statistical analysis.** Independent experimental units were donors (group-level counts documented in the source assembly). Peptide counts are nested observations. Descriptive statistics are counts and percentages of proteome-supported peptides within length branch. Exploratory two-sided Fisher’s exact tests on peptide 2 × 2 tables used SciPy 1.17; no multiplicity correction was applied across UniDL4BioPep categories. Donor-level mixed models were not fitted because a donor-by-peptide matrix was not deposited. Docking scores (Table 5) are reported as mean ± SD; no inferential statistics were applied to a within-set ranking. Software versions for UniDL4BioPep, NTxPred2, mebipred, AnOxPePred and docking search parameters were not stated in the source drafts.

## References

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
