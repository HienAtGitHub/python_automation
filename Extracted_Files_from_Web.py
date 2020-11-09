# -*- coding: utf-8 -*-
"""

@author: Hien Dang

Description: This program is to get to KO Finance Connect and download desired files on a monthly basis

Note: to force the program to stop, move the cursor to the upper left corner of the screen as fast as you can :)

"""
#Import librabries
import pyautogui as pg
import time
import subprocess

# Enable Fail-Safes feature (stop the program by moving the mouse to the upper left corner of the sceen)
pg.FAILSAFE = True

pg.hotkey("winleft")
time.sleep(2)
pg.typewrite("chrome",0.5)
pg.press("enter")
time.sleep(3)

# Download "Profit Center" data
pg.typewrite("https://path_to_desired_file.com/file1.xlsx")
time.sleep(1)
pg.press("enter")
time.sleep(2)

# Dowload "RU" Data
pg.hotkey("ctrl","n")
pg.typewrite("https://path_to_desired_file.com/file2.xlsx")
time.sleep(1)
pg.press("enter")
time.sleep(2)

# Dowload "BOFC Mapping" Data
pg.hotkey("ctrl","n")
pg.typewrite("https://path_to_desired_file.com/file3.xlsx")
time.sleep(1)
pg.press("enter")
time.sleep(2)
