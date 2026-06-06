
import os
import subprocess

# إنشاء فولدر الفيديوهات النهائية
os.makedirs(
    "workspace/output/final_videos",
    exist_ok=True
)

verticals_folder = "workspace/output/verticals"
srt_folder = "workspace/output/srt"
final_folder = "workspace/output/final_videos"

for file in os.listdir(verticals_folder):

    if not file.endswith(".mp4"):
        continue

    clip_id = file.split("_")[1]

    input_video = os.path.join(
        verticals_folder,
        file
    )

    output_video = os.path.join(
        final_folder,
        file.replace(".mp4", "_pro.mp4")
    )

    subtitle_filter = (
        f"subtitles={srt_folder}/clip_{clip_id}.srt:"
        "force_style="
        "'FontName=Arial,"
        "FontSize=9,"
        "PrimaryColour=&HFFFFFF&,"
        "OutlineColour=&H000000&,"
        "BackColour=&H000000&,"
        "Outline=2,"
        "Shadow=1,"
        "Bold=1,"
        "Alignment=2,"
        "MarginV=20'"
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

print("\nDone!")

