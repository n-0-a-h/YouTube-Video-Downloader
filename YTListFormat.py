<<<<<<< HEAD
import yt_dlp


def list_available_formats(url):
    ydl_opts = {
        "quiet": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Extract metadata without downloading anything
        info = ydl.extract_info(url, download=False)
        formats = info.get("formats", [])

        print(f"\n--- Available Formats for: {info.get('title')} ---\n")
        print(f"{'ID':<10} {'EXT':<6} {'RESOLUTION':<14} {'NOTE'}")
        print("-" * 60)

        for f in formats:
            format_id = f.get("format_id", "N/A")
            ext = f.get("ext", "N/A")
            resolution = f.get("resolution") or f"{f.get('width', '')}x{f.get('height', '')}"
            note = f.get("format_note", "") or ""

            acodec = f.get("acodec")
            vcodec = f.get("vcodec")
            has_audio = acodec not in (None, "none")
            has_video = vcodec not in (None, "none")

            # Tag each stream so silent (video-only) formats are easy to spot
            if has_audio and has_video:
                tag = " [Audio + Video]"
            elif has_video:
                tag = " [Video only - NO sound]"
            elif has_audio:
                tag = " [Audio only]"
            else:
                tag = ""

            print(f"{format_id:<10} {ext:<6} {resolution:<14} {note}{tag}")


if __name__ == "__main__":
    url = input("Enter YouTube Video URL: ").strip()
    if url:
=======
import yt_dlp

def list_available_formats(url):
    ydl_opts = {
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Extract metadata without downloading
        info = ydl.extract_info(url, download=False)
        formats = info.get('formats', [])

        print(f"\n--- Available Formats for: {info.get('title')} ---\n")
        print(f"{'ID':<10} {'EXT':<6} {'RESOLUTION':<12} {'NOTE'}")
        print("-" * 50)

        for f in formats:
            format_id = f.get('format_id', 'N/A')
            ext = f.get('ext', 'N/A')
            resolution = f.get('resolution') or f"{f.get('width', '')}x{f.get('height', '')}"
            note = f.get('format_note', '')
            
            # Highlight single pre-merged formats (no FFmpeg required)
            acodec = f.get('acodec')
            vcodec = f.get('vcodec')
            is_combined = acodec != 'none' and vcodec != 'none'
            combined_tag = " [Audio + Video]" if is_combined else ""

            print(f"{format_id:<10} {ext:<6} {resolution:<12} {note}{combined_tag}")

if __name__ == "__main__":
    url = input("Enter YouTube Video URL: ").strip()
    if url:
>>>>>>> a090fc9e9a428b03ad536521ead46e6d96229180
        list_available_formats(url)