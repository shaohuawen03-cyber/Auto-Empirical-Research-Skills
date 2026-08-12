# 牙龈卟啉单胞菌肽–AChE–Aβ 机制综述（1yzy）

本目录是 Arena 会话分支上的**独立研究文件夹**，不改动仓库 skills 目录。

## 目录（v0.5 投稿包，与 Light-skills `arena/019ff377-light-skills` 规格对齐）

```
projects/1yzy-pg-ad-mechanism/
  README.md
  VERSIONS.md                     # ★ 版本记录：v0.1–v0.5 + tag + 恢复方法
  SHA256SUMS.txt                  # source-docs 哈希
  ARTIFACT_SHA256SUMS.txt         # 产物哈希
  manuscript/
    manuscript_en.md              # 英文主稿（投稿用，8 节，43 条文献）
    manuscript_zh.md              # 中文主稿（逐节对应）
    manuscript_bilingual.md/.docx # 分节对照双语稿（脚本重建）
    supplementary_tables_bilingual.md/.docx   # 补充表 S1–S5
    references.bib                # BibTeX（43 条手稿文献的文档化超集）
    figures/                      # fig1–fig5（PDF 母版 + PNG 预览）
    sci_v04_en.md / sci_v03_en.md / bilingual-sci-review.md   # 历史版本存档
  references/verified_references.md   # 43 条核验状态（含两处纠错）
  evidence/                       # 来源范围、主张–证据台账、排除材料记录
  revision_v2/                    # 九阶段记录 01–09 + statistics_audit.json
  quality_reports/                # 审计 JSON + 质量汇总 + 伦理/自审/文献覆盖
  submission/                     # 双语投稿信/询问/标题页/亮点/选刊/就绪清单
  pipeline/                       # v0.3、v0.4 技能运行记录（历史）
  scripts/                        # 审计/构建/绘图脚本（Python 标准库）
  source-docs/                    # 作者原始 docx/pdf
```

## 使用了哪些 AERS 技能

按根目录 `SKILL.md` 路由，只加载了任务相关 skill，没有通读 1151 条目录：

| 阶段 | Skill |
| --- | --- |
| 路由 | 仓库根 `SKILL.md` |
| 综述结构 | `skills/36-taoyunudt-literature-review-skill`（五步法：检索–筛选–争议/空白–主题组织–写作） |
| 报告规范 | `skills/52-keemanxp-slr-prisma`（PRISMA 2020 条目映射；本文是机制导向叙事综述，不是 meta-analysis） |
| 英文稿 | `skills/04-K-Dense-AI-claude-scientific-writer/scientific-writing` 与 `skills/03-K-Dense-AI-claude-scientific-skills/scientific-writing`（IMRAD、整段散文、图表） |
| 引用核验（v0.4 新增） | `skills/04-K-Dense-AI-claude-scientific-writer/citation-management`（PubMed/PDB 逐条比对，见 `pipeline/01_skill_run_v04.md`） |
| 中文降套话 | `skills/48-copaper-ai-chinese-de-aigc`（少四字套话、少段首“此外/因此”、断言降级） |

## 当前主稿（投稿用 v0.5）

- **英文主稿**：`manuscript/manuscript_en.md`；**中文主稿**：`manuscript/manuscript_zh.md`；**双语对照**：`manuscript/manuscript_bilingual.md/.docx`
- 九阶段记录：`revision_v2/01–09`；质检汇总：`quality_reports/quality_summary.md`（当前确定性审计全部 PASS）
- 投稿包：`submission/`（双语六件套 + 就绪清单）；选刊决定权归作者
- v0.4 及更早（`sci_v04_en.md` 等）仅作历史存档，不要投稿

### v0.5 相对 v0.4 的变化（按 Light-skills 九阶段规格重构）

1. 中英双语完整稿 + 分节对照双语稿 + 双语补充表（S1–S5），DOCX 用标准库脚本构建并通过包审计。
2. 新增确定性审计链（`scripts/audit_suite_v05.py`）：数值一致、禁用主张、43 条文献序列、DOI 集合平价（EN/ZH/核验表一致；BibTeX 为文档化超集）、8 节结构、DOCX 包完整性；全部 PASS。
3. 统计独立复算（`revision_v2/statistics_audit.json`，`all_checks_pass=true`；记录 48.25/51.75 的截断舍入口径）。
4. 证据台账与诚信边界：主张–证据台账 16 条；诚信边界扩至 12 条（新增对接与 MD 两条）；GSE42872 排除记录。
5. 模拟审稿自审、科研伦理审查、文献覆盖声明、投稿就绪清单。

### v0.4 新增内容速览

1. 引言六小节：AD 与 AChE 的非经典 PAS 功能 → 牙周炎–AD 轴（菌/蛋白酶/囊泡之外缺肽清单）→ 金属假说与载体问题 → 外源短肽神经毒模板（tau26–44/Cu(II)、curli 交叉播种）→ sORF 与蛋白质组支持筛选 → 本研究目标与边界。
2. 结果 3.7 + 方法 2.10–2.11：12 条主候选对 4EY6 PAS 的 Vina 1.2.5 聚焦对接（40×40×40 Å³，−8.25…−9.60 kcal/mol，跨 PAS–峡部结合模式）；GROMACS 100 ns 尝试因 Z 轴压力不稳定被如实报告并排除。
3. 引用从 15 条扩到 43 条；作者文献表两处错误已纠正（Di Natale 2018 的 DOI/PMID；Perini 2019 实为 Int J Biol Macromol 而非 Sci Rep），4EY6 补上 Cheung 2012 原始文献。

源稿已在 `source-docs/`。GSE42872 是黑色素瘤维莫非尼再分析，不是 AD 结果。AChE–Aβ 中译是下一阶段对接位点的文献，不是本阶段结果。

## Git

- 工作分支：`arena/019ff3f9-auto-empirical-research-skills`（当前会话；旧分支 `arena/019ff371-…` 为 v0.1–v0.3 存档）
- **版本记录与 tag**：`VERSIONS.md`（tag 命名 `1yzy-manuscript-vX.Y`，恢复方法在内）
- **拉我推上去的更新**：`scripts/SYNC.md`（每次生成后都用这个，不要重新 clone）
- 上传源稿：`scripts/UPLOAD.md`
- 当前 tag：`1yzy-manuscript-v0.5`
