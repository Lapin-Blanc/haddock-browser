$ErrorActionPreference = "Stop"

if ($args.Count -lt 1) {
    Write-Host "Usage: tools\\tag_release.ps1 <version> [message]"
    Write-Host "Exemple: tools\\tag_release.ps1 v0.1.0 \"pedagogic release\""
    exit 1
}

$version = $args[0]
$message = "release"
if ($args.Count -ge 2) {
    $message = ($args[1..($args.Count - 1)] -join " ")
}

$status = git status --porcelain
if ($status) {
    Write-Host "Working tree non clean. Commit ou stash avant de tagger."
    exit 1
}

git tag -a $version -m "${version}: $message"
git push origin $version
