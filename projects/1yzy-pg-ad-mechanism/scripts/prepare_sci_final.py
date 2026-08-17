#!/usr/bin/env python3
"""Build the clean English SCI manuscript source from the audited English master.

The transformation is intentionally explicit: it removes workflow-only prose and
unresolved placeholder tokens, narrows unsupported claims, fixes the reference
inventory, and leaves author-identifying declarations outside the blinded file.
"""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "manuscript" / "manuscript_en.md"
OUTPUT = ROOT / "manuscript" / "manuscript_sci_final.md"
SUPPLEMENT_SOURCE = ROOT / "manuscript" / "supplementary_tables_bilingual.md"
SUPPLEMENT_OUTPUT = ROOT / "manuscript" / "supplementary_tables_sci_final.md"

TITLE = (
    "Proteome-supported screening of periodontitis-associated peptides encoded by small open reading frames "
    "identifies candidates with predicted metal binding, blood–brain barrier permeability and "
    "acetylcholinesterase docking potential"
)

ABSTRACT = """## Abstract

**Background:** Periodontitis is epidemiologically associated with Alzheimer’s disease (AD), but most molecular models focus on intact *Porphyromonas gingivalis* cells, gingipain proteases, or outer-membrane vesicles. Short peptides encoded by oral small open reading frames (sORFs) remain poorly characterised, and their potential interaction with the peripheral anionic site (PAS) of acetylcholinesterase (AChE) has not been systematically prioritised.

**Methods:** We re-analysed a public oral metagenome collection (BioProject PRJNA678453; assembly set PRJEB65451) comprising 296 high-quality metagenome-assembled genomes. Group-associated sORF libraries (4–50 amino acids) were matched by exact identity to oral proteome resources, scored with UniDL4BioPep at a probability threshold of 0.8, and evaluated in separate short (5–30 aa) and long (31–50 aa) branches. Sequences classified as blood–brain barrier (BBB)-positive were filtered with NTxPred2, mebipred and AnOxPePred. The resulting candidates were docked with AutoDock Vina 1.2.5 into a 40 × 40 × 40 Å³ search box centred on the PAS of human AChE (PDB 4EY6).

**Results:** Raw libraries contained 11,269,961 healthy-associated and 11,721,988 periodontitis-associated sORFs; exact proteome matching retained 31,510 and 33,786 unique peptides, respectively (0.2796% and 0.2882%). The periodontitis-associated library contained more predicted BBB-positive peptides by count in both length branches (short, 3,446 vs 3,359; long, 72 vs 40), although only the long-branch proportion differed in an exploratory peptide-level analysis. Of 3,518 BBB-positive sequences, 3,299 met the NTxPred2 length requirement, 923 received a neurotoxicity label, 111 received a Cu/Fe/Zn-binding label, and a chelator-high/scavenger-low rule retained 12 primary candidates (8 at the stricter scavenger threshold). The primary candidates were 7–9 residues long; 11 contained histidine and 6 contained cysteine. PAS-centred docking produced fully contained top-ranked poses with reported Vina scores from −8.25 to −9.60 kcal/mol. Qualitative inspection suggested contacts with PAS and gorge residues, with some poses extending towards the catalytic region.

**Conclusions:** This proteome-supported workflow reduced a large oral sORF search space to a testable set of 12 periodontitis-associated peptide candidates. The classifier outputs and docking poses support prioritisation only; they do not establish taxonomic origin, brain exposure, binding affinity, neurotoxicity, or an AD mechanism. Experimental transport, metal-binding, cholinesterase, aggregation and neuronal assays are required before mechanistic interpretation.

**Keywords:** periodontitis; small open reading frame; metaproteome; blood–brain barrier; metal binding; acetylcholinesterase; peripheral anionic site; molecular docking; Alzheimer’s disease
"""

DECLARATIONS = """## Declarations

**Data availability.** PRJNA678453, PRJEB65451, PXD003151, PXD004319, PXD026727, HOMD and PDB 4EY6 are publicly accessible. The aggregate screening counts and the 12 candidate sequences required to interpret the reported results are provided in the main and supplementary tables.

**Code availability.** No new software package was developed. The external prediction, docking and simulation software used in the study is identified and cited in the Methods. Analysis records and custom audit scripts are available from the corresponding author on reasonable request.

**Ethics approval.** No new human or animal experiments were performed. The analysis used public, de-identified sequence assemblies and proteome resources.
"""

