:: This batch file tells you the details of your windows, hardware and networking configuration.

:: CurrentVersion = 1.0

:: Author = Alix

@ECHO OFF

TITLE SysInfo

ECHO.
ECHO.

ECHO                                            ===============
ECHO                                            =    HELLO    =
ECHO                                            ===============

:: Section 1: windows information.

ECHO.
ECHO                                         ======================
ECHO                                         =    WINDOWS INFO    =
ECHO                                         ======================
ECHO.

Systeminfo | findstr /c:"OS Name"
Systeminfo | findstr /c:"OS Version"
Systeminfo | findstr /c:"System Type"


PAUSE
