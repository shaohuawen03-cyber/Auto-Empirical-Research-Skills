# 牙龈卟啉单胞菌肽–AChE–Aβ 机制综述（1yzy）

本目录是 Arena 会话分支上的**独立研究文件夹**，不改动仓库 skills 目录。

## 目录

```
projects/1yzy-pg-ad-mechanism/
  README.md
  scripts/upload-local-docs.ps1   # 本机 E:\0writing\1yzy → source-docs → push
  scripts/UPLOAD.md
  source-docs/                    # 作者原始 docx/pdf（需本机脚本灌入）
  manuscript/
    bilingual-sci-review.md       # 中英对照 SCI 综述（主交付）
    references.bib
    figures/
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

## 当前主稿（投稿用 v0.4）

- **英文 SCI 主稿**：`manuscript/sci_v04_en.md`（v0.3 的引言大幅扩写为六小节；并入作者 12 条主候选序列、PAS 聚焦 Vina 对接结果与后续机制方案；外源毒性肽文献框架（tau26–44/Cu(II) 等）已核验并并入引言）
- v0.3 主稿 `manuscript/sci_v03_en.md` 降为档案（“未做对接”阶段的历史版本）
- 流程记录：`pipeline/00_skill_run.md`（v0.3）+ `pipeline/01_skill_run_v04.md`（v0.4 技能清单、引用纠错日志、统计审查）
- 中文摘要在主稿文内；投稿信 / Highlights：`submission/`
- 矢量图：`manuscript/figures/fig1_design.pdf` … `fig4_bbb_length.pdf`，v0.4 新增 `fig5_docking_scores.pdf`（脚本 `scripts/fig5_docking_scores.py`）
- v0.2 双语夹写稿仅作档案：`manuscript/bilingual-sci-review.md`
- v0.1 不要投稿

### v0.4 新增内容速览

1. 引言六小节：AD 与 AChE 的非经典 PAS 功能 → 牙周炎–AD 轴（菌/蛋白酶/囊泡之外缺肽清单）→ 金属假说与载体问题 → 外源短肽神经毒模板（tau26–44/Cu(II)、curli 交叉播种）→ sORF 与蛋白质组支持筛选 → 本研究目标与边界。
2. 结果 3.7 + 方法 2.10–2.11：12 条主候选对 4EY6 PAS 的 Vina 1.2.5 聚焦对接（40×40×40 Å³，−8.25…−9.60 kcal/mol，跨 PAS–峡部结合模式）；GROMACS 100 ns 尝试因 Z 轴压力不稳定被如实报告并排除。
3. 引用从 15 条扩到 43 条；作者文献表两处错误已纠正（Di Natale 2018 的 DOI/PMID；Perini 2019 实为 Int J Biol Macromol 而非 Sci Rep），4EY6 补上 Cheung 2012 原始文献。

源稿已在 `source-docs/`。GSE42872 是黑色素瘤维莫非尼再分析，不是 AD 结果。AChE–Aβ 中译是下一阶段对接位点的文献，不是本阶段结果。

## Git

- 工作分支：`arena/019ff371-auto-empirical-research-skills`
- **拉我推上去的更新**：`scripts/SYNC.md`（每次生成后都用这个，不要重新 clone）
- 上传源稿：`scripts/UPLOAD.md`
- 本地 tag 示例：`1yzy-manuscript-v0.2`
