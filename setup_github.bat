@echo off
setlocal enabledelayedexpansion
title History of India - GitHub Setup & Push
echo ========================================================
echo    History of India - GitHub Repository Publisher
echo ========================================================
echo.
cd /d "%~dp0"

where git >nul 2>nul
if %errorlevel% neq 0 (
    if exist "%LOCALAPPDATA%\Microsoft\WinGet\Packages\Git.MinGit_Microsoft.Winget.Source_8wekyb3d8bbwe\cmd\git.exe" (
        set "PATH=%LOCALAPPDATA%\Microsoft\WinGet\Packages\Git.MinGit_Microsoft.Winget.Source_8wekyb3d8bbwe\cmd;!PATH!"
    ) else if exist "C:\Program Files\Git\cmd\git.exe" (
        set "PATH=C:\Program Files\Git\cmd;!PATH!"
    ) else if exist "%LOCALAPPDATA%\Programs\Git\cmd\git.exe" (
        set "PATH=%LOCALAPPDATA%\Programs\Git\cmd;!PATH!"
    ) else (
        echo [!] Git was not found on your system.
        echo Please ensure Git is installed.
        pause
        exit /b 1
    )
)

echo [+] Checking Git repository status...
if not exist ".git" (
    echo [+] Initializing local Git repository...
    git init
    git branch -M main
)

echo.
echo [+] Adding files to staging...
git add .

echo [+] Creating commit...
git commit -m "Initial release: History of India interactive digital archive & project report"

echo.
echo ========================================================
echo  Step 1: Go to https://github.com/new in your browser.
echo  Step 2: Create a repository named: history-of-india
echo  Step 3: Copy the repository URL (e.g., https://github.com/YourUsername/history-of-india.git)
echo ========================================================
echo.
set /p REPO_URL="Paste your GitHub Repository URL here (or press Enter to skip): "

if not "%REPO_URL%"=="" (
    git remote remove origin >nul 2>nul
    git remote add origin %REPO_URL%
    echo.
    echo [+] Pushing to GitHub (main branch)...
    git push -u origin main
    if %errorlevel% equ 0 (
        echo.
        echo [SUCCESS] Your project has been uploaded to GitHub successfully!
        echo You can now enable GitHub Pages in Settings -^> Pages to host it online for free!
    ) else (
        echo.
        echo [!] Push failed. Please verify your GitHub credentials or repo permissions.
    )
) else (
    echo.
    echo [*] Skipped remote push. Your local Git repository is initialized and committed.
)

echo.
pause
