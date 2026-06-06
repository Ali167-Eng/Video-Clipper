
import json
import subprocess
import os

# إنشاء الفولدرات
os.makedirs("workspace/output/clips", exist_ok=True)

# قراءة الكليبات المختارة
with open(
    "workspace/temp/clips.json",
    "r",
    encoding="utf-8"
) as f:
    clips = json.load(f)

# قص الكليبات
for clip in clips:

    clip_id = clip["id"]
    start = clip["start"]
    duration = clip["duration"]

    output_file = (
        f"workspace/output/clips/clip_{clip_id}.mp4"
    )

    command = [
        "ffmpeg",
        "-y",
        "-ss",
        str(start),
        "-i",
        "workspace/temp/current_video.mp4",
        "-t",
        str(duration),
        "-c",
        "copy",
        output_file
    ]

    subprocess.run(command)

    print(
        f"Created clip_{clip_id}.mp4 | "
        f"Start={start}s | "
        f"Duration={duration}s"
    )

print("\nAll clips created successfully!")

