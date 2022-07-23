# Cleaning Script for saving time.
# It will automaticaly clean all the necessary things like, temp, prefetch, etc.

# Import dependencies --

import sys
import pyautogui
# from pynput.keyboard import key, Controller #
import os
import time
import ctypes  # for title window_name

#..............................................

# keyboard = Controller()  # Define keyboard Controller.

# Global Variables --

global currentVersion 
global author
global title 

#.........................

# Global variable def --

currentVersion = 1.0   # Vesion info

author = "Alix"   # Author info

title = "CleanSys"  # Title of window

ctypes.windll.kernel32.SetConsoleTitleW(title + " v" + str(currentVersion))

#...............................


# Global def --

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
    pyautogui.typewrite('prefetch')
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

def close_win():
    pyautogui.hotkey("alt", "f4")

    # To close window

#..........................................



# Main def --

def Clean_main():

    print("=== Clearing _temp_ ===" + "\n")
    
    run()
    temp()
    select_all()
    time.sleep(float(1))
    perma_del()
    time.sleep(float(1))
    skip()
    time.sleep(float(1))
    close_win()

    print("=== Clearing _%temp_ ===" + "\n")

    run()
    temp_perc()
    select_all()
    time.sleep(float(1))
    perma_del()
    time.sleep(float(1))
    skip()
    time.sleep(float(1))
    close_win()

    print("=== Clearing _prefetch_ ===" + "\n")

    run()
    prefetch()
    enter()
    select_all()
    time.sleep(float(1))
    perma_del()
    time.sleep(float(1))
    skip()
    time.sleep(float(1))
    close_win()

    print("=== Running _tree_ ===" + "\n")

    run()
    tree()

    print("=== Cleaning Done ===" + "\n")

    # Main Program class

#........................................


# Various Ui messages --

print()
print("============================")
print("=                          =")
print("=  System Cleaner By " + author + "  =")
print("=                          =")
print("============================")
print()
print()
print()
print("= It will automaticaly clear all the temp files")
print()
print()
print("= temp")
print("= %temp%")
print("= prefetch")
print("= tree")
print()
print()
print()
print()
print("==== Cleaning Will Start Now ====")
print()
print()
print()

#.....................................


# Call Main --

Clean_main()
    
# Quit -- 

time.sleep(float(2))
sys.exit()

    

        

    

    



    




    




    



   












