from pynput import keyboard
from dotenv import load_dotenv
import os
from ftplib import FTP

load_dotenv()
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
        if(key.char=="\x13"):
            save_on_ftp()
    except:
        pass


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

listener = keyboard.Listener(on_press=on_press)
listener.start()
