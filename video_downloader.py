# downloading a single video

# import the required modules
from tkinter import *
from pytube import YouTube

#set the gui window

root = Tk()  # create the root object
root.geometry('500x300')  #set the window size
root.resizable(0,0)  #set thefixed size of the window
root.title('My Youtube Downloader')  # name the window


# use the Label() widget to display the static text that the users cannot modify
Label(root, text='Youtube Video Downloader', font='arial 20 bold').pack
# root refers the window
# pack organize widget in the block

# where to save
SAVE_PATH = "D:/movies"

# link of the video to be downloaded
#link = {'https://www.youtube.com/watch?v=PYBIrAZ7KV4', 'https://www.youtube.com/watch?v=mdu5lLpMH_w',
        #'https://www.youtube.com/watch?v=tCjwDv5xGsM '}     # line break -to avoid line being too long -properly aligned

# create field to enter the link
link = StringVar()

Label(root, text='Enter the Video Link', font='arial 15 bold').place(x=160, y=60)
# place used to place the widget at a specified position

link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=90)
# Entry() widget is used when we want to create an input text field
# width sets the width of the Entry widget
# textvariable retrieve the current textvariable into Entry() widget


# video downloader function
def download():
    # object creation using YouTube
    yt = YouTube(str(link.get()))
    # get the video with the extension and resolution
    d_video = yt.streams.get_highest_resolution()
    # download the video
    d_video.download(SAVE_PATH)
    Label(root, text='DOWNLOADED', font='arial 15').place(x=180, y=210)

Button(root, text='DOWNLOAD', font='arial 15 bold', bg='pale violet red', padx=2, command=download).place(x=180, y=150)
# this creates a button on the window
# command is used to call the function

root.mainloop()
# This get executed when we run the program








