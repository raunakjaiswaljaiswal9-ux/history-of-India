# History of India - Localhost Server Starter
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $scriptDir

# Check if Python is available
$pythonCmd = Get-Command python, py -ErrorAction SilentlyContinue | Select-Object -First 1

if ($pythonCmd) {
    Write-Host "[+] Starting Python localhost server via $($pythonCmd.Name)..." -ForegroundColor Cyan
    & $pythonCmd.Source "$scriptDir\server.py"
    exit
}

# Fallback: Native .NET HttpListener (Runs on every modern Windows system)
$port = 8000
$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://localhost:$port/")

try {
    $listener.Start()
} catch {
    $port = 8080
    $listener = New-Object System.Net.HttpListener
    $listener.Prefixes.Add("http://localhost:$port/")
    $listener.Start()
}

$url = "http://localhost:$port/"
Write-Host "==========================================================" -ForegroundColor Yellow
Write-Host "  ✦ HISTORY OF INDIA — LOCALHOST SERVER RUNNING ✦" -ForegroundColor Yellow
Write-Host "==========================================================" -ForegroundColor Yellow
Write-Host "  [+] Localhost URL: $url" -ForegroundColor Green
Write-Host "  [+] Directory    : $scriptDir" -ForegroundColor Cyan
Write-Host "  Press Ctrl+C to terminate." -ForegroundColor Gray
Write-Host "==========================================================" -ForegroundColor Yellow

Start-Process $url

while ($listener.IsListening) {
    $context = $listener.GetContext()
    $request = $context.Request
    $response = $context.Response

    $localPath = $request.Url.LocalPath
    if ($localPath -eq "/" -or [string]::IsNullOrWhiteSpace($localPath)) {
        $localPath = "/index.html"
    }

    $filePath = Join-Path $scriptDir $localPath.TrimStart('/')

    if (Test-Path $filePath -PathType Leaf) {
        $ext = [System.IO.Path]::GetExtension($filePath).ToLower()
        $contentType = switch ($ext) {
            ".html" { "text/html; charset=utf-8" }
            ".css"  { "text/css; charset=utf-8" }
            ".js"   { "application/javascript; charset=utf-8" }
            ".json" { "application/json; charset=utf-8" }
            ".svg"  { "image/svg+xml" }
            ".png"  { "image/png" }
            ".jpg"  { "image/jpeg" }
            default { "application/octet-stream" }
        }

        $bytes = [System.IO.File]::ReadAllBytes($filePath)
        $response.ContentType = $contentType
        $response.ContentLength64 = $bytes.Length
        $response.AddHeader("Access-Control-Allow-Origin", "*")
        $response.OutputStream.Write($bytes, 0, $bytes.Length)
    } else {
        $response.StatusCode = 404
        $msg = [System.Text.Encoding]::UTF8.GetBytes("404 - File Not Found")
        $response.OutputStream.Write($msg, 0, $msg.Length)
    }
    $response.Close()
}
