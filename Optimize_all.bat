@echo off
set drives=C D E

for %%i in (%drives%) do (
    echo Optimizing drive %%i:
    defrag %%i: /O /V
)

