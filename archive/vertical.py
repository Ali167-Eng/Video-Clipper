import subprocess

input_video = "clips_v3/clip_1_subbed.mp4"
output_video = "clips_v3/clip_1_vertical.mp4"

command = [
    "ffmpeg",
    "-y",
    "-i",
    input_video,
    "-vf",
    "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920",
    "-c:a",
    "copy",
    output_video
]

subprocess.run(command)

print("Vertical video created!")