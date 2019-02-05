'''
Austin Wong-Parker
Compatibility Report Script

Project Start: 9/27/18

Before you begin the scrip, please do the following:
1. Computer screen used was a single 1440x900 px monitor. The positions for each mouse movement is relative to only a 1440x900 px screenself.
2. Firefox installed.
3. Firefox magnifier should be default 100% on web page.
4. No other tabs / windows should be open except for this script and the terminal to run the script.
    a. This includes the web page and RoboScreenCapture. The script will open these applications.
5. Before starting, ensure the RoboScreenCapture/Terminal are not maximized windows when opened. This may cause issues when the script is clicking on the top of the webbrowser but instead is clicking on RoboCapture / Terminal.
6. Delete any IODD files loaded onto the device.
7. Reset the IOLM to default settings if needed.

A. How to run script:
    First, you will need to pull up the Terminal, navigate to the directory that the script is in (in this case, it's in Users\Austin\Documents\Atom Projects>) and run the python script by calling the name followed by the .py extensionself.
    An example of this would be Users\Austin\Documents\Atom Projects>testRobo.py

B. If the script messes up due to window mismanagement, network lag, etc:
    The best way to stop the script is to go back to Command Prompt and CTRL-C the program. Additionally, you can use the fail-safe documented below - it states that you can move your mouse to the top left of the screen; however, I haven't been able to get this to work myself.
        If you had to kill the script halfway through, reset firefox to 100% magnifer, close out of firefox and robo without saving, only have cmd window open to run the script.
'''

import os
import time
import pyautogui
import webbrowser
from selenium import webdriver #Currently not being used
from selenium.webdriver.common.keys import Keys #Currently not being used

#function to open RoboScreenCapture
def openFileRobo():
    try:
        os.startfile('RoboScreenCapture')
    except Exception as e:
        print(str(e))

#function to open Notepad
def openFileNotepad():
    try:
        os.startfile('notepad')
    except Exception as e:
        print(str(e))

#Collecting Sensor Information - Will work on this later to reduce amount of user inputs in the script
#print('Thanks for using the compatibility report script. Please provide the following information below. \nPlease type each instruction completely accurate with no excess spaces before or after the word. \nAfter typing each word, you may press enter on the keyboard to continue.')
#portName =


#Opening the webpage
webbrowser.open('http://10.8.14.84/Home', new = 0, autoraise = True)  #Control-1 to switch to Home tab

#FAILSAFE - If the program is acting weird, move the mouse to the upper left corner of the Screenshot.
#Caution - I've tested this and it doesn't work well. Just go to command prompt (cmd) and CTRL-C to stop script.
pyautogui.FAILSAFE = True

#Changing Firefox to 80% magnifier
pyautogui.moveTo(1422, 53, 0.5)
pyautogui.PAUSE = 6
pyautogui.click()
pyautogui.hotkey('ctrl', '-')
pyautogui.hotkey('ctrl', '-') #Had to use two separate hotkeys since one didn't seem to work.
pyautogui.PAUSE = 2.5

#Screenshot 1: Test Report Overview (Page 3)
openFileRobo()
webbrowser.open('http://10.8.14.84/Software', new = 0, autoraise = True) #Control-2 to switch to Advanced tab
pyautogui.moveTo(543,0)
pyautogui.hotkey('ctrl', 'shift', 'r')
pyautogui.moveTo(0,75) #Near Comtrol Icon
pyautogui.dragTo(869, 854, 0.5)
pyautogui.click()

#Screenshot 2: IO-Link Diagnostics Page (Page 4)
pyautogui.moveTo(1280, 10) #Display Main Webbrowser window
pyautogui.click()
webbrowser.open('http://192.168.14.84/IOLink/Diag', new = 0, autoraise = True) #Control-3 to switch to Diagnostics
pyautogui.moveTo(659, 881) #This will serve as a dual-purpose: opening the RoboScreenCapture Program and moving the mouse out of the Screenshot
pyautogui.click()
pyautogui.hotkey('ctrl', 'shift', 'r')
pyautogui.moveTo(890, 856)
pyautogui.dragTo(0, 75, 0.5) #Near Comtrol Icon
pyautogui.click()

