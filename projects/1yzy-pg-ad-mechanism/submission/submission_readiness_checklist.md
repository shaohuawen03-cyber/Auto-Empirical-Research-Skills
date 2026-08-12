# Submission-readiness checklist / 投稿准备清单（v0.5）

Date: 2026-08-12  
Status: **TECHNICAL PACKAGE READY FOR AUTHOR REVIEW; ADMINISTRATIVE + PARTIAL TECHNICAL BLOCKERS REMAIN**

## A. Completed in this package / 本包已完成

- [x] Nine-stage reconstruction recorded (`../revision_v2/`), harmonised with the Light-skills branch spec.
- [x] Excluded-source containment documented (GSE42872) without deleting author files.
- [x] Author’s twelve candidate sequences and PAS docking results integrated (Tables 5 / S4).
- [x] English + Chinese masters and section-parallel bilingual draft rebuilt; DOCX packages built and audited (stdlib).
- [x] Aggregate arithmetic independently recomputed (`revision_v2/statistics_audit.json`, `all_checks_pass=true`).
- [x] All 43 references verified or status-flagged; two author-supplied citations corrected against PubMed/PDB; 43-DOI parity across EN/ZH/verified list.
- [x] Prohibited-claim and placeholder audits pass in both languages; consistency/structure/word-count/docx audits pass.
- [x] Evidence ledger, scope statement, ethics review, reviewer self-review and literature coverage written.
- [x] Bilingual cover letter, pre-submission enquiry, title page, highlights and journal-targeting notes prepared.
- [x] Attempted-MD failure reported with causes and remediation (Methods 2.11).

## B. Blocking author inputs before formal submission / 正式投稿前必须补齐

- [ ] Target journal selected; scope/APC/limits/AI-policy re-checked on the journal site.
- [ ] Positive response to the pre-submission enquiry.
- [ ] Author names, affiliations, ORCIDs, corresponding-author details, CRediT roles.
- [ ] Ethics approval/exemption wording; consent statement; funding; competing interests.
- [ ] Software versions/seeds: UniDL4BioPep, NTxPred2, mebipred, AnOxPePred.
- [ ] Docking parameters: exhaustiveness, run count, seeds, receptor/ligand preparation toolchain.
- [ ] The 8-of-12 strict-subset membership labels.
- [ ] Ref 23 (Frontiers 2026) author line confirmed; refs 31/42 full author lines confirmed; Crossmark/retraction screening for all 43 refs.
- [ ] Data/Code Availability and AI-use disclosure final approval.

## C. Scientific blockers (not fixable by editing) / 科学阻断项

- [ ] Experimental validation cascade (stopping rule unchanged).
- [ ] Production 100-ns MD after pressure-stability remediation.
- [ ] Donor-by-peptide matrix for donor-level inference.

## D. Final file-level checks immediately before upload / 上传前文件级检查

- [ ] Word revision marks/comments removed; DOCX re-rendered page-by-page by the author (no renderer in this environment).
- [ ] Title/author order identical across manuscript, portal, cover letter, title page.
- [ ] Word counts recounted after journal formatting.
- [ ] Figures meet journal dpi/font/colour-mode specs.
