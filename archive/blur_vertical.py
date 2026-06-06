import subprocess

input_video = "clips_v3/clip_1_subbed.mp4"
output_video = "clips_v3/clip_1_blur.mp4"

filter_complex = (
    "[0:v]scale=1080:1920:force_original_aspect_ratio=increase,"
    "boxblur=20:10,crop=1080:1920[bg];"
    "[0:v]scale=1080:-2[fg];"
    "[bg][fg]overlay=(W-w)/2:(H-h)/2"
)

command = [
    "ffmpeg",
    "-y",
    "-i",
    input_video,
    "-filter_complex",
    filter_complex,
    "-c:a",
    "copy",
    output_video
]

subprocess.run(command)

print("Blur vertical video created!")