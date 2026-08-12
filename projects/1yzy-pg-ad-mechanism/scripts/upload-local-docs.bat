@echo off
setlocal
echo === 1yzy source-docs upload ===
cd /d "%~dp0..\..\.."
echo repo=%CD%
if not exist ".git" (
  echo ERROR: not the git repo root: %CD%
  exit /b 1
)
git rev-parse --abbrev-ref HEAD
if not exist "E:\0writing\1yzy" (
  echo ERROR: missing E:\0writing\1yzy
  exit /b 1
)
mkdir "projects\1yzy-pg-ad-mechanism\source-docs" 2>nul
echo Copying files...
copy /Y "E:\0writing\1yzy\*" "projects\1yzy-pg-ad-mechanism\source-docs\"
dir "projects\1yzy-pg-ad-mechanism\source-docs"
git add "projects/1yzy-pg-ad-mechanism/source-docs"
git status
echo.
echo If status looks right, run:
echo   git commit -m "docs(1yzy): ingest local source manuscripts from E:\0writing\1yzy"
echo   git push origin arena/019ff371-auto-empirical-research-skills
endlocal
