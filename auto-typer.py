#!/bin/python3
import pyautogui
import time

dwellTime = 5
time.sleep(dwellTime)

cmdFilename = r"./commands.txt"
keystrokeInterval = 0.1
postCommandDelay = 1.0 

with open(cmdFilename, 'r') as f:
    commands = [line.strip() for line in f if line.strip()]

for command in commands:
    pyautogui.write(command, interval=keystrokeInterval)
    tiem.sleep(1)
    pyautogui.press('enter')
    time.sleep(postCommandDelay)
