# downloading a single video

# import the module
from pytube import YouTube

# where to save
SAVE_PATH = "D:/"

# link of the video to be downloaded
link = {'https://www.youtube.com/...', 'https://www.youtube.com/...',
        'https://www.youtube.com/...'}     # line break -to avoid line being too long -properly aligned
# to check all the links use a for loop
for i in link:

    try:
        # object creation using YouTube
        yt = YouTube(i)

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


