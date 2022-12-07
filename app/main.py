from __future__ import print_function
from infi.systray import SysTrayIcon
import os
import ctypes
from pynput import keyboard
from dotenv import load_dotenv
import os
from ftplib import FTP
import threading
import tkinter
import customtkinter  
import settings

pause = False

""" load_dotenv()
FTP_USERNAME = os.getenv('FTP_USERNAME')
FTP_PASSWORD = os.getenv('FTP_PASSWORD')
FTP_HOST = os.getenv('FTP_HOST')
FTP_DIRECTORY = os.getenv('FTP_DIRECTORY')
FILES = os.getenv('FILES')

ftp = FTP(FTP_HOST, encoding="latin-1")
ftp.login(FTP_USERNAME, FTP_PASSWORD)
ftp.cwd(FTP_DIRECTORY)

def fast_save():
    for f in FILES.split(","):
        split = f.split("\\")
        filename = split[len(split)-1]
        file = open(f,"rb")
        ftp.storbinary("STOR "+filename, file)
        file.close()

def save_on_ftp():
    print("ctrl+s pressed")
    fast_save()

def on_press(key):
    try:
        if(key.char=="\x13" and not pause):
            save_on_ftp()
    except:
        pass

def thread_function():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

x = threading.Thread(target=thread_function)
x.start() """


def on_quit(systray):
    import sys
    sys.exit(0)
def set_pause(systray):
    global pause
    pause = not pause
def on_status(systray):
    status = "stopped" if pause else "active"
    ctypes.windll.user32.MessageBoxW(None, u"Status: "+status, u"About", 0)
menu_options = (("Pause/Resume", None, set_pause),
                ("Settings", None, settings.run),
                ("Status", None, on_status))
systray = SysTrayIcon(os.path.join(os.path.dirname(__file__), "ftp.ico"), "Fast FTP", menu_options, on_quit)
systray.start()