#Screenshot 3: Configuring IO-Link Settings (Page 5)
pyautogui.moveTo(1280, 10) #Display Main Webbrowser window
pyautogui.click()
webbrowser.open('http://192.168.14.84/IOLink/Settings', new = 0, autoraise = True) #Control-4 to switch to Configuration
pyautogui.moveTo(714, 271)
pyautogui.click()
pyautogui.moveTo(559, 741)
pyautogui.click()
pyautogui.press('down')
pyautogui.press('enter')
openFileNotepad()
pyautogui.moveRel(10, 10, 1)
pyautogui.typewrite('Please type in the Port Name and press enter in the cmd;\nNote: for most optimal screenshot, use less than 23 characters.\nDo not save - the script will save it.\nClose this window.', interval=0.05)
input('Press Enter to Continue')
pyautogui.moveTo(1280, 10) #Display Main Webbrowser window
pyautogui.click()
pyautogui.moveTo(659, 881) #This will serve as a dual-purpose: opening the RoboScreenCapture Program and moving the mouse out of the Screenshot
pyautogui.click()
pyautogui.moveTo(721, 279) #Mouse included in photo
pyautogui.hotkey('ctrl', 'shift', 'r')
pyautogui.moveTo(955,857)
pyautogui.dragTo(0,75, 0.5) #Near Comtrol Icon
pyautogui.click()
pyautogui.moveTo(1237, 13)
pyautogui.click()
pyautogui.moveTo(721, 279)
pyautogui.click()

#Screenshot 4: Configuring IO-Link Settings (Page 6)
pyautogui.moveTo(1280, 10) #Display Main Webbrowser window
pyautogui.click()
pyautogui.hotkey('ctrl', 'r')
pyautogui.moveTo(659, 881)
pyautogui.click()
pyautogui.hotkey('ctrl', 'shift', 'r')
pyautogui.moveTo(955,857)
pyautogui.dragTo(0,75, 0.5) #Near Comtrol Icon
pyautogui.click()

#Screenshot 5: After Configuring Port-Friendly Names (Page 7)
pyautogui.moveTo(1280, 10) #Display Main Webbrowser window
pyautogui.click()
pyautogui.hotkey('ctrl', '3')
pyautogui.hotkey('ctrl', 'r')
pyautogui.moveTo(958, 241)
pyautogui.click()
pyautogui.moveTo(1088, 241)
pyautogui.click()
pyautogui.moveTo(1247, 241)
pyautogui.moveTo(659, 881) #This will serve as a dual-purpose: opening the RoboScreenCapture Program and moving the mouse out of the Screenshot
pyautogui.click()
pyautogui.hotkey('ctrl', 'shift', 'r')
pyautogui.moveTo(1170, 857)
pyautogui.dragTo(0,75, 0.5) #Near Comtrol Icon
pyautogui.click()

#Screenshot: Password - Do not need to create Screenshot (Page 8)
#Screenshot: IODD Finder - Do this manually (Page 9-10)
openFileNotepad()
pyautogui.moveRel(10, 10, 1)
pyautogui.typewrite('If the sensor needs an IODD from the IODDFinder website, please manually create the screenshot.\nThese are on pages 9-10.\nOnce the IODDFinder website screenshots are complete, you may press enter in the cmd.\nClose this window.', interval=0.05)
input('Press Enter to Continue')

