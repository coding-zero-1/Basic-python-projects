import tkinter
import customtkinter
from pytube import YouTube

def download_video():
    pass

#system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

#app frame
app=customtkinter.CTk()
app.geometry("720×480")
app.title("YouTube Downloader")

#adding UI Elements
title=customtkinter.CTkLabel(app,text="Insert a YouTube link")
title.pack(padx=10,pady=10)

url_var=tkinter.StringVar()
link=customtkinter.CTkEntry(app,width=400,height=60,corner_radius=10,textvariable=url_var)
link.pack()

#download button
download=customtkinter.CTkButton(app,width=50,height=50,textvariable=download_video)
download.pack()
#Run app as a loop to keep it open
app.mainloop()