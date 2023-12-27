from pytube import YouTube
import os
from download import download_video

# Example usage:
urls_file = "video_urls.txt"
with open(urls_file, "r") as file:
    video_urls_list = [line.strip() for line in file.readlines()]
    for url in video_urls_list:
        print(url)
        download_video(url, "1")
