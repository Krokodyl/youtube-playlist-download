import os
import subprocess

from pytube import YouTube, Playlist
from pytube.exceptions import VideoUnavailable
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
	print(count)
	if count < start:
		count = count+1
		continue
	
	# file exists
	try:
		stream = video.streams.filter(only_audio=True).first()
		name = stream.default_filename
		print("Downloading..." + name)
		my_file = Path("D:/git/youtube-playlist-download/downloads/"+name)
		if my_file.is_file():
			print("Skipping "+name)
		else:
			stream.download()
	except VideoUnavailable:
		print("VideoUnavailable")
		continue

print("Done...")