import os
import subprocess

from pytube import YouTube, Playlist
from pathlib import Path

print("Downloading...")
# yt = YouTube("https://youtu.be/rCrkSxcuhl0?list=PLFu2J9pEwhz0Zf_PWs-cSakqnRZBfRIo9")

# accessing audio streams of YouTube obj.(first one, more available)
#stream = yt.streams.filter(only_audio=True).first()
# downloading a video would be: stream = yt.streams.first()

# download into working directory
#stream.download()

count = 0
start = 88

playlist = Playlist("https://www.youtube.com/playlist?list=PLFu2J9pEwhz1zIjSdlS_DQXNJQfixngeF")
for video in playlist.videos:
	print("video.title")
print("Done...")
