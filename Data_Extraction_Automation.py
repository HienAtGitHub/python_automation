# -*- coding: utf-8 -*-
"""

@author: Hien Dang

Desc: This program is to run the Audit Command Language Script to extract SAP data from the backend

Note: to force the program to stop, move the cursor to the upper left corner of the screen as fast as you can :)

"""
#Import librabries
import pyautogui as pg
import time
import subprocess


# Enable Fail-Safes feature (stop the program by moving the mouse to the upper left corner of the sceen)
pg.FAILSAFE = True

# Call ACLLauncher to activate ACL then open the desired ACL script
program_path = 'C:\\Program Files (x86)\\ACL Software\\ACL for Windows 11\\ACLLauncher.exe'
file_path = 'H:\\Path_to_scripts\\script.acl'
subprocess.Popen([program_path,file_path])
time.sleep(5)

# Look for the "active_analytics" button and click on it
activate_position = pg.locateOnScreen('active_analytics.png')
time.sleep(5)
pg.click(activate_position)
time.sleep(5)

# Navigate to 'Script' Folder and click it
iscripts_position = pg.locateOnScreen('I_Scripts.png')
pg.doubleClick(iscripts_position)
time.sleep(2)

# Navigate to '_Main_Script' Folder and double click it
mainscript_position = pg.locateOnScreen('_Main_Script.png')
pg.doubleClick(mainscript_position)
time.sleep(2)

# Navigate to 'Run' button and click on it
run_position = pg.locateOnScreen('Run.png')
pg.click(run_position)
time.sleep(1)

# Enter username and password
pg.typewrite("username")
pg.press("enter")
pg.typewrite("password")
pg.press("enter")
time.sleep(3)

# hit 'Enter' for all prompts until before "Extract Master Tables"
pg.press("enter")
time.sleep(1)
pg.press("enter")
time.sleep(1)
pg.press("enter")
time.sleep(1)

# Tab to choose "Yes" in the dropdown list to extract Master Tables
pg.press("tab")
pg.press("tab")
pg.press("down")
pg.press("enter")
time.sleep(1)

# Hit "Enter" for the rest of the prompts
pg.press("enter")
time.sleep(1)
pg.press("enter")
time.sleep(1)
