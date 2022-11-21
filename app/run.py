#this file should become an exe which run the background app 
import subprocess

info = subprocess.STARTUPINFO()
info.dwFlags=1
info.wShowWindow=0 
subprocess.Popen(['D:\\Projects\\Github\\fast-ftp\\app\\main.py'], shell=True, creationflags=subprocess.SW_HIDE)