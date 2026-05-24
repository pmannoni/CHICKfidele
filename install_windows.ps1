$ErrorActionPreference = 'Stop'

Set-Location -Path $PSScriptRoot

# Use the project venv python if present
$py = Join-Path $PSScriptRoot '.venv\Scripts\python.exe'
if (-not (Test-Path $py)) {
    throw "Python venv introuvable: $py"
}

Write-Host '[1/6] Upgrade pip/setuptools/wheel'
& $py -m pip install --upgrade pip setuptools wheel

Write-Host '[2/6] Install CPU PyTorch (required by nougat)'
& $py -m pip install --index-url https://download.pytorch.org/whl/cpu torch torchvision

Write-Host '[3/6] Install resolver guard dependencies first'
& $py -m pip install datasets==2.21.0 pyarrow==24.0.0

Write-Host '[4/6] Install project requirements'
& $py -m pip install -r requirements.txt

Write-Host '[5/6] Verify nougat CLI'
$nougatExe = Join-Path $PSScriptRoot '.venv\Scripts\nougat.exe'
if (Test-Path $nougatExe) {
    & $nougatExe --help | Out-Null
    Write-Host 'nougat.exe OK'
} else {
    Write-Warning 'nougat.exe non trouve dans .venv\Scripts. Test fallback python -m nougat...'
    & $py -m nougat --help | Out-Null
    Write-Host 'python -m nougat OK'
}

Write-Host '[6/6] Final check'
& $py -m pip show nougat-ocr | Out-Host
Write-Host 'Installation terminee.'

