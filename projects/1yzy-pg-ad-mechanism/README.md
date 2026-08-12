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
| 中文降套话 | `skills/48-copaper-ai-chinese-de-aigc`（少四字套话、少段首“此外/因此”、断言降级） |

## 当前主稿

- **v0.2（以你的机制稿数字为准）**：`manuscript/bilingual-sci-review.md`
- 漏斗图：`manuscript/figures/fig5_screening_funnel.png`
- v0.1 是源稿入库前的误构（GSE42872 / 已发表 AChE–Aβ MD），不要投稿；只留在 git 历史里

源稿已在 `source-docs/`。GSE42872 是黑色素瘤维莫非尼再分析，不是 AD 结果。AChE–Aβ 中译是下一阶段对接位点的文献，不是本阶段结果。

## Git

- 工作分支：`arena/019ff371-auto-empirical-research-skills`
- **拉我推上去的更新**：`scripts/SYNC.md`（每次生成后都用这个，不要重新 clone）
- 上传源稿：`scripts/UPLOAD.md`
- 本地 tag 示例：`1yzy-manuscript-v0.2`