#Screenshot 6: Loading IODD File (Page 12)
pyautogui.moveTo(1280, 10) #Display Main Webbrowser window
pyautogui.click()
webbrowser.open('http://192.168.14.84/IODD', new = 0, autoraise = True) #Control - 5
pyautogui.moveTo(1280, 10) #Display Main Webbrowser window
pyautogui.click()
pyautogui.moveTo(90, 315)
pyautogui.click()
pyautogui.click()
openFileNotepad()
pyautogui.moveRel(10, 10, 1)
pyautogui.typewrite('Please select IODD. Then press enter in cmd. Script will press the upload button.\nClose this window.', interval=0.05)
input('Press Enter to Continue')
pyautogui.moveTo(1280, 10) #Display Main Webbrowser window
pyautogui.click()
pyautogui.PAUSE = 8
pyautogui.moveTo(305, 318)
pyautogui.click()
pyautogui.moveTo(659, 881) #This will serve as a dual-purpose: opening the RoboScreenCapture Program and moving the mouse out of the Screenshot
pyautogui.click()
pyautogui.hotkey('ctrl', 'shift', 'r')
pyautogui.PAUSE = 2
pyautogui.moveTo(929, 640)
pyautogui.dragTo(540, 351)
pyautogui.click()

#Screenshot 7: Loading IODD File (Page 12)
pyautogui.moveTo(1280, 10) #Display Main Webbrowser window
pyautogui.click()
pyautogui.moveTo(885, 591)
pyautogui.click()
pyautogui.moveTo(659, 881) #This will serve as a dual-purpose: opening the RoboScreenCapture Program and moving the mouse out of the Screenshot
pyautogui.click()
pyautogui.hotkey('ctrl', 'shift', 'r')
pyautogui.moveTo(1435, 381)
pyautogui.dragTo(0,75, 0.5) #Near Comtrol Icon
pyautogui.click()

#Screenshot 8: Loading IODD File (Page 13)
pyautogui.moveTo(1280, 10) #Display Main Webbrowser window
pyautogui.click()
pyautogui.moveTo(659, 881) #This will serve as a dual-purpose: opening the RoboScreenCapture Program and moving the mouse out of the Screenshot
pyautogui.click()
pyautogui.moveTo(348, 288)
pyautogui.hotkey('ctrl', 'shift', 'r')
pyautogui.moveTo(1435, 381)
pyautogui.dragTo(0,75, 0.5) #Near Comtrol Icon
pyautogui.click()

#Screenshot 9: Loading IODD File (Page 13)
pyautogui.moveTo(1280, 10) #Display Main Webbrowser window
pyautogui.click()
pyautogui.moveTo(348, 288)
pyautogui.click()
pyautogui.moveTo(659, 881) #This will serve as a dual-purpose: opening the RoboScreenCapture Program and moving the mouse out of the Screenshot
pyautogui.click()
pyautogui.moveTo(694, 228)
pyautogui.hotkey('ctrl', 'shift', 'r')
pyautogui.moveTo(1224, 743)
pyautogui.dragTo(194, 180, 0.5)
pyautogui.click()

#Screenshot 10: Verifying that the Correct IODD Files are Loaded (Page 14)
pyautogui.moveTo(1280, 10) #Display Main Webbrowser window
pyautogui.click()
pyautogui.PAUSE = 5
pyautogui.moveTo(1212, 197)
pyautogui.click()
webbrowser.open('http://192.168.14.84/Summary', new = 0, autoraise = True) #Control - 6
pyautogui.moveTo(659, 881) #This will serve as a dual-purpose: opening the RoboScreenCapture Program and moving the mouse out of the Screenshot
pyautogui.click()
pyautogui.moveTo(854, 858)
pyautogui.hotkey('ctrl', 'shift', 'r')
pyautogui.dragTo(0,75, 0.5) #Near Comtrol Icon
pyautogui.click()
pyautogui.PAUSE = 2.5

#Screenshot 11: Changing Parameters on the Sensor (Page 15)
pyautogui.moveTo(1280, 10) #Display Main Webbrowser window
pyautogui.click()
webbrowser.open('http://192.168.14.84/IODD_Port/1', new = 0, autoraise = True) #Control - 7
openFileNotepad()
pyautogui.moveRel(10, 10, 1)
pyautogui.typewrite('Minimize parameters for screenshot.\nClose this window.', interval=0.05)
input('Press Enter to Continue')
pyautogui.moveTo(1280, 10) #Display Main Webbrowser window
pyautogui.click()
pyautogui.moveTo(659, 881) #This will serve as a dual-purpose: opening the RoboScreenCapture Program and moving the mouse out of the Screenshot
pyautogui.click()
pyautogui.moveTo(1436, 855)
pyautogui.hotkey('ctrl', 'shift', 'r')
pyautogui.dragTo(0,75, 0.5) #Near Comtrol Icon
pyautogui.click()

