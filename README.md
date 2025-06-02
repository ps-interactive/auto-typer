# auto-typer
A tool for smoothly typing commands in demos

## Pre-requisites
* Requires python3
<p>pip3 install pyautogui

## Parameters
* dwellTime: The maximum available time from running the script to bringing the target window into focus
* cmdFilename: Full path to the command file 
* keystrokeInterval: The time between each keystroke in seconds

## Usage
<p>Create a file called cmd.txt which contains the command you want to be typed
<p>./auto-typer.py
  
## To-Do
* Add jitter around keystrokeInterval so typing looks more natural
* Add command line options for dwellTime, cmdFilename and keystrokeInterval
* Add support for multi-command demos. Detect when a command has completed and then run the next one.
