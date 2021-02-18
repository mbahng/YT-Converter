# importing module
import youtube_dl
import os

ydl_opts = {}

def dwl_vid():
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([zxt])

channel = 1
while (channel == int(1)):
    link_of_the_video = input("Input the link: ")
    zxt = link_of_the_video.strip()
    dwl_vid()
    channel = int(input("Enter 1 if you want to download more videos \nEnter 0 if you are done "))

directory = f"/Users/mbahng/PycharmProjects/YTtoMP3Converter"
for filename in os.listdir(directory):
    if filename.endswith(".mp4"):
        os.rename(f"{directory}/{filename}", f"/Users/mbahng/Desktop/{filename}")