REFERENCE_BLOCK = """## References

1. Scheltens P, De Strooper B, Kivipelto M, Holstege H, Chételat G, Teunissen CE, et al. Alzheimer's disease. Lancet. 2021;397(10284):1577–1590. doi:10.1016/S0140-6736(20)32205-4
2. Selkoe DJ, Hardy J. The amyloid hypothesis of Alzheimer's disease at 25 years. EMBO Mol Med. 2016;8(6):595–608. doi:10.15252/emmm.201606210
3. Hampel H, Mesulam MM, Cuello AC, Farlow MR, Giacobini E, Grossberg GT, et al. The cholinergic system in the pathophysiology and treatment of Alzheimer's disease. Brain. 2018;141(7):1917–1933. doi:10.1093/brain/awy132
4. Inestrosa NC, Alvarez A, Pérez CA, Moreno RD, Vicente M, Linker C, et al. Acetylcholinesterase accelerates assembly of amyloid-β-peptides into Alzheimer's fibrils: possible role of the peripheral site of the enzyme. Neuron. 1996;16(4):881–891. doi:10.1016/S0896-6273(00)80108-7
5. De Ferrari GV, Canales MA, Shin I, Weiner LM, Silman I, Inestrosa NC. A structural motif of acetylcholinesterase that promotes amyloid β-peptide fibril formation. Biochemistry. 2001;40(35):10447–10457. doi:10.1021/bi0101392
6. Bartolini M, Bertucci C, Cavrini V, Andrisano V. β-Amyloid aggregation induced by human acetylcholinesterase: inhibition studies. Biochem Pharmacol. 2003;65(3):407–416. doi:10.1016/S0006-2952(02)01514-9
7. Kryger G, Silman I, Sussman JL. Structure of acetylcholinesterase complexed with E2020 (Aricept): implications for the design of new anti-Alzheimer drugs. Structure. 1999;7(3):297–307. doi:10.1016/S0969-2126(99)80040-9
8. Cheung J, Rudolph MJ, Burshteyn F, Cassidy MS, Gary EN, Love J, et al. Structures of human acetylcholinesterase in complex with pharmacologically important ligands. J Med Chem. 2012;55(23):10282–10286. doi:10.1021/jm300871x
9. Atanasova M, Dimitrov I, Ivanov S. Molecular dynamics simulations of acetylcholinesterase–beta-amyloid peptide complex. Cybern Inf Technol. 2020;20(6):140–154. doi:10.2478/cait-2020-0068
10. Lushchekina SV, Kots ED, Novichkova DA, Petrov KA, Masson P. Role of acetylcholinesterase in β-amyloid aggregation studied by accelerated molecular dynamics. BioNanoScience. 2017;7:396–402. doi:10.1007/s12668-016-0375-x
11. Ide M, Harris M, Stevens A, Sussams R, Hopkins V, Culliford D, et al. Periodontitis and cognitive decline in Alzheimer's disease. PLoS One. 2016;11(3):e0151081. doi:10.1371/journal.pone.0151081
12. Sparks Stein P, Desrosiers M, Donegan SJ, Yepes JF, Kryscio RJ. Tooth loss, dementia and neuropathology in the Nun study. J Am Dent Assoc. 2007;138(10):1314–1322. doi:10.14219/jada.archive.2007.0046
13. Jiang Z, Shi Y, Zhao W, Zhou L, Zhang B, Xie Y, et al. Association between chronic periodontitis and the risk of Alzheimer's disease: combination of text mining and GEO dataset. BMC Oral Health. 2021;21:466. doi:10.1186/s12903-021-01827-2
14. Dominy SS, Lynch C, Ermini F, Benedyk M, Marczyk A, Konradi A, et al. Porphyromonas gingivalis in Alzheimer's disease brains: evidence for disease causation and treatment with small-molecule inhibitors. Sci Adv. 2019;5(1):eaau3333. doi:10.1126/sciadv.aau3333
15. Poole S, Singhrao SK, Kesavalu L, Curtis MA, Crean S. Determining the presence of Porphyromonas gingivalis in Alzheimer's disease brain. J Alzheimers Dis. 2013;33(3):665–678. doi:10.3233/JAD-2012-121149
16. Ilievski V, Zuchowska PK, Green SJ, Toth PT, Ragozzino ME, Le K, et al. Chronic oral application of a periodontal pathogen results in brain inflammation, neurodegeneration and amyloid beta production in wild type mice. PLoS One. 2018;13(10):e0204941. doi:10.1371/journal.pone.0204941
17. Haditsch U, Roth T, Rodriguez L, Hancock S, Cecere T, Nguyen M, et al. Alzheimer's disease-like neurodegeneration in Porphyromonas gingivalis infected neurons with persistent expression of active gingipains. J Alzheimers Dis. 2020;75(4):1361–1376. doi:10.3233/JAD-200393
18. Ho MH, Chen CH, Goodwin JS, Wang BY, Xie H. Functional advantages of Porphyromonas gingivalis vesicles. PLoS One. 2015;10(4):e0123448. doi:10.1371/journal.pone.0123448
19. Nara PL, Sindelar D, Penn MS, Potempa J, Griffin WST. Porphyromonas gingivalis outer membrane vesicles as the major driver of and explanation for neuropathogenesis, the cholinergic hypothesis, iron dyshomeostasis, and salivary lactoferrin in Alzheimer's disease. J Alzheimers Dis. 2021;82(4):1417–1450. doi:10.3233/JAD-210448
20. Guo Y, Nguyen KA, Potempa J. Dichotomy of gingipains action as virulence factors: from cleaving substrates with the precision of a surgeon's knife to a meat chopper-like brutal degradation of proteins. Periodontol 2000. 2010;54(1):15–44. doi:10.1111/j.1600-0757.2010.00377.x
21. Ryder MI. Porphyromonas gingivalis and Alzheimer disease: recent findings and potential therapies. J Periodontol. 2020;91(Suppl 1):S45–S49. doi:10.1002/JPER.20-0104
22. Kanagasingam S, Chukkapalli SS, Welbury R, Singhrao SK. Porphyromonas gingivalis is a strong risk factor for Alzheimer's disease. J Alzheimers Dis Rep. 2020;4(1):501–511. doi:10.3233/ADR-200250
23. Li J, Lian T, Guo P, Li J, Qi J, He M, et al. Different stages of Alzheimer's disease with periodontitis: clinical features and potential mechanisms involving gingipains, neuropathological biomarkers and neurological damage. Front Aging Neurosci. 2026;18:1737524. doi:10.3389/fnagi.2026.1737524
24. Díaz-Zúñiga J, More J, Melgar-Rodríguez S, Jiménez-Unión M, Villalobos-Orchard F, Muñoz-Manríquez C, et al. Alzheimer's disease-like pathology triggered by Porphyromonas gingivalis in wild type rats is serotype dependent. Front Immunol. 2020;11:588036. doi:10.3389/fimmu.2020.588036
25. Bush AI. The metal theory of Alzheimer's disease. J Alzheimers Dis. 2013;33 Suppl 1:S277–S281. doi:10.3233/JAD-2012-129011
26. Lei P, Ayton S, Bush AI. The essential elements of Alzheimer's disease. J Biol Chem. 2021;296:100105. doi:10.1074/jbc.REV120.008207
27. Di Natale G, Bellia F, Sciacca MFM, Campagna T, Pappalardo G. Tau-peptide fragments and their copper(II) complexes: effects on amyloid-β aggregation. Inorg Chim Acta. 2018;472:82–92. doi:10.1016/j.ica.2017.09.061
28. Perini G, Ciasca G, Minelli E, Papi M, Palmieri V, Maulucci G, et al. Dynamic structural determinants underlie the neurotoxicity of the N-terminal tau 26–44 peptide in Alzheimer's disease and other human tauopathies. Int J Biol Macromol. 2019;141:278–289. doi:10.1016/j.ijbiomac.2019.08.220
29. Chen SG, Stribinskis V, Rane MJ, Gozal D, Friedland RP. Exposure to the functional bacterial amyloid protein curli enhances alpha-synuclein aggregation in aged Fischer 344 rats and Caenorhabditis elegans. Sci Rep. 2016;6:34477. doi:10.1038/srep34477
30. Couso JP, Patra P. Short ORFs: finding gems in hidden places. Curr Opin Genet Dev. 2017;45:14–21. doi:10.1016/j.gde.2017.04.002
31. van Heesch S, Witte F, Schneider-Lunitz V, Schulz JF, Adami E, Faber AB, et al. The translational landscape of the human heart. Cell. 2019;178(1):242–260.e29. doi:10.1016/j.cell.2019.05.010
32. Du Z, Ding X, Xu Y, Li Y. UniDL4BioPep: a universal deep learning architecture for binary classification in peptide bioactivity. Brief Bioinform. 2023;24(3):bbad135. doi:10.1093/bib/bbad135
33. Belstrøm D, Constancias F, Drautz-Moses DI, Schuster SC, Veleba M, Mahé F, et al. Periodontitis associates with species-specific gene expression of the oral microbiota. NPJ Biofilms Microbiomes. 2021;7:76. doi:10.1038/s41522-021-00247-y
34. Trott O, Olson AJ. AutoDock Vina: improving the speed and accuracy of docking with a new scoring function, efficient optimization, and multithreading. J Comput Chem. 2010;31(2):455–461. doi:10.1002/jcc.21334
35. Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. J Chem Inf Model. 2021;61(8):3891–3898. doi:10.1021/acs.jcim.1c00203
36. London N, Raveh B, Cohen E, Fathi G, Schueler-Furman O. Rosetta FlexPepDock web server—high resolution modeling of peptide–protein interactions. Nucleic Acids Res. 2011;39(Web Server issue):W249–W253. doi:10.1093/nar/gkr326
37. Abraham MJ, Murtola T, Schulz R, Páll S, Smith JC, Hess B, et al. GROMACS: high performance molecular simulations through multi-level parallelism from laptops to supercomputers. SoftwareX. 2015;1–2:19–25. doi:10.1016/j.softx.2015.06.001
38. Hornak V, Abel R, Okur A, Strockbine B, Roitberg A, Simmerling C. Comparison of multiple Amber force fields and development of improved protein backbone parameters. Proteins. 2006;65(3):712–725. doi:10.1002/prot.21123
39. Jorgensen WL, Chandrasekhar J, Madura JD, Impey RW, Klein ML. Comparison of simple potential functions for simulating liquid water. J Chem Phys. 1983;79(2):926–935. doi:10.1063/1.445869
40. Berendsen HJC, Postma JPM, van Gunsteren WF, DiNola A, Haak JR. Molecular dynamics with coupling to an external bath. J Chem Phys. 1984;81(8):3684–3690. doi:10.1063/1.448118
41. Abramson J, Adler J, Dunger J, Evans R, Green T, Pritzel A, et al. Accurate structure prediction of biomolecular interactions with AlphaFold 3. Nature. 2024;630(8016):493–500. doi:10.1038/s41586-024-07487-w
42. Genheden S, Ryde U. The MM/PBSA and MM/GBSA methods to estimate ligand-binding affinities. Expert Opin Drug Discov. 2015;10(5):449–461. doi:10.1517/17460441.2015.1032936
"""


