# Reviewer-style self-review / 模拟审稿意见（v0.5）

Date: 2026-08-12. Written adversarially; each anticipated objection is paired with the manuscript’s current answer.

**R1. “Docking without MD or experiment is weak.”**
Answered in §2.11 and §4.2: the MD attempt is reported with failure cause and remediation; docking is framed as ranking, not certification; the roadmap (§4.5) and stopping rule bound the claim. The paper does not overstate.

**R2. “Vina on flexible 7–9-mers is noisy; one box, one receptor conformation.”**
Conceded in §4.2/§4.4 (missing loops 259–262/492–495, no glycans/waters/metal, no protonation sampling, no MM/GBSA rescoring). The within-set design (12 closely related ligands) is the mitigating argument; FlexPepDocking is the stated upgrade.

**R3. “Peptide-level statistics ignore donors.”**
Stated in Methods 2.1/2.8 and every results paragraph: donors are the independent unit; peptide 2×2 tests are exploratory; no donor-level matrix was deposited.

**R4. “Why PAS and not CAS or the 344–361 patch directly?”**
§1.1/§1.6: PAS is the documented Aβ-accelerating surface and borders the residence patch; CAS and 344–361 are explicitly on the follow-up panel (§4.5), and poses already reaching Ser203/His447 are flagged.

**R5. “The taxonomy claim is tempting — these must be *P. gingivalis* peptides.”**
Refused three times (§1.6, §4.4, quality summary boundary 6): community metagenome, assignment not claimed.

**R6. “The introduction cites a 2026 Frontiers record that cannot yet be fully verified.”**
Flagged in-line (ref 23) and in `references/verified_references.md`; author must confirm before submission.

**R7. “Where are the per-peptide interaction tables and the 8-peptide subset?”**
`AUTHOR_INPUT_NEEDED`; disclosed in Methods and the readiness checklist rather than invented.

**Verdict as editor:** the package is internally consistent and honestly bounded; it is a computational triage
+ hypothesis-generating paper, and should be pitched as such to a methods-tolerant venue.
