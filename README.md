# YT Video Downloader

A small Python tool for downloading YouTube videos (with sound) to your PC, built on [yt-dlp](https://github.com/yt-dlp/yt-dlp) and FFmpeg.

## Files

| File | Purpose |
|------|---------|
| `YTdownloader.py` | Downloads a video into a `downloads` folder. Detects FFmpeg automatically and picks the best format that includes sound. |
| `YTListFormat.py` | Lists every format available for a video and tags each as audio + video, video only, or audio only. |

> The instructions below are written for Windows. Other operating systems are noted where the commands differ.

## Requirements

### 1. Python

```powershell
python --version
# If "python" is not recognised, try the Python Launcher:
py --version
```

If neither works, install Python and tick **Add python.exe to PATH** during setup:

```powershell
winget install Python.Python.3.12
```

### 2. yt-dlp (the download library)

```powershell
pip install yt-dlp
```

If `pip` is not recognised, use the Python Launcher:

```powershell
py -m pip install yt-dlp
```

> **Note:** `winget install yt-dlp` and `choco install yt-dlp` install the standalone command-line program, not the Python library. These scripts use `import yt_dlp`, so they need the `pip` version.

### 3. FFmpeg (needed for sound at high quality)

YouTube stores high-quality video and audio as separate streams. FFmpeg merges them into one file.

```powershell
winget install FFmpeg
```

Close and reopen your terminal afterwards, then check it works:

```powershell
ffmpeg -version
```

Other systems: `brew install ffmpeg` (macOS) or `sudo apt install ffmpeg` (Debian/Ubuntu).

### Keeping yt-dlp up to date

YouTube changes often, and an outdated yt-dlp is the most common cause of sudden errors.

```powershell
pip install -U yt-dlp
```

## Usage

Open a terminal in the project folder:

```powershell
cd "C:\path\to\your\project"
```

**(Optional) List available formats:**

```powershell
python YTListFormat.py
```

**Download a video:**

```powershell
python YTdownloader.py
```

Paste the video URL when prompted. The file is saved in the `downloads` folder.

### Full first-time setup

```powershell
winget install Python.Python.3.12
winget install FFmpeg
# --- close and reopen the terminal here ---
python --version
ffmpeg -version
pip install yt-dlp
cd "C:\path\to\your\project"
python YTdownloader.py
```

## Problems we ran into (and the fixes)

### Downloaded videos had no sound

The script requested format `137`, which is a **video-only** stream (1080p H.264 MP4). YouTube delivers higher-quality videos as separate video and audio streams, so `137` has no audio track.

**Fix:** request video and audio together and let FFmpeg merge them:

```python
'format': 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best',
'merge_output_format': 'mp4',
```

### FFmpeg is required for merging

Without FFmpeg, the only way to get sound is a pre-merged format such as `18`, limited to about 360p. The script now checks for FFmpeg on start-up and falls back automatically, printing a message if it is missing.

### Other issues

- **`pip` not recognised:** Python is not on PATH. Use `py -m pip ...` or reinstall Python with "Add to PATH" ticked.
- **Library vs. program confusion:** winget/choco install the yt-dlp program, not the Python library. Use `pip`.
- **Unmaintained libraries:** `pytube` and `youtube-dl` no longer keep up with YouTube. Use `yt-dlp`.
- **Ambiguous format list:** `YTListFormat.py` now tags every stream explicitly instead of only flagging combined ones.

## How the format string works

yt-dlp tries each option from left to right and uses the first one available:

| Part | Meaning |
|------|---------|
| `bestvideo[height<=1080][ext=mp4]` | Best MP4 video stream up to 1080p (video only) |
| `+bestaudio[ext=m4a]` | Plus the best M4A audio stream; FFmpeg merges the two |
| `/bestvideo[height<=1080]+bestaudio` | Fallback: any container, still merged |
| `/best[height<=1080]` | Fallback: best single pre-merged file up to 1080p |
| `/best` | Last resort: best single file |
| `merge_output_format: 'mp4'` | Forces the merged result to be an `.mp4` |

To change the maximum quality, edit `max_height` in `download_youtube_video` (for example `720`, `1440` or `2160`).

## Troubleshooting

| Symptom | What to try |
|---------|-------------|
| No sound in the file | Run `ffmpeg -version`. If not found, install FFmpeg and reopen the terminal. |
| `'ffmpeg' is not recognized` | Reopen the terminal after installing, or add FFmpeg's `bin` folder to PATH. |
| `ModuleNotFoundError: yt_dlp` | Run `pip install yt-dlp` using the same Python that runs the script. |
| HTTP 403 / "unable to extract" | Update yt-dlp: `pip install -U yt-dlp` |
| Requested format is not available | Run `YTListFormat.py` to see what is offered, or lower `max_height`. |
| Age-restricted, private or members-only video | These need a signed-in session and are not supported by this script. |

## Disclaimer

Only download content you own, have permission to use, or that is licensed for downloading. Downloading may breach YouTube's Terms of Service.