#Screenshot: Changing Parameters on the Sensor (Page 16-20)
#Indexes and ISDUs need to be done manually
openFileNotepad()
pyautogui.moveRel(10, 10, 1)
pyautogui.typewrite('The next few screenshots are for changing the Indexes / ISDU.\nI recommend doing these nine screenshots manually because Im unable to automate different indexes for different sensors. \nOnce finished, go to any firefox tab and press enter in cmd.\nThese are on pages 16-20.\nClose this window.', interval=0.05)
input('Press Enter to Continue')

#Screenshot 12: Using the Automatic Data Storage Feature (Page 21)
pyautogui.moveTo(1280, 10) #Display Main Webbrowser window
pyautogui.click()
pyautogui.hotkey('ctrl', '4') #Configuration page
pyautogui.hotkey('ctrl', 'r')
pyautogui.moveTo(717, 276)
pyautogui.click()
pyautogui.moveTo(564, 740)
pyautogui.click()
pyautogui.press('up')
pyautogui.press('enter')
pyautogui.moveTo(659, 881) #This will serve as a dual-purpose: opening the RoboScreenCapture Program and moving the mouse out of the Screenshot
pyautogui.click()
pyautogui.moveTo(717, 276)
pyautogui.hotkey('ctrl', 'shift', 'r')
pyautogui.moveTo(960, 856)
pyautogui.dragTo(0,75, 0.5) #Near Comtrol Icon
pyautogui.click()
pyautogui.moveTo(1280, 10) #Display Main Webbrowser window
pyautogui.click()
pyautogui.moveTo(717, 276)
pyautogui.click()

#Screenshot 13: Using the Automatic Data Storage Feature (Factory Reset; Page 21)
pyautogui.moveTo(1280, 10) #Display Main Webbrowser window
pyautogui.click()
pyautogui.hotkey('ctrl', '7') #IODD_Port 1
pyautogui.hotkey('ctrl', 'r')
pyautogui.PAUSE = 15
pyautogui.moveTo(659, 881) #This will serve as a dual-purpose: opening the RoboScreenCapture Program and moving the mouse out of the Screenshot
pyautogui.click()
pyautogui.moveTo(1362, 200)
pyautogui.hotkey('ctrl', 'shift', 'r')
pyautogui.PAUSE = 2.5
pyautogui.moveTo(1436, 855)
pyautogui.dragTo(0,75, 0.5) #Near Comtrol Icon
pyautogui.click()
pyautogui.moveTo(1280, 10) #Display Main Webbrowser window
pyautogui.click()
pyautogui.moveTo(1362, 200)
pyautogui.click()

#Screenshot 14: Using the Automatic Data Storage Feature (Factory Reset; Page 21)
pyautogui.moveTo(1280, 10) #Display Main Webbrowser window
pyautogui.click()
openFileNotepad()
pyautogui.moveRel(10, 10, 1)
pyautogui.typewrite('Manually take screenshot of Restore Factory... Once Refresh Window pops up, press enter in cmd.\nThis is on Page 21.\nClose this window.', interval=0.05)
input('Press Enter to Continue')

#Screenshot 15: Using the Automatic Data Storage Feature (Factory Reset; Page 23)
pyautogui.moveTo(1280, 10) #Display Main Webbrowser window
pyautogui.click()
pyautogui.moveTo(659, 881) #This will serve as a dual-purpose: opening the RoboScreenCapture Program and moving the mouse out of the Screenshot
pyautogui.click()
pyautogui.moveTo(822, 526)
pyautogui.hotkey('ctrl', 'shift', 'r')
pyautogui.moveTo(1436, 855) #Bottom Right Position for Screenshots
pyautogui.dragTo(0,75, 0.5) #Near Comtrol Icon
pyautogui.click()
pyautogui.moveTo(1280, 10) #Display Main Webbrowser window
pyautogui.click()
pyautogui.moveTo(821, 518)
pyautogui.click()

