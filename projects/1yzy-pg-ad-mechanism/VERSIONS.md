# 版本记录 / Version Log（1yzy-pg-ad-mechanism）

> 规则：每个主稿版本一行记录；每个投稿级版本打 annotated tag（命名 `1yzy-manuscript-vX.Y`）；
> 本文件随版本更新，是恢复任何历史版本的唯一索引。

## 版本总览 / Overview

| 版本 | 日期 | 主稿文件 | 分支 | Commit | Tag | 状态 |
| --- | --- | --- | --- | --- | --- | --- |
| v0.1 | 2026-08-12 | （已废弃，未留主文件） | `arena/019ff371-auto-empirical-research-skills` | 早于 `bc03c0a`（浅克隆未含） | — | ❌ 不要投稿：误以 GSE42872 与 AChE–Aβ 轨迹为中心 |
| v0.2 | 2026-08-12 | `manuscript/bilingual-sci-review.md` | 同上 | 早于 `bc03c0a`（浅克隆未含） | — | 📦 档案：双语夹写稿，纠正 v0.1 错误 |
| v0.3 | 2026-08-12 | `manuscript/sci_v03_en.md` | 同上 | `bc03c0a` | — | 📦 档案：英文 IMRaD 重写（Nature-skills），"未做对接"阶段 |
| v0.4 | 2026-08-12 | `manuscript/sci_v04_en.md` | `arena/019ff3f9-auto-empirical-research-skills` | `99dd684` | — | 📦 档案：引言扩写 + 并入序列与 PAS 对接 |
| v0.5 | 2026-08-12 | `manuscript/manuscript_en.md` + `_zh.md` + `manuscript_bilingual.md/.docx` | `arena/019ff3f9-auto-empirical-research-skills` | `d894dfb` | `1yzy-manuscript-v0.5` | 📦 双语内容档案（Light-skills 九阶段规格） |
| **v0.6** | **2026-08-17** | `manuscript/manuscript_sci_final.md/.docx` + `supplementary_tables_sci_final.md/.docx` | `arena/01a00dab-auto-empirical-research-skills` | 本次提交 | `1yzy-manuscript-v0.6` | ✅ **当前 SCI 排版终稿**（三线表、42 条均已引用文献、审计 PASS） |

## 各版详情 / Details

### v0.1 — 废弃
- 写在本地工具二进制入库之前；错误地把 GSE42872（黑色素瘤）与发表的 AChE–Aβ 轨迹当成 AD 结果。
- 仅保留教训，不保留文件；GSE42872 材料的排除记录见 `evidence/excluded_source_record.md`。

### v0.2 — 双语档案
- `manuscript/bilingual-sci-review.md`：中英对照机制稿；首次声明"对接/MD/湿实验不在本阶段"。
- 证据骨架 = 作者《材料与方法及结果_机制研究版》。

### v0.3 — 英文 IMRaD（commit `bc03c0a`，分支 `arena/019ff371-…`）
- 单语英文稿 + 供体级统计口径（独立单位 = 供体 24 vs 26）+ 矢量图 fig1–fig4。
- 15 条文献；12 条序列当时缺失（`AUTHOR_INPUT_NEEDED`）。

### v0.4 — 引言扩写 + 对接（commit `99dd684`，分支 `arena/019ff3f9-…`）
- 引言扩为六小节（含 tau26–44/Cu(II) 外源毒肽模板）；并入作者十二条序列与 4EY6 PAS 聚焦 Vina 对接（表5、图5）；
- MD 尝试如实报告为排除；文献 15 → 43（两处引用纠错：Di Natale 2018 DOI/PMID、Perini 2019 期刊）。

### v0.5 — 投稿级双语包（commit `d894dfb`，tag `1yzy-manuscript-v0.5`）
- Light-skills 九阶段规格：双语主稿 + 双语补充表 S1–S5 + DOCX（标准库构建，包审计 PASS）；
- 确定性审计全 PASS（数值一致 / 8 节结构 / 43-DOI 平价 / DOCX 包）；统计独立复算 `all_checks_pass=true`；
- 证据台账（16 条）、诚信边界 12 条、伦理审查、模拟审稿自审、文献覆盖声明；
- 双语投稿六件套 + 就绪清单；SHA256 校验与仓库清单。
- 结论口径：可交责任作者审阅与预投稿询问；未达立即正式投稿（行政项 + 技术参数 + 实验验证阻断）。

### v0.6 — 英文 SCI 排版终稿（2026-08-17）
- 新建匿名英文主稿与英文补充表 DOCX；A4、Times New Roman、双倍行距、连续行号、页码、Vancouver 格式。
- 主稿 5 个表、补充材料 5 个表全部使用真正三线表：仅表顶线、表头分隔线、表底线，无竖线、无底纹。
- 删除工作流说明、历史排除材料、待办占位符和未被引用的黑色素瘤文献；将缺失运行参数改写为透明的可重复性限制，不虚构方法参数。
- 参考文献收敛为正文实际引用的 42 条，全部含 DOI；核实并修正 2026 Frontiers 作者行、van Heesch 2019 页码/作者行、Belstrøm 2021 作者行。
- `quality_reports/sci_final_audit.json`：内容、引用全集、DOCX 包、匿名元数据、行号/页码及 10 个三线表全部 PASS。

## 修订记录 / Patch notes（v0.5 之后）

### 2026-08-17 修订（无新 tag，仍在 v0.5 框架内）
- 删除主稿标题、文章类型声明、正文结论章节（正文直接到参考文献）；
- 隐藏具体供体数量（不提 24/26，仅保留 296 MAG）；
- 英文/中文摘要按高分 SCI 格式（四要素明确）；引言按 ZZL-Zoro 证据审查标准扩充系统化框架段落；
- MD 方法描述已在 2.11 完整呈现（无引用非正式仓库，不补充未完成结果）；
- 图表：fig5 增加可编辑 SVG（无标题、无页眉页脚页码），三线表格式保留；
- 保留所有 `AUTHOR_INPUT_NEEDED` 标记、科学诚实边界与版本标签 `1yzy-manuscript-v0.5`。

## 恢复方法 / How to restore any version

```powershell
# 列出所有版本 tag
git tag -l "1yzy-manuscript-*"

# 只读查看当前投稿 tag（不改动当前分支）
git show 1yzy-manuscript-v0.6 --stat

# 以 detached HEAD 只读恢复/对比 v0.6（不会创建或移动分支）
git switch --detach 1yzy-manuscript-v0.6

# 回到当前工作分支
git switch arena/01a00dab-auto-empirical-research-skills

# 查看旧分支（v0.1–v0.3 所在）
git fetch origin arena/019ff371-auto-empirical-research-skills
git log --oneline FETCH_HEAD
```

## 打 tag 的标准操作 / Tagging SOP（每次新版都用）

```powershell
# 1) 在仓库根目录确认最新提交
cd E:\0writing\Auto-Empirical-Research-Skills
git log -1 --oneline

# 2) 打 annotated tag（把 vX.Y 换成实际版本）
git tag -a 1yzy-manuscript-vX.Y -m "1yzy manuscript vX.Y: <一句话描述>"

# 3) 推送 tag 到 GitHub
git push origin 1yzy-manuscript-vX.Y

# 4) 核对远端
git ls-remote --tags origin
```
