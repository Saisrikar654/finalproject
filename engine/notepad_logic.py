import os
import subprocess
import pyautogui as gui
import time

# Absolute path for your specific project needs
SAVE_PATH = r"C:\Users\sSs\Desktop\notepad files"

# Ensure directory exists at startup
if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

def open_notepad():
    subprocess.Popen(['notepad.exe'])
    time.sleep(2)

import pygetwindow as gw

def write_text(content):
    # FORCE FOCUS: Find any window with "Notepad" in the title
    try:
        notepad_window = gw.getWindowsWithTitle('Notepad')[0]
        notepad_window.activate() # Brings it to the front
        time.sleep(0.5) 
    except:
        print("Notepad window not found!")

    gui.write(content, interval=0.02)
    gui.press('enter')

def save_notepad(filename):
    # FORCE FOCUS before saving
    try:
        notepad_window = gw.getWindowsWithTitle('Notepad')[0]
        notepad_window.activate()
        time.sleep(0.5)
    except:
        pass

    if not filename.endswith(".txt"):
        filename += ".txt"
    
    full_file_path = os.path.join(SAVE_PATH, filename)
    
    gui.hotkey('ctrl', 's')
    time.sleep(1)
    gui.write(full_file_path)
    time.sleep(0.5)
    gui.press('enter')

def rename_notepad_file(old_name, new_name):
    if not old_name.endswith(".txt"): old_name += ".txt"
    if not new_name.endswith(".txt"): new_name += ".txt"
    
    old_full = os.path.join(SAVE_PATH, old_name)
    new_full = os.path.join(SAVE_PATH, new_name)
    
    try:
        if os.path.exists(old_full):
            # Close Notepad to unlock the file for renaming
            os.system("taskkill /f /im notepad.exe >nul 2>&1")
            time.sleep(1)
            os.rename(old_full, new_full)
            return True
        return False
    except:
        return False