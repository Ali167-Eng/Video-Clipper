
import yt_dlp
import sys
import os

# إنشاء الفولدرات
os.makedirs("workspace/temp", exist_ok=True)

if len(sys.argv) < 2:
    print("Usage: python download_youtube.py URL")
    exit()

url = sys.argv[1]

# حذف الفيديو القديم لو موجود
output_path = "workspace/temp/current_video.mp4"

if os.path.exists(output_path):
    try:
        os.remove(output_path)
    except:
        pass

ydl_opts = {
    "format": "bestvideo+bestaudio/best",
    "merge_output_format": "mp4",
    "outtmpl": output_path,
    "quiet": False
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download complete!")