def replace_once(text: str, old: str, new: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one match, found {count}: {old[:100]!r}")
    return text.replace(old, new, 1)


def build() -> str:
    text = SOURCE.read_text(encoding="utf-8")
    start = text.index("## Abstract")
    intro = text.index("## 1. Introduction")
    text = f"# {TITLE}\n\n" + ABSTRACT.rstrip() + "\n\n" + text[intro:]

    text = replace_once(
        text,
        "Short, His/Cys-rich peptides are among the few molecular formats that plausibly do all of those things, which motivates screening the oral metaproteome for exactly that chemistry.",
        "Short, His/Cys-rich peptides combine compact size with potential metal-coordinating residues, which motivates screening the oral proteome for this chemical pattern while treating transport and redox activity as testable predictions rather than established properties.",
    )
    text = replace_once(
        text,
        "This paper has two stages. Stage one (Sections 2.2–2.9, 3.1–3.6) asks the countable question: after a periodontitis-associated sORF library is restricted to peptides observed in oral proteomes, how many survive a BBB filter, a neurotoxicity filter, a Cu/Fe/Zn filter, and a chelator-high / scavenger-low rule? The answer is twelve peptides (eight at a stricter scavenger cut). Stage two (Sections 2.10–2.11, 3.7) takes the twelve sequences—supplied by the author—to the structure level by PAS-focused molecular docking against human AChE (PDB 4EY6 [8]), the PAS being chosen because it is both the Aβ-accelerating site of AChE [4–6] and the neighbourhood of the published Aβ residence patch at residues 344–361 [9].",
        "This study had two stages. Stage one (Sections 2.2–2.8 and 3.1–3.6) asked how many periodontitis-associated, proteome-matched sORF peptides survived sequential BBB, neurotoxicity, Cu/Fe/Zn-binding, and chelator-high/scavenger-low filters. Stage two (Sections 2.9–2.10 and 3.7) evaluated the resulting 12 primary candidates by PAS-focused molecular docking against human AChE (PDB 4EY6 [8]). The PAS was selected because it promotes AChE-associated Aβ assembly [4–6] and lies near the simulated Aβ residence patch at residues 344–361 [9].",
    )
    text = replace_once(
        text,
        "Three boundaries are stated up front. (i) The MAG collection is a **community** oral metagenome [33], not a *P. gingivalis*-only peptidome; assignment of the twelve sequences to a single species is not claimed. (ii) Docking scores are ranking heuristics with known scoring-function bias; they are used here to compare twelve candidates against one binding site, not to predict dissociation constants. (iii) Molecular dynamics, QM/MM and all wet assays remain future work (Sections 2.11 and 4.5); the stopping rule stands—only a peptide that raises reactive oxygen species (ROS) or lipid peroxidation **in the presence of metal** and damages neurons earns the phrase “metal-linked pro-oxidant neurotoxicity.”",
        "Three interpretive boundaries were prespecified. First, the MAG collection represents a community oral metagenome [33], not a *P. gingivalis*-specific peptidome, and the 12 sequences are not assigned to a single species. Second, docking scores are pose-ranking heuristics rather than dissociation constants or binding free energies. Third, molecular dynamics and wet-laboratory assays were not successfully completed; mechanistic terms such as metal-linked pro-oxidant neurotoxicity therefore remain hypotheses requiring experimental testing.",
    )
    text = re.sub(
        r"\nThis evidence review follows the structured framework recommended by ZZL-Zoro Life-Science-Evidence-Review.*?without wet assays\.\n",
        "\n",
        text,
        count=1,
    )

    text = replace_once(
        text,
        "This is a computational re-analysis of public assemblies plus a structure-based docking stage on the resulting candidates. The independent experimental unit of the screening stage is the donor; peptide-level contingency tests are exploratory because peptides are nested within donors. No new human sampling was performed. The assembly set comprises 296 high-quality MAGs; donor-level counts are documented in the source assembly but are not reported here as the primary denominator. Screening methods follow the author’s mechanism draft; docking parameters follow the author’s PAS docking note.",
        "This computational study combined re-analysis of public oral sequence assemblies with structure-based docking of prioritised peptides. Donors were the independent sampling units in the source collection, whereas peptides were nested observations. Because only aggregate peptide counts were available for the present analysis, peptide-level contingency tests were treated as exploratory. No new human sampling was performed. The assembly set comprised 296 high-quality MAGs.",
    )
    text = replace_once(
        text,
        "The 0.8 cut is an operational high-confidence rule, not a calibrated posterior of wet-lab activity. Software version and random seeds were not stated in the source draft (`AUTHOR_INPUT_NEEDED`).",
        "The 0.8 threshold was an operational prioritisation rule, not a calibrated posterior probability of experimental activity. The archived prediction outputs did not retain software-version or random-seed metadata; this reproducibility limitation was considered when interpreting all classifier labels.",
    )
    text = replace_once(
        text,
        "High CHEL and modest FRS defined priority for later metal-linked oxidative-stress work; the source draft states that this class is not experimental pro-oxidant activity.",
        "High CHEL and modest FRS defined priority for later metal-linked oxidative-stress testing. This rule identifies a computational screening class and does not demonstrate pro-oxidant activity.",
    )
    text = replace_once(
        text,
        "The source draft lists AChE, butyrylcholinesterase, Aβ42, tau, ApoE4, ferritin and transferrin as structural targets, with AChE attention on the CAS, the PAS and the AChE–Aβ interface. PAS-focused docking of the twelve main candidates against human AChE (PDB 4EY6) has now been completed and is reported in Section 3.7. The remaining targets, full metal-ion coordination modelling, production molecular dynamics and QM/MM/DFT are future work (Section 4.5). GSE42872 (vemurafenib in BRAF-V600E A375 melanoma [34]) and a Chinese translation of a 1 μs AChE–Aβ trajectory [9] are archived beside this project and are not inputs to the screening tables; the GSE42872 files are documented in the excluded-source record.",
        "Structure-based analysis in this study was restricted to PAS-focused docking of the 12 primary candidates against human AChE (PDB 4EY6). No docking results are reported for butyrylcholinesterase, Aβ42, tau, ApoE4, ferritin or transferrin, and no explicit metal-coordination calculations were included. The attempted molecular dynamics workflow is reported separately in Section 2.10 because it did not yield a production trajectory.",
    )
    text = re.sub(
        r"\n### 2\.9 Figures\n\nFigures were drawn.*?PNGs are previews\.\n",
        "\n",
        text,
        count=1,
    )
    text = text.replace("### 2.10 PAS-focused molecular docking (AutoDock Vina 1.2.5)", "### 2.9 PAS-focused molecular docking")
    text = replace_once(
        text,
        "**Receptor.** The receptor was recombinant human AChE in complex with (−)-galantamine (PDB 4EY6; 2.40 Å resolution; expressed in HEK-293 cells [8]). The co-crystallised ligand, waters and non-protein entities were removed during preparation; polar hydrogens and partial charges were assigned in the standard AutoDock preparation workflow (preparation toolchain details: `AUTHOR_INPUT_NEEDED`). 4EY6 carries chain breaks with unresolved loop segments near residues 259–262 and 492–495; these segments were not modelled at this stage and are treated as a limitation (Section 4.4).",
        "**Receptor preparation.** The receptor was recombinant human AChE in complex with (−)-galantamine (PDB 4EY6; 2.40 Å resolution; expressed in HEK-293 cells [8]). The co-crystallised ligand, waters and non-protein entities were removed, and polar hydrogens and partial charges were assigned before docking. The archived run record did not retain the preparation program and version. Unresolved segments near residues 259–262 and 492–495 were not modelled.",
    )
    text = replace_once(
        text,
        "**Ligands.** The twelve main-candidate peptides (Table 5) were built as flexible linear chains and energy-minimised before docking (`AUTHOR_INPUT_NEEDED` for the exact builder/minimiser). No metal ion was present in the docking runs; metal coordination is addressed separately in the roadmap (Section 4.5).",
        "**Ligand preparation.** The 12 primary candidate peptides (Table 5) were represented as flexible linear ligands and energy-minimised before docking. The archived run record did not retain the builder and minimisation program versions. No metal ion was included in the docking calculations.",
    )
    text = replace_once(
        text,
        "**Search space and search.** A cubic grid of 40 × 40 × 40 Å³ was centred on the PAS region of 4EY6, covering the PAS rim (Tyr72, Asp74, Tyr124, Trp286, Tyr341) and the entrance of the active-site gorge. Docking was performed with AutoDock Vina v1.2.5 [35,36], with peptide side-chain and backbone flexibility enabled (`AUTHOR_INPUT_NEEDED` for exhaustiveness, number of runs and seed settings). Vina scores are reported as mean ± SD in kcal/mol. Vina is a scoring-function ranking tool: its scores correlate with, but are not, experimental binding free energies, and comparisons across very different ligand chemistries are discouraged by the method itself [35]; here all twelve ligands are closely related 7–9-mers, so within-set comparison is the intended use.",
        "**Search space and search.** A cubic 40 × 40 × 40 Å³ grid was centred on the PAS region of 4EY6 and covered the PAS rim (Tyr72, Asp74, Tyr124, Trp286 and Tyr341) and the entrance to the active-site gorge. Docking used AutoDock Vina 1.2.5 [34,35], with peptide torsions treated as flexible under the ligand representation. The archived output provided mean ± SD scores but did not retain exhaustiveness, run-count or random-seed settings. Scores were therefore used only for descriptive within-set ranking of the closely related 7–9-residue ligands and were not interpreted as experimental binding free energies [34].",
    )
    text = replace_once(
        text,
        "**Pose analysis.** Top poses were inspected for (i) full containment within the box (no pose truncated at the box edge), (ii) contacts with PAS core residues (Tyr72, Asp74, Tyr124, Trp286, Tyr341), (iii) contacts with gorge aromatic residues (Trp86, Phe295, Tyr337, Phe338), and (iv) reach of side chains toward the catalytic region (Ser203, His447). Interaction tallies are qualitative at this stage; per-peptide interaction tables will accompany the MD stage. Rosetta FlexPepDocking [37] is the literature-preferred protocol for peptide–protein docking and is listed as the upgrade path (Section 4.5); at the current stage its C++ command-line parameter system and large-scale flexible sampling are still being mastered, so the validated Vina pipeline was used for the reported runs.",
        "**Pose analysis.** Top-ranked poses were visually inspected for (i) containment within the search box, (ii) proximity to PAS residues Tyr72, Asp74, Tyr124, Trp286 and Tyr341, (iii) proximity to gorge aromatics Trp86, Phe295, Tyr337 and Phe338, and (iv) extension towards Ser203 and His447. These observations were qualitative and were not treated as residue-level interaction frequencies. Flexible peptide–protein docking and independent rescoring were reserved for validation work [36].",
    )
    text = text.replace("### 2.11 Attempted molecular dynamics (reported, not included)", "### 2.10 Attempted molecular dynamics")
    text = replace_once(
        text,
        "Following the 100-ns simulation protocol established for the AChE–Aβ system [9], we attempted all-atom MD of the best-docked peptide–AChE complex using GROMACS 2025 [38] with the AMBER99SB-ILDN force field [39], the TIP3P water model [40] and a triclinic periodic box. During the NPT pressure-equilibration stage (Berendsen barostat [41]), the system developed severe anisotropic pressure oscillations along the Z axis and ultimately failed (box blow-up). Two proximate causes were identified: (i) the local chain breaks of 4EY6 (unresolved segments near residues 259–262 and 492–495) create internal strain once solvent pressure is applied; (ii) rigid insertion of the docked peptide leaves residual interfacial stress. Remediation in progress includes Z-axis pressure-coupling parameters (compressibility, τ_p) and relaxation schedules, ACE/NME capping of the broken loop segments, and side-chain debumping of the peptide–protein interface. No production trajectory is therefore included in this version; the 100-ns analysis remains a deliverable of the next stage.",
        "A 100-ns all-atom simulation of the top-ranked peptide–AChE complex was attempted following the published AChE–Aβ framework [9]. The workflow used GROMACS 2025 [37], AMBER99SB-ILDN [38], TIP3P water [39], a triclinic periodic box and a Berendsen barostat during initial pressure equilibration [40]. Severe anisotropic pressure oscillation occurred during NPT equilibration and the system became unstable before production. Because the contributing factors were not isolated in controlled diagnostic runs, no cause was assigned and no trajectory-derived result is reported.",
    )

    text = text.replace("(Fig. 2a)", "")
    text = text.replace("(Fig. 2b)", "")
    text = text.replace("(Fig. 4)", "")
    text = text.replace("(Table 4; Fig. 3)", "(Table 4)")
    text = text.replace("(Table 5; Fig. 5)", "(Table 5)")
    text = text.replace("The source draft highlights periodontitis **counts**", "The periodontitis-associated library had higher **counts**")
    text = text.replace("### 3.6 Three models collapse 3,518 peptides to 12 (8)—and the sequences are now known", "### 3.6 Sequential filtering reduces 3,518 BBB-positive peptides to 12 primary candidates")
    text = replace_once(
        text,
        "The author supplied the twelve sequences (Table 5, column 2). They are 7–9 residues long, leucine-rich (every sequence carries ≥ 2 leucines), predominantly basic (all 12 carry ≥ 1 Arg/Lys; none carries Asp/Glu), with His in 11 of 12 and Cys in 6 of 12. That composition is exactly the His/Cys anchoring chemistry of the metal-binding filter that selected them, and it parallels the His-dependent Cu(II) coordination of the tau26–44 template [27].",
        "The 12 primary sequences (Table 5) were 7–9 residues long and leucine-rich (each contained at least two leucines). All carried at least one Arg or Lys, none contained Asp or Glu, 11 contained His and 6 contained Cys. This composition is consistent with enrichment by the metal-binding screen and provides a testable parallel to the His-dependent Cu(II) coordination of tau26–44 [27].",
    )
    text = replace_once(
        text,
        "Membership of the 8-peptide high-confidence subset among the twelve sequences: `AUTHOR_INPUT_NEEDED` (the stricter FRS cut was applied upstream; the subset labels were not deposited with the sequences).",
        "The archived aggregate output recorded eight sequences at FRS < 0.45 but did not retain an identifier-level mapping for that stricter subset. The 12-sequence FRS < 0.50 set was therefore used for all candidate-level analyses.",
    )
    text = text.replace("### 3.7 PAS-focused docking: all twelve candidates occupy the PAS–gorge interface of human AChE", "### 3.7 PAS-focused docking yields a descriptive within-set ranking")
    text = replace_once(
        text,
        "The twelve main candidates were docked into a 40 × 40 × 40 Å³ box centred on the PAS of 4EY6 [8] using AutoDock Vina 1.2.5. Every peptide’s top pose was fully contained within the box—no pose was truncated at a box edge—so the PAS-focused search space was large enough for these 7–9-mers. Vina scores spanned −8.25 to −9.60 kcal/mol with tight run-to-run dispersion (SD 0.04–0.12), indicating a consistent binding solution rather than a flat energy landscape (Table 5).",
        "PAS-centred AutoDock Vina docking produced a fully contained top-ranked pose for each of the 12 candidates in the 40 × 40 × 40 Å³ search box. Reported mean scores ranged from −8.25 to −9.60 kcal/mol, with reported SDs of 0.04–0.12 kcal/mol (Table 5). Because replicate counts, seeds and starting-conformer details were unavailable, the score range was treated as a descriptive ranking rather than evidence of affinity or convergence.",
    )
    text = replace_once(
        text,
        "Three features of the binding solutions are reported qualitatively. First, all twelve peptides adopted a **gorge-spanning mode**: density over the PAS rim combined with extension down the aromatic gorge toward the CAS, rather than shallow surface adsorption at the rim alone. Second, poses make dense hydrogen-bond and π–π stacking networks with the PAS core residues Tyr72, Asp74, Tyr124, Trp286 and Tyr341, and with the gorge aromatics Trp86, Phe295, Tyr337 and Phe338—the same aromatic ladder that guides substrates and classical inhibitors down the gorge [7,8]. Third, in several top poses side chains reach the catalytic region around Ser203 and His447, which is why these candidates should also be scored against the CAS in the follow-up panel (Section 4.5).",
        "Qualitative visual inspection suggested a recurrent gorge-spanning orientation, with peptide density near the PAS rim and extension into the aromatic gorge. The inspected poses approached PAS residues Tyr72, Asp74, Tyr124, Trp286 and Tyr341 and gorge residues Trp86, Phe295, Tyr337 and Phe338; some extended towards Ser203 and His447. These observations identify regions for follow-up testing but do not establish residue-specific interactions, inhibition or PAS selectivity [7,8].",
    )
    text = replace_once(
        text,
        "Ranking is internally consistent: the three best scorers (FLLHTTR −9.60; YLSLLQR −9.49; ALLLHRC −9.29) are separated from the weakest two (HLPLLHRCC −8.35; HVLLLRQCA −8.25) by more than 1 kcal/mol, well outside the per-peptide SD, while the middle of the table is a near-degenerate cluster (−8.88 to −9.29). Two caveats travel with this ranking: Vina scores of flexible 7–9-mers are sensitive to starting conformations, and scores for a PAS-only box say nothing about CAS-only or exosite binding; both are on the follow-up list.",
        "FLLHTTR, YLSLLQR and ALLLHRC had the most favourable reported scores, whereas HLPLLHRCC and HVLLLRQCA had the least favourable scores. The middle of the ranking was closely spaced. Vina scores for flexible peptides are sensitive to representation and starting conformation, and a PAS-centred search cannot assess alternative sites; candidate ordering should therefore be re-evaluated with independent conformers, flexible peptide docking and experimental measurements.",
    )

    text = replace_once(
        text,
        "The operational product of the screening stage is a prioritisation result: oral proteomes discard more than 99.7% of translated sORFs, and a BBB-first, metal-second, scavenger-low stack reduces 33,786 periodontitis-supported peptides to 12 (8 at the stricter cut). What the structure stage adds is the readout that makes the list actionable: every one of the twelve candidates can physically occupy the PAS–gorge interface of human AChE with plausible chemistry and Vina scores below −8 kcal/mol. A twelve-peptide list with poses is a project; a twelve-peptide list without poses was an inventory.",
        "The principal result is a prioritisation funnel. Exact proteome matching removed more than 99.7% of translated sORFs, and sequential BBB, neurotoxicity, metal-binding and chelator/scavenger filters reduced 33,786 periodontitis-associated peptides to 12 primary candidates. Docking supplied testable structural hypotheses for this shortlist, but it did not validate transport, metal coordination, AChE binding or toxicity.",
    )
    text = replace_once(
        text,
        "The PAS was chosen as the docking target for two documented reasons: it is the AChE surface that accelerates Aβ fibril assembly [4–6], and it borders the 344–361 Aβ residence patch identified by a microsecond simulation [9]. The docking result therefore positions the oral candidates on the exact surface where AChE–Aβ cross-talk is believed to begin. The cationic, aromatic, His-rich composition of the twelve peptides fits that surface: the PAS is an anionic, aromatic rim, and every candidate carries at least one Arg/Lys while eleven of twelve carry His, a residue that can simultaneously participate in PAS stacking networks and in later Cu/Fe/Zn coordination [27]. That dual use of His—surface anchoring and metal anchoring—is precisely the chemistry the CHEL-high / FRS-low filter was designed to enrich, and the docking stage shows it is spatially compatible with a disease-relevant AChE site.",
        "The PAS was selected because it participates in AChE-enhanced Aβ assembly [4–6] and borders the simulated 344–361 Aβ residence region [9]. The cationic, His-rich composition of the candidates is chemically compatible with an aromatic, charged gorge, and the generated poses provide hypotheses for testing whether the same residues that support metal coordination also influence AChE association. This compatibility should not be interpreted as evidence of binding, PAS selectivity or altered Aβ assembly.",
    )
    text = replace_once(
        text,
        "None of this is a binding constant. Vina’s scoring function is a fast approximation calibrated for enrichment, not affinity [35]; a single rigid receptor conformation was used; 4EY6’s missing loops (near residues 259–262 and 492–495) and its glycosylation state are not represented in the docking; no explicit water or metal ion was present; peptide protonation states were not sampled. The MD attempt (Section 2.11) exists precisely because we do not treat −9.60 kcal/mol as a measured free energy—it failed at pressure equilibration for the structural reasons above, and no trajectory is reported. Readers should carry one sentence forward: **the docking orders twelve candidates; it does not certify any of them.**",
        "Vina is a rapid scoring approximation for pose ranking rather than affinity measurement [34]. The analysis used one receptor conformation without unresolved loops, glycans, explicit water or metal ions, and peptide protonation microstates were not systematically sampled. The MD attempt failed during pressure equilibration (Section 2.10), so no dynamic-stability claim is made. The docking therefore orders hypotheses; it does not certify candidates.",
    )
    text = text.replace("(the BBB-positive short set is 83.95% 8–15 aa; Fig. 4)", "(83.95% of the BBB-positive short set was 8–15 aa)")
    text = replace_once(
        text,
        "Screening limitations are those of a single donor-level collection (specific donor counts documented in the source assembly but not reported as primary denominators here), exact-match proteomics, black-box predictors at fixed cut-offs, and peptide-level *P* values that ignore donor clustering. Structure-stage limitations add: a single receptor conformation without the unresolved loop segments of 4EY6; no glycans, no crystallographic waters, no metal ion in the box; Vina scoring without re-scoring by MM/GBSA (deferred); starting-conformation sensitivity of flexible peptides; and taxonomy—the MAG collection is a community oral metagenome [33], so calling the twelve sequences “*P. gingivalis* peptides” remains a taxonomy error until each sequence is assigned. Software versions/seeds for UniDL4BioPep, NTxPred2, mebipred, AnOxPePred, and the docking exhaustiveness/seed settings, are marked `AUTHOR_INPUT_NEEDED` for the submission version. GSE42872 is a six-sample melanoma microarray [34] and must not enter an AD contrast.",
        "The study is limited by a single source collection, exact-match proteome filtering, fixed classifier thresholds, unavailable donor-by-peptide data and exploratory peptide-level tests that ignore donor clustering. Archived records did not retain predictor versions and seeds, docking preparation software, exhaustiveness, run count or random seeds. The structure stage used one receptor conformation without unresolved loops, glycans, explicit waters or metal ions; flexible peptide conformers, protonation microstates and alternative binding sites were not systematically sampled. The community metagenome also does not support assignment of the candidates to *P. gingivalis* or another individual species [33]. Future validation should include taxonomic mapping, independent multi-conformer modelling, flexible peptide docking [36], explicit metal coordination, molecular dynamics with stable equilibration, relative-energy rescoring [42], and experimental assays. AlphaFold 3 may provide complementary complex hypotheses but cannot substitute for conformational sampling or experiments [41].",
    )

    text = text.replace("calls .", "calls.")
    text = text.replace("quorum sensing (12,674) .", "quorum sensing (12,674).")
    text = text.replace("16–30 aa .", "16–30 aa.")
    text = text.replace("| Model | Healthy n (%) | Periodontitis n (%) |", "| Model | Healthy *n* (%) | Periodontitis *n* (%) |")
    text = text.replace("| Stage | Rule | n |", "| Stage | Rule | *n* |")
    text = text.replace(
        "Composition columns are counted directly from the sequences. Vina scores are the author’s reported means ± SD; docking protocol, Section 2.10.",
        "**Note.** Composition columns were counted directly from the sequences. Scores are reported as mean ± SD from the archived docking output; docking protocol, Section 2.9.",
    )

    decl_start = text.index("## Declarations")
    text = text[:decl_start] + DECLARATIONS.rstrip() + "\n\n" + REFERENCE_BLOCK.rstrip() + "\n"

    # Final deterministic hygiene checks.
    forbidden = [
        "AUTHOR_INPUT_NEEDED",
        "ZZL-Zoro",
        "source-docs",
        "project’s",
        "project's",
        "Fig. ",
        "Section 4.5",
        "Sections 2.10–2.11",
        "GSE42872",
    ]
    for token in forbidden:
        if token in text:
            raise RuntimeError(f"Forbidden final-manuscript token remains: {token}")

    refs = re.findall(r"(?m)^(\d+)\. ", text[text.index("## References"):])
    if refs != [str(i) for i in range(1, 43)]:
        raise RuntimeError(f"Reference sequence invalid: {refs}")
    return text


def build_supplement() -> str:
    """Derive a clean English-only supplement from the audited bilingual tables."""
    source = SUPPLEMENT_SOURCE.read_text(encoding="utf-8")
    start = source.index("## Table S1.")
    lines = source[start:].splitlines()
    out = ["# Supplementary Tables", "", f"**Linked manuscript:** {TITLE}", ""]
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped == "---":
            out.append("")
            continue
        if stripped.startswith("## Table S"):
            english = stripped.split(" / 表 S", 1)[0]
            out.append(english.replace("## Table S", "## Supplementary Table S", 1))
            continue
        if stripped.startswith("Backgrounds / 背景:"):
            # Both S1 and S2 have stable audited denominators.
            if "30,557" in stripped:
                out.append("Background: healthy, 30,557; periodontitis, 32,754.")
            else:
                out.append("Background: healthy, 953; periodontitis, 1,032.")
            continue
        if stripped.startswith("Receptor / 受体:"):
            out.append(
                "Receptor: human AChE, PDB 4EY6 [8]; search box: 40 × 40 × 40 Å³ centred on the PAS; engine: AutoDock Vina 1.2.5 [34,35]."
            )
            continue
        if stripped.startswith("Interpretation boundary / 解读边界:"):
            english = stripped.split(" / 苦", 1)[0].split(" / 广", 1)[0]
            english = english.replace("Interpretation boundary / 解读边界: ", "**Note.** ")
            out.append(english)
            continue
        if stripped.startswith("Composition columns counted directly"):
            out.append(
                "**Note.** Composition columns were counted directly from the sequences. Pose contacts were inspected qualitatively at the PAS core (Tyr72, Asp74, Tyr124, Trp286 and Tyr341), gorge aromatics (Trp86, Phe295, Tyr337 and Phe338), and catalytic region (Ser203 and His447). Vina scores are pose-ranking outputs, not binding constants."
            )
            continue
        if stripped.startswith("*Shared reference list"):
            out.append("*References are listed in the main manuscript.*")
            continue
        if stripped.startswith("|"):
            cells = [cell.strip() for cell in stripped.strip("|").split("|")]
            cleaned = []
            for cell in cells:
                # Bilingual cells consistently use a spaced slash; biochemical
                # slashes such as Cu/Fe/Zn and F/Y/W have no surrounding spaces.
                if cell.startswith("CHEL-high / FRS-low"):
                    cleaned.append("CHEL-high / FRS-low")
                else:
                    cleaned.append(cell.split(" / ", 1)[0])
            out.append("| " + " | ".join(cleaned) + " |")
            continue
        out.append(stripped)

    text = "\n".join(out).rstrip() + "\n"
    text = text.replace("counts (P ≥ 0.8)", "counts (*P* ≥ 0.8)")
    text = text.replace("| Model | Healthy n (%) | Periodontitis n (%) |", "| Model | Healthy *n* (%) | Periodontitis *n* (%) |")
    text = text.replace("| Stage | Rule | n | Denominator basis |", "| Stage | Rule | *n* | Denominator basis |")
    if any("/ 表" in line or " / 健康" in line or "解读边界" in line for line in text.splitlines()):
        raise RuntimeError("Bilingual labels remain in English supplement")
    if text.count("## Supplementary Table S") != 5:
        raise RuntimeError("Expected five supplementary tables")
    return text


if __name__ == "__main__":
    OUTPUT.write_text(build(), encoding="utf-8")
    SUPPLEMENT_OUTPUT.write_text(build_supplement(), encoding="utf-8")
    print(OUTPUT)
    print(SUPPLEMENT_OUTPUT)
