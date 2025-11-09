#download video from youtube with given url and convert it to audio file

import yt_dlp
import os
import shutil
import sys

def check_ffmpeg():
    """Check if FFmpeg is installed and available in PATH"""
    if not shutil.which('ffmpeg'):
        print("Error: FFmpeg is not installed or not found in PATH")
        print("Please install FFmpeg:")
        print("  macOS: brew install ffmpeg")
        print("  Ubuntu/Debian: sudo apt install ffmpeg")
        print("  Windows: Download from https://ffmpeg.org/download.html")
        return False
    return True

def download_video(url):
    # Check if FFmpeg is available
    if not check_ffmpeg():
        return False
        
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'restrictfilenames': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {os.path.basename(__file__)} <YouTube_URL>")
        sys.exit(1)
    url = sys.argv[1]
    if not url.startswith("http"):
        print("Error: Invalid URL.")
        print(f"Usage: python {os.path.basename(__file__)} <YouTube_URL>")
        sys.exit(1)
    download_video(url)