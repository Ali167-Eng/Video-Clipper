import yt_dlp

url = input("Enter YouTube URL: ")

ydl_opts = {
    "format": "bestvideo+bestaudio/best",
    "merge_output_format": "mp4",
    "outtmpl": "video.%(ext)s"
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download completed!")