#!/bin/python3

import pyautogui
import time

dwellTime = 5
time.sleep(dwellTime)

cmdFilenme = r"./command.txt"
keystrokeInterval = 0.1 

with open(cmdFilename) as f:
	data = f.read()
	pyautogui.write(data, interval=keystrokeInterval)
