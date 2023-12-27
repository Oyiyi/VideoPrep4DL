import importlib.util
import subprocess
import sys
import os
 
# Check if PyTube is installed
if importlib.util.find_spec("pytube") is None:
    print("PyTube not found. Installing...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pytube"])
    except Exception as e:
        print("An error occurred while installing PyTube:", e)
 
# Import PyTube
from pytube import YouTube
 
# Enter the YouTube video URL
url = input("Enter the YouTube video URL: ")
 
# Create a YouTube object
yt = YouTube(url)
 
# Show the available formats
print("Available formats:")
formats = yt.streams.all()
for i, stream in enumerate(formats):
    print(f"{i+1}. Resolution: {stream.resolution}, Format: {stream.mime_type}")
 
# Select the format to download
choice = int(input("Enter the number of the format to download: "))
if choice not in range(1, len(formats)+1):
    print("Invalid choice.")
    sys.exit(1)
 
stream = formats[choice-1]
 
# Download the video or audio
choice = input("Enter 'a' to download as audio or 'v' to download as video: ")
output_path = os.path.join(os.path.expanduser("~"), "Desktop")
if choice == "a":
    audio = stream.streams.filter(only_audio=True).first()
    audio.download(filename_prefix="audio_", output_path=output_path)
    print("Audio downloaded successfully!")
 
    # Convert the audio to mp3
    os.chdir(output_path)
    base, ext = os.path.splitext(audio.default_filename)
    new_file = f"{base}.mp3"
    subprocess.call(["ffmpeg", "-i", f"{audio.default_filename}", new_file])
    os.remove(audio.default_filename)
    print("Audio converted to MP3 successfully!")
 
elif choice == "v":
    video = stream.streams.filter(resolution=stream.resolution, mime_type="video/mp4", only_video=True).first()
    audio = stream.streams.filter(only_audio=True).first()
 
    video.download(filename_prefix="video_", output_path=output_path)
    audio.download(filename_prefix="audio_", output_path=output_path)
 
    print("Video and audio downloaded successfully!")
 
    # Merge video and audio
    os.chdir(output_path)
    video_base, video_ext = os.path.splitext(video.default_filename) # default_filename: original filename of the media file available on YouTube
    audio_base, audio_ext = os.path.splitext(audio.default_filename)
    output_file = f"{video_base}_merged.mp4"
    
    subprocess.call(["ffmpeg", "-i", video.default_filename, "-i", audio.default_filename, "-c:v", "copy", "-c:a", "copy", output_file])
 
    os.remove(video.default_filename)
    os.remove(audio.default_filename)
    print("Video and audio merged successfully!")
    
else:
    print("Invalid choice.")