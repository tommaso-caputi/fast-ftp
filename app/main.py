from pynput import keyboard

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