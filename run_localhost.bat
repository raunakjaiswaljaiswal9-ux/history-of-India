@echo off
title History of India - Localhost Server
echo ========================================================
echo    Launching History of India on Localhost...
echo ========================================================
cd /d "%~dp0"

where python >nul 2>nul
if %errorlevel% equ 0 (
    python server.py
    goto end
)

where py >nul 2>nul
if %errorlevel% equ 0 (
    py server.py
    goto end
)

if exist "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" (
    "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" server.py
    goto end
)

if exist "%ProgramFiles%\Python312\python.exe" (
    "%ProgramFiles%\Python312\python.exe" server.py
    goto end
)

echo [!] Python was not detected in PATH.
echo Starting via PowerShell localhost HTTP server...
powershell -ExecutionPolicy Bypass -File "%~dp0start_server.ps1"

:end
pause