#Screenshot: Notice Parameters... (Page 24)
#Manually do this
openFileNotepad()
pyautogui.moveRel(10, 10, 1)
pyautogui.typewrite('Navigate to Attached Devices --> Port 1 --> Take screenshots on previous parameters that have now changed back to factory default.\nPress enter in cmd.\nClose this window.', interval=0.05)
input('Press Enter to Continue')

#Screenshot 16: Enable Automatic Download (Page 25)
pyautogui.moveTo(1280, 10) #Display Main Webbrowser window
pyautogui.click()
pyautogui.hotkey('ctrl', '4')
pyautogui.hotkey('ctrl', 'r')
pyautogui.moveTo(717, 273)
pyautogui.click()
pyautogui.moveTo(569, 775)
pyautogui.click()
pyautogui.press('down')
pyautogui.press('enter')
pyautogui.moveTo(659, 881) #This will serve as a dual-purpose: opening the RoboScreenCapture Program and moving the mouse out of the Screenshot
pyautogui.click()
pyautogui.moveTo(717, 273)
pyautogui.hotkey('ctrl', 'shift', 'r')
pyautogui.moveTo(959, 858)
pyautogui.dragTo(0,75, 0.5) #Near Comtrol Icon
pyautogui.click()
pyautogui.moveTo(1280, 10) #Display Main Webbrowser window
pyautogui.click()
pyautogui.moveTo(717, 273)
pyautogui.click()

#Screenshot: Downloaded Configured Values (Page 26)
#Manually do this
#Note, this usually never works for some reason, may need to fudge numbers for the report's sake.
openFileNotepad()
pyautogui.moveRel(10, 10, 1)
pyautogui.typewrite('Attached Devices --> Port 1 --> Same parameters; they should be the previously configured parameters now.\nThis one doesnt seem to work all the time so you may have to fudge the numbers for the reports sake.\nPress enter in cmd.\nClose this window.', interval=0.05)
input('Press Enter to Continue')

#Screnshot 17: Clearing Data Storage (Page 27)
pyautogui.moveTo(1280, 10) #Display Main Webbrowser window
pyautogui.click()
pyautogui.hotkey('ctrl', '4')
pyautogui.hotkey('ctrl', 'r')
pyautogui.moveTo(717, 273)
pyautogui.click()
pyautogui.scroll(-1500)
pyautogui.moveTo(558, 376)
pyautogui.click()
pyautogui.press('up')
pyautogui.press('enter')
pyautogui.moveTo(659, 881) #This will serve as a dual-purpose: opening the RoboScreenCapture Program and moving the mouse out of the Screenshot
pyautogui.click()
pyautogui.moveTo(556, 439)
pyautogui.hotkey('ctrl', 'shift', 'r')
pyautogui.moveTo(959, 858) #Port2-3 Screenshot placement
pyautogui.dragTo(0,75, 0.5) #Near Comtrol Icon
pyautogui.click()
pyautogui.moveTo(1280, 10) #Display Main Webbrowser window
pyautogui.click()

#Random Error 0x01 Protocol
openFileNotepad()
pyautogui.moveRel(10, 10, 1)
pyautogui.typewrite('Physically disconnect sensor and plug back in.\nThen, press enter in cmd.\nClose this window.', interval=0.05)
input('Press Enter to Continue')

pyautogui.moveTo(1280, 10) #Display Main Webbrowser window
pyautogui.click()
pyautogui.moveTo(556, 439)
pyautogui.click()
pyautogui.moveTo(800, 523)
pyautogui.click()
pyautogui.moveTo(884, 482)
pyautogui.click()

