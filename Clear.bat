:: A script to clean basic directories for windows.
:: By Alix
:: version=1.2


:: Main

@ECHO OFF

:: Clear %temp% 

cd /D %temp%

for /d %%D in (*) do rd /s /q "%%D"

del /f /q *

::................

:: Clear temp

cd /D C:\Windows\Temp\

for /d %%D in (*) do rd /s /q "%%D"

del /f /q *

::..................

:: Clear Prefetch

cd /D C:\Windows\Prefetch\

for /d %%D in (*) do rd /s /q "%%D"

del /f /q *

::.......................