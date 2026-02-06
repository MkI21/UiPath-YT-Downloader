import os
import sys
import re
from yt_dlp import YoutubeDL

#Fonctions 
def sanitize_folder(name):
    """Normalize folder names: remove invalid chars, trim spaces, collapse spaces."""
    name = name.strip()
    name = re.sub(r'[\/:*?"<>|]', '_', name)  # replace invalid filesystem chars
    name = re.sub(r'\s+', ' ', name)          # collapse multiple spaces
    return name

def find_existing_artist_folder(base_folder, artist_name):
    """Check if a folder for the artist already exists (ignores case and formatting)."""
    artist_safe = sanitize_folder(artist_name).lower()
    for folder in os.listdir(base_folder):
        if os.path.isdir(os.path.join(base_folder, folder)) and sanitize_folder(folder).lower() == artist_safe:
            return os.path.join(base_folder, folder)
    return None

# Read arguments
artist = sys.argv[1]
song = sys.argv[2]

# Base folder
base_folder = r"C:\Music"
os.makedirs(base_folder, exist_ok=True)

# Determine artist folder
existing_folder = find_existing_artist_folder(base_folder, artist)
if existing_folder:
    artist_folder = existing_folder
else:
    artist_folder = os.path.join(base_folder, sanitize_folder(artist))
    os.makedirs(artist_folder, exist_ok=True)

# Output file template
song_safe = sanitize_folder(song)
output_template = os.path.join(artist_folder, f"{song_safe}.%(ext)s")

#  yt-dlp options 
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': output_template,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '0',
    }],
    'ffmpeg_location': r"C:\Users\mkl\Downloads\ffmpeg\ffmpeg\bin",
}

# Download song
query = f"ytsearch1:{artist} {song}"
with YoutubeDL(ydl_opts) as ydl:
    ydl.download([query])

print(f"Downloaded: {artist} - {song}")
