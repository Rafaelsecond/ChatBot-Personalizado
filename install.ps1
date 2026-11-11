$ErrorActionPreference = 'Stop'

winget install -e --id Microsoft.AzureCLI
winget install microsoft.azd
azd ext install microsoft.foundry

python -m venv .venv
.venv/Scripts/Activate.ps1
python -m pip install -r requirements.txt