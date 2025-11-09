# YouTube Video to Audio Converter

A simple Python script that downloads YouTube videos and converts them to MP3 audio files.

## Prerequisites

### System Requirements
- Python 3.7 or higher
- FFmpeg (for audio conversion)

### Installing FFmpeg

**macOS:**
```bash
brew install ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ffmpeg
```

**Windows:**
1. Download FFmpeg from https://ffmpeg.org/download.html
2. Extract the files and add the `bin` folder to your system PATH
3. Restart your command prompt/terminal

## Installation

1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd video-to-audio
   ```
3. (Optional but recommended) Create and activate a virtual environment:

    **macOS/Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    **Windows:**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```
3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Method 1: Edit the script
1. Open `video-to-audio.py`
2. Replace the URL in the script with your desired YouTube URL:
   ```python
   url = "https://youtu.be/YOUR_VIDEO_ID"
   ```
3. Run the script:
   ```bash
   python video-to-audio.py
   ```

### Method 2: Command line (modify script for input)
The script can be easily modified to accept command line arguments or user input.

## Features

- Downloads best available audio quality from YouTube
- Converts to MP3 format (192kbps)
- Saves files to `downloads/` folder
- Uses video title as filename
- Checks for FFmpeg availability before processing

## Output

Downloaded audio files will be saved in the `downloads/` directory with the format:
```
downloads/Video Title.mp3
```

## Troubleshooting

**Error: FFmpeg not found**
- Make sure FFmpeg is properly installed and added to your system PATH
- Restart your terminal after installing FFmpeg

**HTTP Error 400: Bad Request**
- This usually means YouTube has updated their API
- Try updating yt-dlp: `pip install --upgrade yt-dlp`

**Permission errors**
- Make sure you have write permissions in the project directory
- The script will create the `downloads/` folder automatically

## Dependencies

- `yt-dlp`: YouTube video downloader
- `FFmpeg`: Audio/video processing tool (system dependency)

## License

This project is for educational purposes. Please respect YouTube's Terms of Service and copyright laws.
