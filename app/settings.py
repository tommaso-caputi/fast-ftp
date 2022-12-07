from tkinter.filedialog import askopenfilenames
import tkinter
import customtkinter

def set_file_paths(): #need to be fixed
    filepaths = askopenfilenames() 
    paths = "FILES = "
    with open(".env", "w") as f:
        for path in filepaths:
            paths += path+"-"
        paths = paths[:-1]
        f.write(paths)
    return paths

def get_values():
    values = {}
    with open(".env","r") as f:
        line = str(f.read())
        line = str(line).split()
        for i in range(0, int(len(line)), 3):
            values[line[i]] = line[i+2]
    return values    

#def settings(systray):
def settings():
    root_tk = tkinter.Tk()
    root_tk.geometry("500x270")
    root_tk.title("CustomTkinter Test")
    root_tk.eval('tk::PlaceWindow . center')
    root_tk.resizable(False, False)
    def update():
        with open(".env","w") as f:
            for i in range(len(keys)):
                new_line = keys[i]+" = "+entrys[i].get()+"\n"
                f.write(new_line)
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

#def run(systray):
def run():
    settings()

run()