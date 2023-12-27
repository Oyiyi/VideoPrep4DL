from pytube import YouTube
import os

urls_file = "video_urls.txt"

# Define a function to download a video given its URL and save it as "1.mp4"
def download_video(video_url, output_folder):
    # Create YouTube object
    yt = YouTube(video_url)
    title = yt.title

    # Check if the video file exists and download the video if not
    video_file_path = os.path.join(output_folder, "1.mp4")
    if not os.path.exists(video_file_path):
        stream = yt.streams.get_highest_resolution()
        #yt.streams.filter(res="1080p").first().download(output_path=output_folder, filename="1")
        stream.download(output_path=output_folder, filename="1")
        print(f"Video '{title}' downloaded as '1.mp4' in folder '{output_folder}'.")
    else:
        print(f"Skipped downloading video '{title}' as it was already downloaded.")

# Read video URLs from "video_urls.txt"
with open(urls_file, "r") as file:
    video_urls = [line.strip() for line in file.readlines()]

# Create a directory to store downloaded videos if it doesn't exist
output_directory = "output"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Iterate through the list of video URLs
for i, video_url in enumerate(video_urls, start=1):
    # Create a folder for each video
    folder_name = str(i)
    folder_path = os.path.join(output_directory, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Download the video into the folder and name it "1.mp4"
    download_video(video_url, folder_path)

print("All videos downloaded as '1.mp4' in their respective folders.")
