# todos 1. edit the output of the ffmpeg merge; 2. maybe we could have the audio saved and simplify the rest of streamline?
# 2. reduce the music background
# 3. delete the screens that has unclear faces (mask, unclear faces in the sub-screen) / multiple faces - test it and leave room for mannual check
# potential error in the future - if the highest resolution doesn't have mp4 format and mweb only?

import os
import subprocess
from pytube import YouTube

def download_video(url, file_folder):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    file_folder = os.path.join(script_directory, "output", file_folder)
    
    # Create YouTube object
    yt = YouTube(url)
    title = yt.title
    file_name = f"{title}.mp4"

    # Show the available formats and find the highest resolution
    print("Available formats:") 
    """
    13. Resolution: 240p, Format: video/webm
    14. Resolution: 144p, Format: video/mp4
    15. Resolution: 144p, Format: video/webm
    16. Resolution: None, Format: audio/mp4
    17. Resolution: None, Format: audio/mp4
    18. Resolution: None, Format: audio/webm
    19. Resolution: None, Format: audio/webm
    20. Resolution: None, Format: audio/webm
    """
    formats = yt.streams.all()
    highest_resolution = 0  # Initialize the highest resolution as 0
    for i, stream in enumerate(formats):
        print(f"{i+1}. Resolution: {stream.resolution}, Format: {stream.mime_type}")
        # Parse the resolution and compare to find the highest
        try:
            if stream.resolution is not None: # exclude the errors from cases: "Resolution: None, Format: audio/webm"
                resolution = stream.resolution
                print(resolution)
                resolution = int(stream.resolution[:-1])  # Extract and convert resolution to an integer
                if resolution > highest_resolution:
                    highest_resolution = resolution
        except ValueError:
            pass  # Handle cases where resolution cannot be parsed (e.g., audio streams)

    # Set the highest resolution as "res"
    res = f"{highest_resolution}p"
    print(f"Highest Resolution: {res}")

    # Download based on resolution </>= 1080p (w/ first checking if the video file exists and download the video if not)
    if not os.path.exists(os.path.join(file_folder, file_name)):
        #stream = yt.streams.get_highest_resolution()  # NOT USE as "highest_resolution" capped at 720p
        print(f"Downloading a video @{res} resolution......")
        if highest_resolution < 1080:  # Check against the highest resolution
            print("<1080p download model is used")
            download_lr(stream, file_folder)
        else:
            print(">=1080p download model is used")
            download_hr(res, yt, file_folder)
        print("Video downloaded.")
    else:
        print("Skipped downloading video as it was already downloaded.")


def download_lr(stream, file_folder):
    stream.download(output_path=file_folder)

def download_hr(res, yt, file_folder):
    print(res)
    video = yt.streams.filter(res=res, mime_type="video/mp4").first()
    audio = yt.streams.filter(only_audio=True).first()
    video_filename_prefix = "video_"
    audio_filename_prefix = "audio_"
    video.download(output_path=file_folder, filename_prefix=video_filename_prefix)
    audio.download(output_path=file_folder, filename_prefix=audio_filename_prefix)
    print("Video and audio downloaded successfully!")

    # Merge video and audio
    os.chdir(file_folder)
    video_base, video_ext = os.path.splitext(video.default_filename)
    audio_base, audio_ext = os.path.splitext(audio.default_filename)
    
    # Modify the output filename format
    output_file = f"merged_{video_base}.mp4"

    subprocess.call(["ffmpeg", "-i", f"{video_filename_prefix}{video.default_filename}", "-i", f"{audio_filename_prefix}{audio.default_filename}", "-c:v", "copy", "-c:a", "copy", output_file])
    print(f"Video and audio merged successfully and saved as 'merged_{video_base}.mp4'")


# Download captions (subtitles) if available
def download_captions(yt, file_folder):
    caption_folder = os.path.join(script_directory, "output", file_folder, "captions")
    caption_track = yt.captions.get_by_language_code('en')  # Replace 'en' with the language code you want
    if caption_track:
        if not os.path.exists(caption_folder):
            os.makedirs(caption_folder)
        caption_srt = caption_track.generate_srt_captions()
        print("Downloading caption...")
        caption_file_path = os.path.join(caption_folder, f"{title}_captions.srt")
        with open(caption_file_path, "w") as file:
            file.write(caption_srt)
        print("Captions downloaded.")
    else:
        print("No captions available for this video.")

# Example usage
#download_video("https://www.youtube.com/watch?v=fGPdL65D_X4&list=PL0eGJygpmOH6JZoTiBexaSQveslxxaLrf&index=40&ab_channel=CCTV%E4%B8%AD%E5%9B%BD%E4%B8%AD%E5%A4%AE%E7%94%B5%E8%A7%86%E5%8F%B0", "output_folder")