#Screnshot 18: Clearing Data Storage (Page 28)
pyautogui.moveTo(1280, 10) #Display Main Webbrowser window
pyautogui.click()
pyautogui.moveTo(747, 493)
pyautogui.scroll(1500)
pyautogui.moveTo(725, 272)
pyautogui.click()
pyautogui.moveTo(659, 881) #This will serve as a dual-purpose: opening the RoboScreenCapture Program and moving the mouse out of the Screenshot
pyautogui.click()
pyautogui.hotkey('ctrl', 'shift', 'r')
pyautogui.moveTo(959, 858) #Port2-3 Screenshot placement
pyautogui.dragTo(0,75, 0.5) #Near Comtrol Icon
pyautogui.click()


#Screnshot 19: Using the Manual Data Storage UPLOAD Feature (Page 29)
pyautogui.moveTo(1280, 10) #Display Main Webbrowser window
pyautogui.click()
pyautogui.hotkey('ctrl', 'r')
pyautogui.PAUSE = 4
pyautogui.moveTo(716, 275)
pyautogui.click()
pyautogui.hotkey('ctrl', '-')
pyautogui.moveTo(529, 745)
pyautogui.click()
pyautogui.moveTo(659, 881) #This will serve as a dual-purpose: opening the RoboScreenCapture Program and moving the mouse out of the Screenshot
pyautogui.click()
pyautogui.moveTo(788, 516)
pyautogui.hotkey('ctrl', 'shift', 'r')
pyautogui.moveTo(947, 857) #Modified Port2-3 Screenshot placement
pyautogui.dragTo(0,75, 0.5) #Near Comtrol Ico
pyautogui.click()
pyautogui.moveTo(1280, 10) #Display Main Webbrowser window
pyautogui.click()
pyautogui.moveTo(788, 516)
pyautogui.click()
pyautogui.PAUSE = 5
pyautogui.moveTo(856, 477)
pyautogui.click()
pyautogui.PAUSE = 2

#Screenshot 20: Using the Manual Data Storage UPLOAD Feature (Page 30)
pyautogui.moveTo(1280, 10) #Display Main Webbrowser window
pyautogui.click()
pyautogui.hotkey('ctrl', '+')
pyautogui.moveTo(659, 881) #This will serve as a dual-purpose: opening the RoboScreenCapture Program and moving the mouse out of the Screenshot
pyautogui.click()
pyautogui.hotkey('ctrl', 'shift', 'r')
pyautogui.moveTo(959, 858) #Port2-3 Screenshot placement
pyautogui.dragTo(0,75, 0.5) #Near Comtrol Icon
pyautogui.click()

#Screenshot: Resetting the Sensor to Factory Defaults (Page 31)
#These will be three screenshots that will have to be done manually
openFileNotepad()
pyautogui.moveRel(10, 10, 1)
pyautogui.typewrite('Resetting Sensor to Factory Default Screenshots. \nPage 31-33\nPress enter in cmd.\nClose this window.', interval=0.05)
input('Press Enter to Continue')

#Screenshot 21: Using the Manual Data Storage DOWNLOAD Feature (Page 34)
pyautogui.moveTo(1280, 10) #Display Main Webbrowser window
pyautogui.click()
pyautogui.hotkey('ctrl', '4')
pyautogui.hotkey('ctrl', 'r')
pyautogui.moveTo(715, 276)
pyautogui.click()
pyautogui.hotkey('ctrl', '-')
pyautogui.moveTo(541, 766)
pyautogui.click()
pyautogui.moveTo(659, 881) #This will serve as a dual-purpose: opening the RoboScreenCapture Program and moving the mouse out of the Screenshot
pyautogui.click()
pyautogui.moveTo(792, 516)
pyautogui.hotkey('ctrl', 'shift', 'r')
pyautogui.moveTo(947, 857) #Modified Port2-3 Screenshot placement
pyautogui.dragTo(0,75, 0.5) #Near Comtrol Ico
pyautogui.click()
pyautogui.moveTo(1280, 10) #Display Main Webbrowser window
pyautogui.click()
pyautogui.moveTo(792, 516)
pyautogui.click()
pyautogui.PAUSE = 5
pyautogui.moveTo(856, 496)
pyautogui.click()
pyautogui.PAUSE = 2
pyautogui.hotkey('ctrl', '+')
pyautogui.moveTo(720, 275)
pyautogui.click()

