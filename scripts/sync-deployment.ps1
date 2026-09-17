[CmdletBinding()]
param(
    [ValidateSet("Check", "Apply")]
    [string]$Mode = "Check",
    [string]$Destination = $env:TRIZ_DEPLOY_DIR
)

$source = Join-Path (Split-Path -Parent $PSScriptRoot) "triz-universal"
if (-not (Test-Path -LiteralPath $source -PathType Container)) {
    throw "Source skill directory does not exist: $source"
}
if ([string]::IsNullOrWhiteSpace($Destination)) {
    throw "Set TRIZ_DEPLOY_DIR or pass -Destination to the installed triz-universal directory."
}

$destinationPath = [System.IO.Path]::GetFullPath($Destination)
if ((Split-Path -Leaf $destinationPath) -ne "triz-universal") {
    throw "Destination must be the triz-universal directory, not a broader parent path: $destinationPath"
}

function Get-FileHashes([string]$Root) {
    if (-not (Test-Path -LiteralPath $Root -PathType Container)) {
        return @()
    }
    $rootPath = [System.IO.Path]::GetFullPath($Root).TrimEnd([System.IO.Path]::DirectorySeparatorChar)
    return @(Get-ChildItem -LiteralPath $rootPath -Recurse -File | ForEach-Object {
        $relative = $_.FullName.Substring($rootPath.Length).TrimStart([char[]]@('\', '/'))
        "$relative|$((Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256).Hash)"
    })
}

if ($Mode -eq "Apply") {
    if (Test-Path -LiteralPath $destinationPath) {
        Get-ChildItem -LiteralPath $destinationPath -Force | Remove-Item -Recurse -Force
    } else {
        New-Item -ItemType Directory -Path $destinationPath -Force | Out-Null
    }
    Copy-Item -Path (Join-Path $source "*") -Destination $destinationPath -Recurse -Force
}

$sourceHashes = Get-FileHashes $source
$destinationHashes = Get-FileHashes $destinationPath
$differences = Compare-Object -ReferenceObject @($sourceHashes) -DifferenceObject @($destinationHashes)

if ($differences) {
    $message = "Deployed skill differs from source. Run with -Mode Apply after reviewing the target: $destinationPath"
    if ($Mode -eq "Check") { throw $message }
    throw "Deployment sync did not produce byte-for-byte parity: $destinationPath"
}

Write-Output "Deployment is synchronized: $destinationPath"
