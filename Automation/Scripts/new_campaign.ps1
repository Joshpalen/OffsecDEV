param(
  [Parameter(Mandatory=$true)][string]$Name,
  [string]$Root = "Pentest Campaign/Reports",
  [string]$TemplateOverview = "Templates/Campaign_Overview.md"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$rootFull = Resolve-Path -LiteralPath . | Join-Path -ChildPath $Root
if (-not (Test-Path $rootFull)) { throw "Root path not found: $rootFull" }

$camp = Join-Path $rootFull $Name
$dirs = @(
  '01-Admin/ROE',
  '02-Recon/scans',
  '02-Recon/Infrastructure/Templates',
  '03-Enumeration/scans',
  '04-Exploitation',
  '05-Post-Exploitation',
  '06-Reporting/Findings',
  'Evidence/images','Evidence/pcap','Evidence/logs','Evidence/emails','Evidence/attachments','Evidence/audio','Evidence/other'
)
foreach ($d in $dirs) { New-Item -ItemType Directory -Force -Path (Join-Path $camp $d) | Out-Null }

# Overview
$tpl = Resolve-Path -LiteralPath $TemplateOverview
$overview = Join-Path $camp 'Overview.md'
Copy-Item -LiteralPath $tpl -Destination $overview -Force
Write-Host "Campaign scaffold created at: $camp" -ForegroundColor Green

