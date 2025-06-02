#!/bin/python3

import pyautogui
import time

dwellTime = 5
time.sleep(dwell_time)

cmdFilenme = r"/home/ubuntu/command.txt"
keystrokeInterval = 0.1 

with open(cmdFilename) as f:
	data = f.read()
	pyautogui.write(data, interval=keystrokeInterval)
