@echo off
:: Check for admin privileges
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo Requesting administrative privileges...
    powershell.exe -Command "Start-Process cmd -ArgumentList '/c %~fnx0' -Verb RunAs"
    exit
)

set drives=C D E

for %%i in (%drives%) do (
    echo Optimizing drive %%i:
    defrag %%i: /O /V
)