#Screenshot: Manual Data Storage DOWNLOAD - Verifying Parameters (Page 35)
#Manually do this Screenshot
openFileNotepad()
pyautogui.moveRel(10, 10, 1)
pyautogui.typewrite('Go back and verify Parameters are downloaded in the same place in Port1.\n Press enter in cmd.\nClose this window.', interval=0.05)
input('Press Enter to Continue')

#Screenshot: Using the Device Validation Feature (Page 36)
#This one is tricky because I need to flip my screen 90 degrees to get the entire screenshot.
openFileNotepad()
pyautogui.moveRel(10, 10, 1)
pyautogui.typewrite('Need to rotate screen 90 degrees. Configuration page. Page 36.\nPress enter in cmd.\nClose this window.', interval=0.05)
input('Press Enter to Continue')

#Removing the Sensor
openFileNotepad()
pyautogui.moveRel(10, 10, 1)
pyautogui.typewrite('Before continuing, please physically remove the sensor from the Master. Press Enter on cmd when ready.\nClose this window.', interval=0.05)
input('Press Enter to Continue')

#Screenshot 22: Using the Device Validation Feature - Wrong Sensor (Page 37)
pyautogui.moveTo(1280, 10) #Display Main Webbrowser window
pyautogui.click()
pyautogui.hotkey('ctrl', '3')
pyautogui.hotkey('ctrl', 'r')
pyautogui.moveTo(1200, 188)
pyautogui.click()
pyautogui.moveTo(659, 881) #This will serve as a dual-purpose: opening the RoboScreenCapture Program and moving the mouse out of the Screenshot
pyautogui.click()
pyautogui.hotkey('ctrl', 'shift', 'r')
pyautogui.moveTo(1056, 389)
pyautogui.dragTo(0,75, 0.5) #Near Comtrol Ico
pyautogui.click()

#Screenshot 23: Using the Device Validation Feature - Last Events (Page 37)
pyautogui.moveTo(1280, 10) #Display Main Webbrowser window
pyautogui.click()
pyautogui.moveTo(732, 455) #random place to get scroll to works
pyautogui.scroll(-1500)
pyautogui.moveTo(659, 881) #This will serve as a dual-purpose: opening the RoboScreenCapture Program and moving the mouse out of the Screenshot
pyautogui.click()
pyautogui.hotkey('ctrl', 'shift', 'r')
pyautogui.moveTo(1055, 668)
pyautogui.dragTo(43, 557)
pyautogui.click()
pyautogui.moveTo(1280, 10) #Display Main Webbrowser window
pyautogui.click()
pyautogui.moveTo(732, 455) #random place to get scroll to works
pyautogui.scroll(1500)

#Re-Attaching the Sensor
openFileNotepad()
pyautogui.moveRel(10, 10, 1)
pyautogui.typewrite('Before continuing, please physically attach the sensor to the Master. Press Enter on cmd when ready.\nClose this window.', interval=0.05)
input('Press Enter to Continue')

#Screenshot 24: Using the Device Validation - Reattaching Sensor(Page 38)
pyautogui.moveTo(1280, 10) #Display Main Webbrowser window
pyautogui.click()
pyautogui.hotkey('ctrl', '3')
pyautogui.hotkey('ctrl', 'r')
pyautogui.moveTo(659, 881) #This will serve as a dual-purpose: opening the RoboScreenCapture Program and moving the mouse out of the Screenshot
pyautogui.click()
pyautogui.hotkey('ctrl', 'shift', 'r')
pyautogui.moveTo(1056, 857)
pyautogui.dragTo(0,75, 0.5) #Near Comtrol Ico
pyautogui.click()



'''
End of script
First Draft Completed: 10/24/18
Austin Wong-Parker
'''
