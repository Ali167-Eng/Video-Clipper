import os
import subprocess

os.makedirs("final_videos", exist_ok=True)

for file in os.listdir("verticals"):

    if not file.endswith(".mp4"):
        continue

    clip_id = file.split("_")[1]

    input_video = os.path.join(
        "verticals",
        file
    )

    output_video = os.path.join(
        "final_videos",
        file.replace(".mp4", "_final.mp4")
    )

    subtitle_filter = (
        f"subtitles=srt/clip_{clip_id}.srt"
    )

    command = [
        "ffmpeg",
        "-y",
        "-i",
        input_video,
        "-vf",
        subtitle_filter,
        "-c:a",
        "copy",
        output_video
    ]

    print(f"\nProcessing: {file}")

    subprocess.run(command)

print("\nAll final videos created!")