# src/commands.py
import os

def execute_command(command):
    if "switch audio" in command:
        # Example: Command for switching audio device
        os.system("powershell -command \"Set-DefaultAudioDevice -Name 'Speakers'\"")
        print("Switched audio device")
    elif "open browser" in command:
        # Example: Opening a browser
        os.system("start chrome")
        print("Opening browser")
    else:
        print("Command not recognized")