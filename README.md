# CompatibilityScriptSEL

Updated 2019 verison of the Compatibility Script used for automating sensor report information. This repository is the successor of CompatScript.py

---

**Disclaimer #1:** this code is 100% only for the use of Compatibilty Report Scripting that was used for automating certain sensor reports at my current internship - that's all. DO NOT use this code for reference, there is a lot of _bad coding practices_ in this file. 

**Disclaimer #2:** most of the code is 'hard-coded' exactly for a specific monitor resolution (1440 x 900). If you are referencing this repo, please do not use my exact pixel positions - it won't work on your machine. Please reference the documentation for each method / program. Also, there's many autoIt scripts running on sidewinder that'll need to be working for full utilization of this script. 



# Looking for an answer: 

I am still looking for a solution on deploying this script to multiple machines w/o using pixel position. First - I've tried image recognition from pyautogui, though it wasn't working at all. The image couldn't be located. Second - Unfortunately selenium is only browser automation, so I couldn't use it for my RoboScreenCapture software. Third - I've tried autoIt's SciTE Script Editor and autoIT window info to try and get the class & instance of an element, but this doesn't seem to work very well on non-browser applications.


# Apps
1. Python Methods used: pyautogui, win32gui, selenium.
2. Scripting programs used: autoit.
3. Window applications: RoboScreenCapture.
