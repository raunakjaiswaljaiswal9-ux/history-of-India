@echo off
title Push History of India to GitHub
cd /d "%~dp0"

echo =======================================================================
echo    PUSHING HISTORY OF INDIA TO GITHUB
echo    Target: https://github.com/raunakjaiswaljaiswal9-ux/history-of-India.git
echo =======================================================================
echo.

set "PATH=C:\Users\RAUNAK JAISWAL\AppData\Local\Microsoft\WinGet\Packages\Git.MinGit_Microsoft.Winget.Source_8wekyb3d8bbwe\cmd;C:\Users\RAUNAK JAISWAL\AppData\Local\Microsoft\WinGet\Packages\GitHub.cli_Microsoft.Winget.Source_8wekyb3d8bbwe\bin;%PATH%"

gh auth status >nul 2>nul
if %errorlevel% neq 0 (
    echo [*] Connecting your GitHub account (raunakjaiswaljaiswal9-ux)...
    echo     1. Your web browser will open GitHub.
    echo     2. Enter the one-time code shown below and click 'Authorize'.
    echo.
    gh auth login --web -h github.com
    gh auth setup-git
)

echo.
echo [+] Pushing project commits and museum assets to GitHub...
git push -u origin main --force

if %errorlevel% equ 0 (
    echo.
    echo =======================================================================
    echo   [SUCCESS] Your project has been uploaded to GitHub!
    echo   Repository URL:
    echo   https://github.com/raunakjaiswaljaiswal9-ux/history-of-India
    echo =======================================================================
    echo.
    echo   To make it live worldwide on GitHub Pages:
    echo   1. Open https://github.com/raunakjaiswaljaiswal9-ux/history-of-India/settings/pages
    echo   2. Set Branch to 'main' and click Save!
    echo.
) else (
    echo.
    echo [!] Push encountered an issue. Please review the message above.
)

pause
