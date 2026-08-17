# v0.6 同步与版本管理

> 当前唯一工作分支：`arena/01a00dab-auto-empirical-research-skills`
>
> 当前投稿版本：`1yzy-manuscript-v0.6`
>
> 主稿：`projects\1yzy-pg-ad-mechanism\manuscript\manuscript_sci_final.docx`
>
> 原则：先保护本地修改，只做 fast-forward；不要 `reset --hard`，不要再拉旧的 `arena/019ff3f9-...` 分支。

## A. 已有仓库：第一次切换到 v0.6 分支

在 PowerShell 中逐行运行：

```powershell
cd E:\0writing\Auto-Empirical-Research-Skills

# 1. 先看本地是否有未保存修改
git status --short

# 2. 若上一步有输出，先提交；不准备提交时可暂存
# git add -A
# git commit -m "Save local work before v0.6 sync"
# 或：git stash push --include-untracked -m "before-v0.6-sync"

# 3. 获取本次会话的固定分支与版本标签
git fetch --prune --tags origin
git switch --track -c arena/01a00dab-auto-empirical-research-skills origin/arena/01a00dab-auto-empirical-research-skills

# 如果提示本地分支已经存在，改用：
# git switch arena/01a00dab-auto-empirical-research-skills

# 4. 只允许快进，避免覆盖本地历史
git pull --ff-only origin arena/01a00dab-auto-empirical-research-skills

# 5. 核对版本标签、提交和文件
git describe --tags --always
git log -3 --oneline --decorate
git merge-base --is-ancestor 1yzy-manuscript-v0.6 HEAD
if ($LASTEXITCODE -ne 0) { throw "当前分支不包含 v0.6，停止使用" }

dir .\projects\1yzy-pg-ad-mechanism\manuscript\*sci_final*
```

如之前用了 stash，同步完成后先检查，再恢复：

```powershell
git stash list
git stash show --stat 'stash@{0}'
# 确认无冲突风险后才执行：
git stash pop
```

## B. 以后每次一键同步

仓库已同步到本版本后，可以运行随仓库提供的安全脚本：

```powershell
cd E:\0writing\Auto-Empirical-Research-Skills
powershell -ExecutionPolicy Bypass -File .\projects\1yzy-pg-ad-mechanism\scripts\sync_sci_v06.ps1
```

如果本地有修改并希望脚本先代为 stash：

```powershell
powershell -ExecutionPolicy Bypass -File .\projects\1yzy-pg-ad-mechanism\scripts\sync_sci_v06.ps1 -StashLocalChanges
```

脚本会执行以下保护：

1. 拒绝静默覆盖未提交修改；
2. `fetch --prune --tags`；
3. 固定在 `arena/01a00dab-auto-empirical-research-skills`；
4. 只执行 `pull --ff-only`；
5. 验证 `1yzy-manuscript-v0.6` 是当前 HEAD 的祖先；
6. 对主稿、补充表和审计报告执行 SHA-256 校验；
7. stash 不会自动 pop，避免同步后冲突。

## C. 尚未 clone

```powershell
cd E:\0writing
git clone --branch arena/01a00dab-auto-empirical-research-skills --single-branch https://github.com/shaohuawen03-cyber/Auto-Empirical-Research-Skills.git
cd .\Auto-Empirical-Research-Skills
git fetch --tags origin
git describe --tags --always
```

若 HTTPS 返回 403，可切换到已经配置过的 SSH 443：

```powershell
git remote set-url origin ssh://git@ssh.github.com:443/shaohuawen03-cyber/Auto-Empirical-Research-Skills.git
git fetch --prune --tags origin
git pull --ff-only origin arena/01a00dab-auto-empirical-research-skills
```

## D. v0.6 文件与校验

| 内容 | 路径 |
| --- | --- |
| SCI 英文主稿 | `projects\1yzy-pg-ad-mechanism\manuscript\manuscript_sci_final.docx` |
| SCI 英文补充表 | `projects\1yzy-pg-ad-mechanism\manuscript\supplementary_tables_sci_final.docx` |
| 可追踪文本源 | `manuscript_sci_final.md`、`supplementary_tables_sci_final.md` |
| 版本记录 | `projects\1yzy-pg-ad-mechanism\VERSIONS.md` |
| 最终审计 | `projects\1yzy-pg-ad-mechanism\quality_reports\sci_final_audit.json` |
| SHA-256 | `projects\1yzy-pg-ad-mechanism\SCI_FINAL_SHA256SUMS.txt` |

手动执行 SHA-256 校验：

```powershell
cd E:\0writing\Auto-Empirical-Research-Skills\projects\1yzy-pg-ad-mechanism
Get-Content .\SCI_FINAL_SHA256SUMS.txt | ForEach-Object {
    if ($_ -match '^([0-9a-fA-F]{64})  (.+)$') {
        $expected = $Matches[1].ToLower()
        $file = $Matches[2]
        $actual = (Get-FileHash -Algorithm SHA256 -LiteralPath $file).Hash.ToLower()
        if ($actual -ne $expected) { throw "SHA-256 校验失败: $file" }
        Write-Host "PASS $file"
    }
}
```

## E. 新版本发布规则（维护者使用）

每个可投稿版本必须同时完成：

```powershell
# 示例：发布下一版 v0.7；不要覆盖或移动已有 v0.6 tag
git status --short
git add .\projects\1yzy-pg-ad-mechanism
git commit -m "Prepare 1yzy manuscript v0.7"
git tag -a 1yzy-manuscript-v0.7 -m "1yzy manuscript v0.7: <变更摘要>"
git push origin arena/01a00dab-auto-empirical-research-skills
git push origin 1yzy-manuscript-v0.7
```

版本纪律：

- 已发布 tag 永不移动、永不复用；修订必须递增版本号。
- `VERSIONS.md` 必须与 DOCX、Markdown、审计报告和校验文件同批更新。
- 投稿时优先记录 tag；如分支后续继续更新，仍可用 `git show 1yzy-manuscript-v0.6` 恢复本版。
- 不要在含未提交修改时切分支或 pull。
