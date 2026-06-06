
import os
import subprocess

# إنشاء فولدر الـ Vertical
os.makedirs(
    "workspace/output/verticals",
    exist_ok=True
)

clips_folder = "workspace/output/clips"
verticals_folder = "workspace/output/verticals"

for file in os.listdir(clips_folder):

    if not file.endswith(".mp4"):
        continue

    clip_name = file.replace(".mp4", "")

    input_video = os.path.join(
        clips_folder,
        file
    )

    crop_output = os.path.join(
        verticals_folder,
        f"{clip_name}_crop.mp4"
    )

    blur_output = os.path.join(
        verticals_folder,
        f"{clip_name}_blur.mp4"
    )

    print(f"\nProcessing {file}")

    # ==========================
    # CROP VERSION
    # ==========================

    crop_command = [
        "ffmpeg",
        "-y",
        "-i",
        input_video,
        "-vf",
        "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920",
        "-c:a",
        "copy",
        crop_output
    ]

    subprocess.run(crop_command)

    print(f"Created {crop_output}")

    # ==========================
    # BLUR VERSION
    # ==========================

    blur_filter = (
        "[0:v]scale=1080:1920:"
        "force_original_aspect_ratio=increase,"
        "boxblur=20:10,"
        "crop=1080:1920[bg];"
        "[0:v]scale=1080:-2[fg];"
        "[bg][fg]overlay=(W-w)/2:(H-h)/2"
    )

    blur_command = [
        "ffmpeg",
        "-y",
        "-i",
        input_video,
        "-filter_complex",
        blur_filter,
        "-c:a",
        "copy",
        blur_output
    ]

    subprocess.run(blur_command)

    print(f"Created {blur_output}")

print(
    "\nAll vertical videos created successfully!"
)

