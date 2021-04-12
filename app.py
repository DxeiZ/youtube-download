import tkinter as tk
from tkinter import ttk
import os
from pytube import YouTube
from tkinter import messagebox as m_box
import subprocess
import threading

def onClick():
    got_link = link.get()
    got_path = path.get()
    try:
        yt = YouTube(str(got_link))
    except:
        m_box.showerror("ERROR", "There was a problem with the connection!")
    else:
        vid = yt.streams.get_highest_resolution()
        destination = str(got_path)
        vid.download(destination)
        os.startfile(got_path)
        return m_box.showinfo('SUCCES', f"Successfully saved video named {yt.title} to {got_path} folder!")


threads = []


def startThredProcess():
    myNewThread = threading.Thread(target=onClick)
    threads.append(myNewThread)
    myNewThread.start()

win = tk.Tk()
for i in range(3):
    win.columnconfigure(i, weight=1, minsize=75)
    win.rowconfigure(i, weight=1, minsize=50)
win.geometry("500x300")
win.title("Youtube Video Downloader - Krios Software")
frame = ttk.LabelFrame(master=win, relief=tk.RAISED, borderwidth=0)
frame.grid(row=0, column=0, padx=50, pady=50)
frame.pack()
get_info = ttk.Label(master=frame, text="Youtube Link")
get_info.place(x=0, y=0)
get_info.grid(row=0, column=0, sticky=tk.W)

link = tk.StringVar()

yt_link = ttk.Entry(frame, width=75, textvariable=link)
yt_link.grid(row=1, columnspan=1, padx=0, pady=3)
yt_link.focus()


get_info = ttk.Label(master=frame, text="File Name")
get_info.place(x=0, y=0)
get_info.grid(row=2, column=0, sticky=tk.W)

path = tk.StringVar()

download_path = ttk.Entry(frame, width=75, textvariable=path)
download_path.grid(row=3, columnspan=1, padx=0, pady=3)

btn1 = ttk.Button(frame, text="Start", width=75, command=startThredProcess)
btn1.grid(row=5, columnspan=1, padx=13, pady=7)

win.mainloop()