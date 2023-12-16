import os

# Specify the folder containing your MP4 files
folder_path = 'output/1'

# Get a list of all MP4 files in the folder
mp4_files = [f for f in os.listdir(folder_path) if f.endswith('.mp4')]

# Sort the files alphabetically to ensure sequential numbering
mp4_files.sort()

# Rename the files with sequential numbers
for index, mp4_file in enumerate(mp4_files, start=1):
    new_name = f'{index}.mp4'
    os.rename(os.path.join(folder_path, mp4_file), os.path.join(folder_path, new_name))
