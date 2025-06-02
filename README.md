# auto-typer
A tool for smoothly typing commands in demos

## Parameters
* dwellTime: The maximum available time from running the script to bringing the target window into focus
* cmdFilename: Full path to the command file 
* keystrokeInterval: The time between each keystroke in seconds

## Usage
<p>pip3 install pyautogui
<p>git clone https://github.com/ps-interactive/auto-typer.git
<p>cd auto-typer
<p>sudo chmod +x auto-typer.py
<p>Create a file called command.txt which contains the command you want to be typed
<p>./auto-typer.py
  
## To-Do
* Add jitter around keystrokeInterval so typing looks more natural
* Add command line options for dwellTime, cmdFilename and keystrokeInterval
* Add support for multi-command demos. Detect when a command has completed and then run the next one.
