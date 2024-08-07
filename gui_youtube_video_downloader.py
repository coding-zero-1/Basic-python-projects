import tkinter
import customtkinter
from pytube import YouTube

def download_video():
    try:
        yt_link=link.get()
        youtube_object=YouTube(yt_link)
        video=youtube_object.streams.get_by_resolution("720p")
        video.download()
        print("Download complete")
    except:
        print("There is an error!!")


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
download=customtkinter.CTkButton(app,width=50,height=50,text="Download video",command=download_video)
download.pack(padx=10,pady=10)
#Run app as a loop to keep it open
app.mainloop()