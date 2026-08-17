#requires -Version 5.1
<#
.SYNOPSIS
Safely synchronise the v0.6 SCI manuscript from GitHub without discarding local work.

.EXAMPLE
powershell -ExecutionPolicy Bypass -File .\sync_sci_v06.ps1

.EXAMPLE
powershell -ExecutionPolicy Bypass -File .\sync_sci_v06.ps1 -RepoPath "D:\research\Auto-Empirical-Research-Skills"
#>
[CmdletBinding()]
param(
    [string]$RepoPath = "E:\0writing\Auto-Empirical-Research-Skills",
    [switch]$StashLocalChanges
)

$ErrorActionPreference = "Stop"
$Branch = "arena/01a00dab-auto-empirical-research-skills"
$VersionTag = "1yzy-manuscript-v0.6"
$Project = "projects/1yzy-pg-ad-mechanism"
$ChecksumFile = Join-Path $Project "SCI_FINAL_SHA256SUMS.txt"
$StashCreated = $false

function Invoke-Git {
    param([Parameter(ValueFromRemainingArguments = $true)][string[]]$Arguments)
    & git @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "git $($Arguments -join ' ') failed with exit code $LASTEXITCODE"
    }
}

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw "Git is not installed or is not available on PATH."
}
if (-not (Test-Path -LiteralPath (Join-Path $RepoPath ".git"))) {
    throw "Repository not found at '$RepoPath'. Clone it first using the command in scripts/SYNC.md."
}

Push-Location $RepoPath
try {
    $origin = (& git remote get-url origin).Trim()
    if ($LASTEXITCODE -ne 0 -or -not $origin) {
        throw "The repository has no usable 'origin' remote."
    }
    Write-Host "Repository: $RepoPath"
    Write-Host "Origin:     $origin"
    Write-Host "Branch:     $Branch"
    Write-Host "Version:    $VersionTag"

    $dirty = @(& git status --porcelain)
    if ($dirty.Count -gt 0) {
        if (-not $StashLocalChanges) {
            Write-Host "Local changes detected:" -ForegroundColor Yellow
            $dirty | ForEach-Object { Write-Host "  $_" }
            throw "Sync stopped to protect local work. Commit it, or rerun with -StashLocalChanges."
        }
        $stamp = Get-Date -Format "yyyyMMdd-HHmmss"
        Invoke-Git stash push --include-untracked -m "pre-sync-$VersionTag-$stamp"
        $StashCreated = $true
        Write-Host "Local changes were stashed and will NOT be popped automatically." -ForegroundColor Yellow
    }

    Invoke-Git fetch --prune --tags origin

    & git show-ref --verify --quiet "refs/remotes/origin/$Branch"
    if ($LASTEXITCODE -ne 0) {
        throw "Remote branch origin/$Branch does not exist. Check GitHub connectivity and the branch name."
    }

    & git show-ref --verify --quiet "refs/heads/$Branch"
    if ($LASTEXITCODE -eq 0) {
        Invoke-Git switch $Branch
    }
    else {
        Invoke-Git switch --track -c $Branch "origin/$Branch"
    }

    # Fast-forward only: never rewrite or discard local history.
    Invoke-Git pull --ff-only origin $Branch

    & git rev-parse --verify --quiet "$VersionTag^{commit}" | Out-Null
    if ($LASTEXITCODE -ne 0) {
        throw "Version tag '$VersionTag' was not fetched. Do not use an unversioned manuscript."
    }
    Invoke-Git merge-base --is-ancestor $VersionTag HEAD

    $required = @(
        "$Project/manuscript/manuscript_sci_final.docx",
        "$Project/manuscript/supplementary_tables_sci_final.docx",
        "$Project/quality_reports/sci_final_audit.json",
        $ChecksumFile
    )
    foreach ($file in $required) {
        if (-not (Test-Path -LiteralPath $file)) {
            throw "Required v0.6 file is missing: $file"
        }
    }

    $checksumFailures = @()
    foreach ($line in Get-Content -LiteralPath $ChecksumFile) {
        if ($line -match '^([0-9a-fA-F]{64})  (.+)$') {
            $expected = $Matches[1].ToLowerInvariant()
            $relative = $Matches[2]
            $actual = (Get-FileHash -LiteralPath (Join-Path $Project $relative) -Algorithm SHA256).Hash.ToLowerInvariant()
            if ($actual -ne $expected) {
                $checksumFailures += $relative
            }
        }
    }
    if ($checksumFailures.Count -gt 0) {
        throw "SHA-256 verification failed: $($checksumFailures -join ', ')"
    }

    $head = (& git rev-parse --short=12 HEAD).Trim()
    $tagCommit = (& git rev-list -n 1 $VersionTag).Trim().Substring(0, 12)
    Write-Host ""
    Write-Host "Sync complete." -ForegroundColor Green
    Write-Host "HEAD:       $head"
    Write-Host "v0.6 tag:   $tagCommit"
    Write-Host "Checksums:  PASS"
    Write-Host "Main DOCX:  $Project/manuscript/manuscript_sci_final.docx"
    Write-Host "Supplement: $Project/manuscript/supplementary_tables_sci_final.docx"
    if ($StashCreated) {
        Write-Host ""
        Write-Host "Your local edits remain safely stashed. Review with 'git stash list'; restore with 'git stash pop' only after checking the synced files." -ForegroundColor Yellow
    }
}
finally {
    Pop-Location
}
