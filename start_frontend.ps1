# Start DataLens Frontend Server
$frontendPath = Join-Path $PSScriptRoot "frontend"
$npmPath = "C:\Program Files\nodejs\npm.cmd"

Write-Host "Starting DataLens Frontend..." -ForegroundColor Green
Set-Location $frontendPath

# Check if node_modules exists
if (-not (Test-Path "node_modules")) {
    Write-Host "Installing dependencies..." -ForegroundColor Yellow
    & $npmPath install
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Failed to install dependencies!" -ForegroundColor Red
        pause
        exit 1
    }
}

Write-Host "Starting development server on http://localhost:3000..." -ForegroundColor Green
& $npmPath run dev

