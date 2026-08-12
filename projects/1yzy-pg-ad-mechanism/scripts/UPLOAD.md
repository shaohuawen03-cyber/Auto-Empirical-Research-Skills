# 本机文档如何进这个仓库（不要在 `E:\0writing\1yzy` 里 `git init`）

会话分支固定为 `arena/019ff371-auto-empirical-research-skills`。源稿在 Windows 的 `E:\0writing\1yzy`，Arena 沙箱读不到该盘，所以必须在你本机拷进本仓库后再 push。

## 为什么不要在 `1yzy` 目录单独 `git init`

`git init` 会在那个文件夹新建一个**空历史仓库**。本仓库已经是 `Auto-Empirical-Research-Skills`，历史、skills、catalog 都在这里。正确做法是：

1. 克隆（或打开已有克隆）本仓库
2. 检出 Arena 分支
3. 把 `E:\0writing\1yzy` 里的 docx/pdf **复制**到 `projects/1yzy-pg-ad-mechanism/source-docs/`
4. `git add` / `commit` / `push origin arena/019ff371-auto-empirical-research-skills`
5. 你在本地按质量打 tag

## Spyder / 本机终端：不要套一层 `powershell -File`，也不要反引号换行

Spyder 的 `(base) PS` 已经是 PowerShell。再写 `powershell -File ...` 加反引号换行，经常会吞掉输出，看起来像没执行。下面每一行单独回车。

先确认分支和源目录（应看到 `arena/019ff371-...` 和 6 个本地文件）：

```powershell
cd E:\0writing\Auto-Empirical-Research-Skills
git fetch origin
git checkout arena/019ff371-auto-empirical-research-skills
git pull origin arena/019ff371-auto-empirical-research-skills
git branch --show-current
dir E:\0writing\1yzy
dir .\projects\1yzy-pg-ad-mechanism
```

再复制、提交、推送（仍是一行一条，不要反引号）：

```powershell
New-Item -ItemType Directory -Force -Path .\projects\1yzy-pg-ad-mechanism\source-docs | Out-Null
Copy-Item -Path E:\0writing\1yzy\* -Destination .\projects\1yzy-pg-ad-mechanism\source-docs\ -Force
dir .\projects\1yzy-pg-ad-mechanism\source-docs
git add projects/1yzy-pg-ad-mechanism/source-docs
git status
git commit -m "docs(1yzy): ingest local source manuscripts from E:/0writing/1yzy"
git push origin arena/019ff371-auto-empirical-research-skills
```

也可以双击或直接运行 `.\projects\1yzy-pg-ad-mechanism\scripts\upload-local-docs.bat`（只负责复制和 `git add`，commit/push 仍要你自己回车确认）。

## 手敲等价命令

```powershell
# 若还没有克隆
git clone https://github.com/shaohuawen03-cyber/Auto-Empirical-Research-Skills.git
cd Auto-Empirical-Research-Skills

git fetch origin
git checkout arena/019ff371-auto-empirical-research-skills

New-Item -ItemType Directory -Force -Path .\projects\1yzy-pg-ad-mechanism\source-docs | Out-Null
Copy-Item -Path "E:\0writing\1yzy\*" -Destination ".\projects\1yzy-pg-ad-mechanism\source-docs\" -Force

git add projects/1yzy-pg-ad-mechanism/source-docs
git status
git commit -m "docs(1yzy): ingest local source manuscripts from E:\0writing\1yzy"
git push -u origin arena/019ff371-auto-empirical-research-skills
```

## 本地打 tag（你验收后再做）

```powershell
# 只存在于本地，方便存档
git tag -a 1yzy-manuscript-v0.1 -m "bilingual review draft + source-docs"

# 确认要同步到远程再执行
git push origin 1yzy-manuscript-v0.1
```

查看历史：

```powershell
git log --oneline -- projects/1yzy-pg-ad-mechanism
git tag -l "1yzy*"
```
