from pynput import keyboard
from dotenv import load_dotenv
import os
from ftplib import FTP

load_dotenv()
FTP_USERNAME = os.getenv('FTP_USERNAME')
FTP_PASSWORD = os.getenv('FTP_PASSWORD')
FTP_HOST = os.getenv('FTP_HOST')

print("start")

ftp = FTP()
ftp.connect(FTP_HOST, 21)
ftp.login(FTP_USERNAME, FTP_PASSWORD)
print(ftp.getwelcome())

def save_on_ftp():
    print("ctrl+s pressed")

def on_press(key):
    try:
        if(key.char=="\x13"):
            save_on_ftp()
    except:
        pass


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

listener = keyboard.Listener(on_press=on_press)
listener.start()
