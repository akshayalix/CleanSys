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

def run():
    pyautogui.hotkey("win", "r")

    # opens run dailog box

def temp():
    pyautogui.typewrite('temp')
    pyautogui.keyDown('Enter')
    pyautogui.keyUp('Enter')
    time.sleep(float(1))

    # Types _temp_ in run dailog box

def temp_perc():
    pyautogui.typewrite('%temp%')
    pyautogui.keyDown('Enter')
    pyautogui.keyUp('Enter')
    time.sleep(float(1))

    # Types _%temp%_ in run dailog box

def prefetch():
    pyautogui.typewrite('%temp%')
    pyautogui.keyDown('Enter')
    pyautogui.keyUp('Enter')
    time.sleep(float(1))

    # Types _prefetch_ in run dailog box

def tree():
    pyautogui.typewrite('tree')
    pyautogui.keyDown('Enter')
    pyautogui.keyUp('Enter')
    time.sleep(float(1))

    # Types _tree_ in run dailog box

    
def select_all():
    pyautogui.hotkey("ctrl", "a")
    
    # To Press select_all_keymap

def enter():
    pyautogui.keyDown('Enter')
    pyautogui.keyUp('Enter')
    
    # To Press Enter_Key

def perma_del():
    pyautogui.hotkey("shift", "del")

    # Press key_map permanent_delete

def skip():
    pyautogui.press("up")
    pyautogui.press("enter")
    pyautogui.press("down")
    pyautogui.press("right")
    pyautogui.press("enter")

    # Initialize skip_protocal




def Clean_main():
    
    run()
    temp()
    time.sleep(float(1))
    select_all()
    time.sleep(float(1))
    perma_del()
    time.sleep(float(1))
    skip()
    


Clean_main()

    

        

    

    



    




    




    



   












