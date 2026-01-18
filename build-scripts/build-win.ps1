$ErrorActionPreference = "Stop"

$projectRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
Push-Location $projectRoot

try {
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt

    $iconPath = Join-Path $projectRoot "assets\icon.ico"
    if (-not (Test-Path $iconPath)) {
        throw "Icone introuvable : $iconPath"
    }

    python -m nuitka `
        --standalone `
        --onefile `
        --enable-plugin=pyside6 `
        --lto=yes `
        --assume-yes-for-downloads `
        --windows-console-mode=disable `
        --windows-icon-from-ico="$iconPath" `
        --remove-output `
        --output-dir=dist `
        src\app.py
}
finally {
    Pop-Location
}
