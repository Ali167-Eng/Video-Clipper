import json

CLIP_START = 0
CLIP_END = 60

def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)

    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"

with open("transcript.json", "r", encoding="utf-8") as f:
    segments = json.load(f)

with open("clip_1.srt", "w", encoding="utf-8") as srt:

    index = 1

    for segment in segments:

        if (
            segment["end"] < CLIP_START
            or
            segment["start"] > CLIP_END
        ):
            continue

        start = max(segment["start"], CLIP_START)
        end = min(segment["end"], CLIP_END)

        start -= CLIP_START
        end -= CLIP_START

        srt.write(f"{index}\n")
        srt.write(
            f"{format_time(start)} --> {format_time(end)}\n"
        )
        srt.write(
            segment["text"].strip() + "\n\n"
        )

        index += 1

print("clip_1.srt created!")