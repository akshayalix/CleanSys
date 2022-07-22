# Cleaning Script for saving time.
# It will automaticaly clean all the necessary things like, temp, prefetch, etc.

# Import dependencies --

import pyautogui
# from pynput.keyboard import key, Controller #
import os
import time

# keyboard = Controller()  # Define keyboard Controller.

# Global Variables --

global currentVersion 
global author
global name

currentVersion = 1.0   # Vesion info

author = "Alix"   # Author info

name = "CleanSys"  # Script Name


# Let's User decide if they want system info

print()
print("Hello" + "\n" )
print("Welcome to CleanSys")
print()
print("Do you want to display system Info " + "  Y/N  " + "\n")

sysinfo_userinput = input("Answer : ")

if sysinfo_userinput == 'Y':
    
    # SysInfo_bat content

    SysInfo_bat = """   :: This batch file tells you the details of your windows, hardware and networking configuration. 

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

                        :: Section 3: Netwwork information.

                        ECHO.
                        ECHO                                       ======================
                        ECHO                                       =    NETWORK INFO    =
                        ECHO                                       ======================
                        ECHO.

                        ipconfig | findstr IPv4
                        ipconfig | findstr IPv6


                        PAUSE 
                        ECHO.  """


    # Save SysInfo_bat 

    f = open("SysInfoR.bat", "w")
    f.write(SysInfo_bat)
    f.close()

    # To open SysInfo_bat

    def SysInfo_open():
        os.startfile("SysInfoR.bat")


    SysInfo_open()

else:
    print("Declined")






