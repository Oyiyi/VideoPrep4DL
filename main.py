from pytube import YouTube
import os

def download_video_and_captions(url, video_title, file_folder):
    # Create YouTube object
    yt = YouTube(url)
    title = video_title
    script_directory = os.path.dirname(os.path.realpath(__file__))
    file_folder = file_folder
    file_name = f"{title}.mp4"
    video_file_path = os.path.join(script_directory, "output", file_folder, file_name)
    caption_folder = os.path.join(script_directory, "output", file_folder, "captions")

    # Check if the video file exists and download the video if not
    if not os.path.exists(video_file_path):
        #stream = yt.streams.get_highest_resolution()
        stream = yt.streams.filter(res="1080p").first()
        print("Downloading video...")
        stream.download(output_path=os.path.join(script_directory, "output", file_folder))
        print("Video downloaded.")
    else:
        print("Skipped downloading video as it was already downloaded.")

    # Download captions (subtitles)
    yt.bypass_age_gate()  # Temporary fix for age gate
    caption_tracks = yt.captions

    if caption_tracks:

        if not os.path.exists(caption_folder):
            os.makedirs(caption_folder)

        for caption in caption_tracks:
            caption_language = caption.code
            caption_srt = caption.xml_captions
            print(caption_srt)
            print("Downloading caption...")
            caption_file_path = os.path.join(caption_folder, f"{caption_language}.xml")
            with open(caption_file_path, "w") as file:
                file.write(caption_srt)
            print(f"Caption in {caption_language} downloaded.")

    else:
        print("No captions available for this video.")

# Example usage:
urls_file = "video_urls.txt"
with open(urls_file, "r") as file:
    video_urls_list = [line.strip() for line in file.readlines()]
    for url in video_urls_list:
        print(url)
        # url = 'https://www.youtube.com/watch?v=n0Zvshs8wzk&list=PL0eGJygpmOH6JZoTiBexaSQveslxxaLrf&index=23'
        download_video_and_captions(url, 1, "1")
