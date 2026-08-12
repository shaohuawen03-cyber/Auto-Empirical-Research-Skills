#Requires -Version 5.1
<#
.SYNOPSIS
  把本机 E:\0writing\1yzy 下的源文档拷进本仓库 projects/1yzy-pg-ad-mechanism/source-docs，
  检出 Arena 会话分支并推送。不要在 1yzy 目录单独 git init 成另一个仓库。

.USAGE
  # 在已有克隆里执行（推荐）
  powershell -ExecutionPolicy Bypass -File .\projects\1yzy-pg-ad-mechanism\scripts\upload-local-docs.ps1

  # 指定源目录 / 仓库根 / 远程
  powershell -ExecutionPolicy Bypass -File .\projects\1yzy-pg-ad-mechanism\scripts\upload-local-docs.ps1 `
    -SourceDir "E:\0writing\1yzy" `
    -RepoRoot "D:\code\Auto-Empirical-Research-Skills"
#>
param(
    [string]$SourceDir = "E:\0writing\1yzy",
    [string]$RepoRoot = "",
    [string]$RemoteUrl = "https://github.com/shaohuawen03-cyber/Auto-Empirical-Research-Skills.git",
    [string]$Branch = "arena/019ff371-auto-empirical-research-skills",
    [string]$DestRel = "projects\1yzy-pg-ad-mechanism\source-docs"
)

$ErrorActionPreference = "Stop"

function Assert-Cmd($Name) {
    if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
        throw "未找到命令: $Name。请先安装 Git for Windows，并确保 git 在 PATH 中。"
    }
}

Assert-Cmd git

if (-not (Test-Path -LiteralPath $SourceDir)) {
    throw "源目录不存在: $SourceDir"
}

if ([string]::IsNullOrWhiteSpace($RepoRoot)) {
    $here = Get-Location
    if (Test-Path -LiteralPath (Join-Path $here ".git")) {
        $RepoRoot = $here.Path
    } elseif ($PSScriptRoot) {
        $guess = Resolve-Path (Join-Path $PSScriptRoot "..\..\..") -ErrorAction SilentlyContinue
        if ($guess -and (Test-Path (Join-Path $guess ".git"))) {
            $RepoRoot = $guess.Path
        }
    }
}

if ([string]::IsNullOrWhiteSpace($RepoRoot) -or -not (Test-Path (Join-Path $RepoRoot ".git"))) {
    throw @"
未能定位本仓库根目录。请先克隆并进入仓库后再跑本脚本：

  git clone $RemoteUrl
  cd Auto-Empirical-Research-Skills
  git fetch origin
  git checkout $Branch
  powershell -ExecutionPolicy Bypass -File .\projects\1yzy-pg-ad-mechanism\scripts\upload-local-docs.ps1
"@
}

Set-Location -LiteralPath $RepoRoot

$current = (git rev-parse --abbrev-ref HEAD).Trim()
if ($current -ne $Branch) {
    Write-Host "当前分支是 $current，切换到 $Branch ..."
    git fetch origin
    git checkout $Branch
}

$dest = Join-Path $RepoRoot $DestRel
New-Item -ItemType Directory -Force -Path $dest | Out-Null

$expected = @(
    "GSE42872_代码方法.docx",
    "GSE42872_论文.docx",
    "乙酰胆碱酯酶-β-淀粉样肽复合物分子动力学模拟_中文翻译.docx",
    "材料与方法及结果_机制研究版.docx",
    "材料与方法及结果_机制研究版.pdf",
    "牙龈卟啉单胞菌肽与AD关联综述.docx"
)

Write-Host "从 $SourceDir 复制文档到 $dest"
$copied = @()
Get-ChildItem -LiteralPath $SourceDir -File | ForEach-Object {
    Copy-Item -LiteralPath $_.FullName -Destination (Join-Path $dest $_.Name) -Force
    $copied += $_.Name
    Write-Host ("  + {0}  ({1:N0} bytes)" -f $_.Name, $_.Length)
}

if ($copied.Count -eq 0) {
    throw "源目录里没有文件可复制。"
}

$missing = @()
foreach ($name in $expected) {
    $hit = $copied | Where-Object { $_ -like ($name -replace '中文翻译','*') -or $_ -eq $name }
    if (-not $hit) {
        # 文件名可能被 PowerShell 截断，用模糊匹配
        $fuzzy = $copied | Where-Object { $_.StartsWith($name.Substring(0, [Math]::Min(8, $name.Length))) }
        if (-not $fuzzy) { $missing += $name }
    }
}
if ($missing.Count -gt 0) {
    Write-Warning ("下列预期文件未精确匹配到，请人工核对: " + ($missing -join "; "))
}

# 清单，便于后续核对
$manifest = Join-Path $dest "MANIFEST.txt"
@(
    "uploaded_at_utc=$(Get-Date -Format o)"
    "source=$SourceDir"
    "branch=$Branch"
    "files:"
) + ($copied | ForEach-Object { "  $_" }) | Set-Content -LiteralPath $manifest -Encoding UTF8

git add -- $DestRel
$status = git status --porcelain -- $DestRel
if (-not $status) {
    Write-Host "没有新的文档变更需要提交。"
    exit 0
}

git commit -m @"
docs(1yzy): ingest local source manuscripts from E:\0writing\1yzy

Add author-held Word/PDF drafts that the bilingual SCI review is
anchored to. Binary sources stay under source-docs/ for versioned
archiving; the derived manuscript lives in manuscript/.
"@

Write-Host "推送到 origin/$Branch ..."
git push -u origin $Branch

Write-Host ""
Write-Host "完成。本地打 tag 示例（确认质量后再执行）："
Write-Host "  git tag -a 1yzy-v0.1 -m `"source-docs ingested`""
Write-Host "  git push origin 1yzy-v0.1"
Write-Host "或只在本地打 tag、暂不推送："
Write-Host "  git tag -a 1yzy-local-v0.1 -m `"local archive`""
