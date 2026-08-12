# 每次生成结束后：同步代码（本机一行一条，Spyder / PowerShell 均可）

> 当前会话分支：`arena/019ff3f9-auto-empirical-research-skills`（2026-08-12 起，v0.4 主稿）  
> 旧分支 `arena/019ff371-auto-empirical-research-skills`（v0.1–v0.3）已归档，不要再拉它。

## 仓库已在 `E:\0writing\Auto-Empirical-Research-Skills` 时（不要重新 clone，只 pull）

```powershell
cd E:\0writing\Auto-Empirical-Research-Skills
git fetch origin
git checkout arena/019ff3f9-auto-empirical-research-skills
git pull origin arena/019ff3f9-auto-empirical-research-skills
git log -1 --oneline
dir .\projects\1yzy-pg-ad-mechanism\manuscript
```

## 还没有克隆过时

```powershell
cd E:\0writing
git clone https://github.com/shaohuawen03-cyber/Auto-Empirical-Research-Skills.git
cd Auto-Empirical-Research-Skills
git checkout arena/019ff3f9-auto-empirical-research-skills
```

## 若 HTTPS 又 403，换 SSH（沿用 Light-skills 那把钥匙，已配过可跳过 `git config`）

```powershell
git remote set-url origin ssh://git@ssh.github.com:443/shaohuawen03-cyber/Auto-Empirical-Research-Skills.git
git pull origin arena/019ff3f9-auto-empirical-research-skills
```

## 本地改过文件、想先保住再拉

```powershell
cd E:\0writing\Auto-Empirical-Research-Skills
git status
git stash push -m "local-notes"
git pull origin arena/019ff3f9-auto-empirical-research-skills
git stash pop
```

## 关键路径（v0.5 起）

| 内容 | 路径 |
| --- | --- |
| **版本记录与恢复方法** | `projects\1yzy-pg-ad-mechanism\VERSIONS.md`（tag 命名 `1yzy-manuscript-vX.Y`） |
| 英文主稿（投稿用） | `projects\1yzy-pg-ad-mechanism\manuscript\manuscript_en.md` |
| 中文主稿 | `projects\1yzy-pg-ad-mechanism\manuscript\manuscript_zh.md` |
| 双语主稿 | `projects\1yzy-pg-ad-mechanism\manuscript\manuscript_bilingual.md/.docx` |
| 双语补充表 | `projects\1yzy-pg-ad-mechanism\manuscript\supplementary_tables_bilingual.md/.docx` |
| 九阶段记录 | `projects\1yzy-pg-ad-mechanism\revision_v2\` |
| 质检汇总 | `projects\1yzy-pg-ad-mechanism\quality_reports\quality_summary.md` |
| 投稿包 | `projects\1yzy-pg-ad-mechanism\submission\` |
| 本机上传源稿 | `scripts\UPLOAD.md` |

## 版本 tag 操作（每次新版）

```powershell
git tag -l "1yzy-manuscript-*"
git tag -a 1yzy-manuscript-vX.Y -m "1yzy manuscript vX.Y: <说明>"
git push origin 1yzy-manuscript-vX.Y
```
