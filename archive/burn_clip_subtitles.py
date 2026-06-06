import subprocess

input_video = "clips_v3/clip_1_blur.mp4"
input_srt = "clip_1.srt"

output_video = "clips_v3/clip_1_final.mp4"

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

print("Final short created!")