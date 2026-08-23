import yt_dlp

def download_youtube_video(url, output_path="./downloads"):
    ydl_opts = {
        # Format 18 is YouTube's legacy pre-merged MP4 stream (includes audio+video).
        # Fallbacks to 'worst' to grab whatever pre-merged file exists.
        'format': '18',
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
        download_youtube_video(video_url)