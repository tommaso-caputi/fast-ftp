from __future__ import print_function
from infi.systray import SysTrayIcon
import os
import ctypes
from pynput import keyboard
from dotenv import load_dotenv
import os
from ftplib import FTP
import threading
from tkinter.filedialog import askopenfilenames
import tkinter
import customtkinter

pause = False

def set_values():
    load_dotenv()
    return os.getenv('FTP_USERNAME'), os.getenv('FTP_PASSWORD'), os.getenv('FTP_HOST'), os.getenv('FTP_DIRECTORY'), os.getenv('FILES')

FTP_USERNAME, FTP_PASSWORD, FTP_HOST, FTP_DIRECTORY, FILES = set_values()


ftp = FTP(FTP_HOST, encoding="latin-1")
ftp.login(FTP_USERNAME, FTP_PASSWORD)
ftp.cwd(FTP_DIRECTORY)

def fast_save():
    for f in FILES.split(","):
        split = f.split("\\")
        filename = split[len(split)-1]
        print(filename)
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
x.start()

def get_values():
    values = {}
    with open(".env","r") as f:
        line = str(f.read())
        line = str(line).split()
        for i in range(0, int(len(line)), 3):
            values[line[i]] = line[i+2]
    return values    

def settings(systray):
    root_tk = tkinter.Tk()
    root_tk.geometry("500x270")
    root_tk.title("CustomTkinter Test")
    root_tk.eval('tk::PlaceWindow . center')
    root_tk.resizable(False, False)
    def set_file_paths(): #need to be fixed
        filepaths = askopenfilenames() 
        paths = ""
        with open('.env','w') as f:
            for i in range(len(values)-1):
                f.write(str(keys[i])+" = "+str(values[keys[i]])+"\n")
            for path in filepaths:
                paths+=path+"-"
            paths = paths[:-1]
            f.write("FILES = "+paths)
        FTP_USERNAME, FTP_PASSWORD, FTP_HOST, FTP_DIRECTORY, FILES = set_values()
        root_tk.destroy()
    def update():
        with open(".env","w") as f:
            for i in range(len(keys)):
                new_line = keys[i]+" = "+entrys[i].get()+"\n"
                f.write(new_line)
        FTP_USERNAME, FTP_PASSWORD, FTP_HOST, FTP_DIRECTORY, FILES = set_values()
        root_tk.destroy()
    values = get_values()
    keys = list(values.keys())
    entrys = []
    for i in range(len(keys)):
        customtkinter.CTkLabel(master=root_tk, text=str(keys[i]), text_color="blue").place(relx=0.025, rely=i/10)
        entrys.append(customtkinter.CTkEntry(master=root_tk, textvariable = tkinter.StringVar(root_tk, values[keys[i]]),width = 350, height=20))
        entrys[i].place(relx=0.25, rely=i/10)
    customtkinter.CTkButton(master=root_tk, text="Update files",corner_radius=10, command=set_file_paths).place(relx=0.7, rely=0.9, anchor=tkinter.CENTER)
    customtkinter.CTkButton(master=root_tk, text="Update data",corner_radius=10, command=update).place(relx=0.3, rely=0.9, anchor=tkinter.CENTER)
    root_tk.mainloop()

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
                ("Settings", None, settings),
                ("Status", None, on_status))
systray = SysTrayIcon(os.path.join(os.path.dirname(__file__), "ftp.ico"), "Fast FTP", menu_options, on_quit)
systray.start()
