
import json
import os

# إنشاء فولدر الـ SRT
os.makedirs(
    "workspace/output/srt",
    exist_ok=True
)

def format_time(seconds):

    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int(
        (seconds - int(seconds)) * 1000
    )

    return (
        f"{hours:02}:"
        f"{minutes:02}:"
        f"{secs:02},"
        f"{millis:03}"
    )

# قراءة الـ Transcript
with open(
    "workspace/temp/transcript.json",
    "r",
    encoding="utf-8"
) as f:

    segments = json.load(f)

# قراءة الكليبات
with open(
    "workspace/temp/clips.json",
    "r",
    encoding="utf-8"
) as f:

    clips = json.load(f)

# إنشاء SRT لكل كليب
for clip in clips:

    clip_id = clip["id"]

    clip_start = clip["start"]

    clip_end = (
        clip_start +
        clip["duration"]
    )

    output_file = (
        f"workspace/output/srt/"
        f"clip_{clip_id}.srt"
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as srt:

        index = 1

        for segment in segments:

            if (
                segment["end"] < clip_start
                or
                segment["start"] > clip_end
            ):
                continue

            start = max(
                segment["start"],
                clip_start
            )

            end = min(
                segment["end"],
                clip_end
            )

            start -= clip_start
            end -= clip_start

            srt.write(
                f"{index}\n"
            )

            srt.write(
                f"{format_time(start)} --> "
                f"{format_time(end)}\n"
            )

            srt.write(
                segment["text"].strip()
                + "\n\n"
            )

            index += 1

    print(
        f"Created clip_{clip_id}.srt"
    )

print(
    "\nAll SRT files created successfully!"
)

