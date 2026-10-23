<<<<<<< HEAD
import shutil
import yt_dlp


def ffmpeg_installed():
    """Return True if FFmpeg can be found on the system PATH."""
    return shutil.which("ffmpeg") is not None


def build_options(output_path, max_height):
    """Build yt-dlp options depending on whether FFmpeg is available."""
    opts = {
        "outtmpl": f"{output_path}/%(title)s.%(ext)s",
        "quiet": False,
    }

    if ffmpeg_installed():
        # Best video (up to max_height) + best audio, merged into one MP4.
        # Fallbacks are tried left to right if a combination is unavailable.
        opts["format"] = (
            f"bestvideo[height<={max_height}][ext=mp4]+bestaudio[ext=m4a]"
            f"/bestvideo[height<={max_height}]+bestaudio"
            f"/best[height<={max_height}]"
            "/best"
        )
        opts["merge_output_format"] = "mp4"
        print(f"FFmpeg found: downloading up to {max_height}p with sound.")
    else:
        # No FFmpeg: only pre-merged (audio + video) files can be used.
        # On YouTube this is usually format 18 (360p MP4).
        opts["format"] = "best[ext=mp4]/best"
        print("FFmpeg NOT found: falling back to a pre-merged file (low quality, ~360p).")
        print("Install FFmpeg (winget install FFmpeg) for higher quality with sound.\n")

    return opts


def download_youtube_video(url, output_path="./downloads", max_height=1080):
    ydl_opts = build_options(output_path, max_height)

    try:
        print(f"Starting download for: {url}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    video_url = input("Enter YouTube Video URL: ").strip()
    if video_url:
=======
import yt_dlp

def download_youtube_video(url, output_path="./downloads"):
    ydl_opts = {
        # Format 18 is YouTube's legacy pre-merged MP4 stream (includes audio+video).
        # Fallbacks to 'worst' to grab whatever pre-merged file exists.
        'format': '137',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'quiet': False,
    }

    try:
        print(f"Starting download for: {url}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter YouTube Video URL: ").strip()
    if video_url:
>>>>>>> a090fc9e9a428b03ad536521ead46e6d96229180
        download_youtube_video(video_url)