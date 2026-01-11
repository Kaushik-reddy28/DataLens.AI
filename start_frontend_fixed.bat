@echo off
echo Starting DataLens Frontend...
cd /d "%~dp0frontend"

REM Check if npm is available
where npm >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: npm is not found in PATH!
    echo Please install Node.js from https://nodejs.org/
    echo Make sure to check "Add to PATH" during installation.
    echo After installation, restart your computer and try again.
    pause
    exit /b 1
)

if not exist "node_modules" (
    echo Installing dependencies...
    call npm install
    if %ERRORLEVEL% NEQ 0 (
        echo ERROR: Failed to install dependencies!
        pause
        exit /b 1
    )
)

echo Starting development server on http://localhost:3000...
echo.
echo Backend should be running on http://localhost:5000
echo.
call npm run dev
pause

