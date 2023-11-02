from pytube import YouTube
import os
from convert_title import convert_title

# URL of the video
url = 'https://www.youtube.com/watch?v=QOaXm_9S9_0&t=1294s&ab_channel=%E4%B9%90%E8%A7%86%E8%A7%86%E9%A2%91%E5%AE%98%E6%96%B9%E9%A2%91%E9%81%93LetvOfficialChannel'

# Create YouTube object
yt = YouTube(url)
title = convert_title(yt.title)
script_directory = os.path.dirname(os.path.realpath(__file__))
file_folder = title
file_name = f"{title}.mp4"
video_file_path = os.path.join(script_directory, "output", file_folder, file_name)
caption_folder = os.path.join(script_directory, "output", file_folder, "captions")

# Check if the video file exists and download the video if not
if not os.path.exists(video_file_path):
    stream = yt.streams.get_highest_resolution()
    print("Downloading video...")
    stream.download()
    print("Video downloaded.")
else:
    print("Skipped downloading video as it was already downloaded.")

# Download captions (subtitles)
yt.bypass_age_gate() #bug temp fix
caption_tracks = yt.captions # ex:{'en': <Caption lang="English" code="en">, 'fr-FR': <Caption lang="French (France)" code="fr-FR">, 'el': <Caption lang="Greek" code="el">, 'vi': <Caption lang="Vietnamese" code="vi">}

if caption_tracks:

    if not os.path.exists(caption_folder):
        os.makedirs(caption_folder)

    for caption in caption_tracks: # ex:{'en': <Caption lang="English" code="en">, 'fr-FR': <Caption lang="French (France)" code="fr-FR">, 'el': <Caption lang="Greek" code="el">, 'vi': <Caption lang="Vietnamese" code="vi">}
        caption_language = caption.code
        caption_srt = caption.xml_captions
        print(caption_srt)
        print("Downloading caption...")
        #caption_srt = caption.generate_srt_captions() # string caption but not working
        caption_file_path = os.path.join(caption_folder, f"{caption_language}.xml")
        with open(caption_file_path, "w") as file:
            file.write(caption_srt)
        print(f"Caption in {caption_language} downloaded.")

else:
    print("No captions available for this video.")


