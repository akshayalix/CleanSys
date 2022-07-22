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

:: Section 2: Hardwware information.

ECHO.
ECHO                                        ======================
ECHO                                        =    HARDWARE INFO   =
ECHO                                        ======================
ECHO.

Systeminfo | findstr /c:"Total Physical Memory"
wmic cpu get Name
wmic diskdrive get name,model,size
wmic path win32_videocontroller get name

PAUSE
