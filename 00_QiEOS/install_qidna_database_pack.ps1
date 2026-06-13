# QiDNA Database Standards Pack installer helper
# Run from the unzipped package root if needed.

$TargetRoot = "C:\QiLabs"
$Source = Join-Path $PSScriptRoot "_QiOS_DNA"
$Destination = Join-Path $TargetRoot "_QiOS_DNA"

Write-Host "Copying QiDNA database standards into $TargetRoot ..."
Copy-Item -Path $Source -Destination $TargetRoot -Recurse -Force
Write-Host "Done. Target folder: C:\QiLabs\_QiOS_DNA\00_QiEOS\30_standards\40_database"
