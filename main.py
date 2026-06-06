
import subprocess
import os
import shutil

# =========================
# CREATE WORKSPACE
# =========================

os.makedirs("workspace/temp", exist_ok=True)
os.makedirs("workspace/output", exist_ok=True)

# =========================
# CLEAN TEMP FILES
# =========================

temp_files = [
    "workspace/temp/transcript.json",
    "workspace/temp/transcript.txt",
    "workspace/temp/clips.json",
    "workspace/temp/current_video.mp4"
]

for file in temp_files:

    if os.path.exists(file):
        os.remove(file)

print("\nWorkspace cleaned!")

# =========================
# VIDEO SOURCE
# =========================

print("\n1 - Local Video")
print("2 - YouTube URL")

choice = input("\nChoose option: ").strip()

video_path = ""

# =========================
# LOCAL VIDEO
# =========================

if choice == "1":

    video_path = input(
        "\nEnter video path: "
    ).strip()

    if not os.path.exists(video_path):

        print("\nVideo not found!")
        exit()

    shutil.copy(
        video_path,
        "workspace/temp/current_video.mp4"
    )

# =========================
# YOUTUBE VIDEO
# =========================

elif choice == "2":

    url = input(
        "\nEnter YouTube URL: "
    ).strip()

    print("\nDownloading video...")

    result = subprocess.run(
        [
            "python",
            "download_youtube.py",
            url
        ]
    )

    if result.returncode != 0:

        print("\nDownload failed!")
        exit()

else:

    print("\nInvalid option!")
    exit()

# =========================
# USE WORKSPACE VIDEO
# =========================

video_path = "workspace/temp/current_video.mp4"

# =========================
# TRANSCRIBE
# =========================

print("\n" + "=" * 60)
print("RUNNING: transcribe.py")
print("=" * 60)

result = subprocess.run(
    [
        "python",
        "transcribe.py",
        video_path
    ]
)

if result.returncode != 0:

    print("\nFAILED: transcribe.py")
    exit()

# =========================
# PIPELINE
# =========================

PIPELINE = [

    "modules/auto_cutter_v3.py",

    "modules/cutter.py",

    "modules/generate_all_srt.py",

    "modules/generate_verticals.py",

    "modules/burn_subtitles_pro.py"

]

for script in PIPELINE:

    print("\n" + "=" * 60)
    print(f"RUNNING: {script}")
    print("=" * 60)

    result = subprocess.run(
        [
            "python",
            script
        ]
    )

    if result.returncode != 0:

        print(f"\nFAILED: {script}")
        exit()

print("\n" + "=" * 60)
print("PIPELINE FINISHED SUCCESSFULLY!")
print("=" * 60)

