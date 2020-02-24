import os
import subprocess

from pytube import YouTube, Playlist
from pathlib import Path

playlist = Playlist("https://www.youtube.com/playlist?list=PLFu2J9pEwhz1zIjSdlS_DQXNJQfixngeF")
for link in playlist.video_urls:
	try:
		video = YouTube(link)
		stream = video.streams.filter(only_audio=True).first()
		name = stream.default_filename
		my_file = Path("/home/yme/dev/youtube-playlist-download/downloads/"+name)
		if my_file.is_file():
			print("Skipping "+name)
		else:
			stream.download()
			print("Downloaded..." + name)
	except:
		print('Error '+link)
