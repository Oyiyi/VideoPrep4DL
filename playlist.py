from pytube import Playlist

# Playlist URL
playlist_url = "https://www.youtube.com/playlist?list=PL0eGJygpmOH6JZoTiBexaSQveslxxaLrf"

# Create a Playlist object
playlist = Playlist(playlist_url)

# Get all the video URLs in the playlist and save them in a list
video_urls = playlist.video_urls

# Convert the list of video URLs to strings and save in a new list
video_url_list = [str(url) for url in video_urls]

# Save the list of video URLs into a text file
with open("video_urls.txt", "w") as file:
    for url in video_url_list:
        file.write(url + "\n")

print("Video URLs saved to video_urls.txt")
