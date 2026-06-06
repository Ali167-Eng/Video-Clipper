import subprocess

input_video = "clips_v3/clip_1.mp4"
input_srt = "captions.srt"

output_video = "clips_v3/clip_1_subbed.mp4"

command = [
    "ffmpeg",
    "-y",
    "-i",
    input_video,
    "-vf",
    f"subtitles={input_srt}",
    output_video
]

subprocess.run(command)

print("Subtitles burned successfully!")