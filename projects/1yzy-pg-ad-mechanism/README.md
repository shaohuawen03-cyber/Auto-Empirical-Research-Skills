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

## 写作边界（请先读）

沙箱里**没有** `材料与方法及结果_机制研究版` 的正文与数字。本稿把该文件的**体例**（方法 → 结果 → 机制解释）作为骨架，证据只引用已核实的公开文献与 GEO 记录。作者本机数字、图、代码灌入 `source-docs/` 后，应用那些原始结果替换第 3 节中的“文献重建”段落，而不是把重建值写成自己的实验。

GSE42872 在 GEO 中是黑色素瘤维莫非尼实验，见 `source-docs/README.md`。

## Git

- 工作分支：`arena/019ff371-auto-empirical-research-skills`
- 上传源稿：见 `scripts/UPLOAD.md`
- 本地 tag：你看过 `manuscript/bilingual-sci-review.md` 后再打，例如 `1yzy-manuscript-v0.1`
