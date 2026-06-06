import json
import os

INPUT_FILE = "transcript.json"
OUTPUT_FILE = "captions_v3.srt"

MAX_WORDS = 8
MIN_WORDS = 4

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    segments = json.load(f)

captions = []
caption_id = 1


def sec_to_srt(seconds):

    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)

    return (
        f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"
    )


for seg in segments:

    text = seg["text"].strip()

    if not text:
        continue

    words = text.split()

    start = seg["start"]
    end = seg["end"]

    duration = end - start

    if len(words) <= MAX_WORDS:

        captions.append({
            "start": start,
            "end": end,
            "text": text
        })

        continue

    chunks = []

    current = []

    for word in words:

        current.append(word)

        if len(current) >= MAX_WORDS:

            chunks.append(current)
            current = []

    if current:
        chunks.append(current)

    total_words = len(words)

    current_time = start

    for chunk in chunks:

        chunk_words = len(chunk)

        chunk_duration = (
            duration *
            (chunk_words / total_words)
        )

        chunk_start = current_time
        chunk_end = current_time + chunk_duration

        chunk_text = " ".join(chunk)

        captions.append({
            "start": chunk_start,
            "end": chunk_end,
            "text": chunk_text
        })

        current_time = chunk_end


with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as f:

    for i, cap in enumerate(captions, start=1):

        f.write(f"{i}\n")

        f.write(
            f"{sec_to_srt(cap['start'])} --> "
            f"{sec_to_srt(cap['end'])}\n"
        )

        f.write(cap["text"] + "\n\n")

print(
    f"Created {OUTPUT_FILE} "
    f"with {len(captions)} captions"
)