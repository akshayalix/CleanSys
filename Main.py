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


# Global def--

def temp():

    # Clean_stat for only _temp_

    def win():
        pyautogui.keyDown('win')
        pyautogui.keyUp('win')
        time.sleep(float(1))
    
        # Open windows pannel
    
    def type_run():
        pyautogui.typewrite('Run')
        pyautogui.keyDown('Enter')
        pyautogui.keyUp('Enter')
        time.sleep(float(1))
        
        # Open Run Dailog box

    def type_temp():
        pyautogui.typewrite('temp')
        pyautogui.keyDown('Enter')
        pyautogui.keyUp('Enter')
        time.sleep(float(1))

        # Types _temp_ in run dailog box

    win()
    type_run()
    type_temp()

def temp_perc():

    # Clean_stat for only _%temp%_

    def type_temp_perc():
        pyautogui.typewrite('%temp%')
        pyautogui.keyDown('Enter')
        pyautogui.keyUp('Enter')
        time.sleep(float(1))

        # Types _temp_ in run dailog box

    type_temp_perc()


    
def select_all():
    pyautogui.keyDown("ctrl")
    pyautogui.keyDown("A")
    pyautogui.keyUp("ctrl")
    pyautogui.keyUp("A")





   












