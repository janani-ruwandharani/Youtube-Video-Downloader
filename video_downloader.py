# downloading a single video

# import the module
from pytube import YouTube

# where to save
SAVE_PATH = "D:/"

# link of the video to be downloaded
link = 'https://www.youtube.com/.........'

try:
    # object creation using YouTube
    yt = YouTube(link)

except:
    print("Connection Failure")


# get the video with the extension and resolution
d_video = yt.streams.get_highest_resolution()

try:
    # download the video
    d_video.download(SAVE_PATH)

except:
    print("An Error Occurred")

print('Task Completed')


