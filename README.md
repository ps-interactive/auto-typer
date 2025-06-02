# auto-typer
A tool for smoothly typing commands in demos

## Parameters
* dwellTime: Initial delay to allow you to focus the terminal window you wnt to type in
* cmdFilename: Full path to the command file 
* keystrokeInterval: The time between each keystroke in seconds
* postCommandDelay: The delay between running successive commands

## Usage
<p>pip3 install pyautogui
<p>git clone https://github.com/ps-interactive/auto-typer.git
<p>cd auto-typer
<p>sudo chmod +x auto-typer.py
<p>Edit command.txt to hold the command you want to be typed
<p>./auto-typer.py
<p> Switch to the console you want your command to be typed in

## To-Do
* Add jitter around keystrokeInterval so typing looks more natural
* Add command line options for dwellTime, cmdFilename and keystrokeInterval
* Add support for multi-command demos. Detect when a command has completed and then run the next one.
