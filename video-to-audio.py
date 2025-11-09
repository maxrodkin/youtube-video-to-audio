#download video from youtube with given url and convert it to audio file

import yt_dlp
import os
import shutil

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
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    url = "https://youtu.be/ko70cExuzZM?si=ADZANbPudo9q1s4L"
    download_video(url)