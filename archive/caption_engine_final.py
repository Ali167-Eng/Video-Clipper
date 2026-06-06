import json

INPUT_FILE = "transcript.json"
OUTPUT_FILE = "captions_final.srt"

BREAK_WORDS = {
    "because",
    "and",
    "but",
    "so",
    "then",
    "however",
    "while",
    "although"
}


def sec_to_srt(seconds):

    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)

    return (
        f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"
    )


def smart_split(text):

    words = text.split()

    if len(words) <= 10:
        return [text]

    center = len(words) // 2

    split_index = None

    for offset in range(6):

        left = center - offset
        right = center + offset

        if (
            left > 0
            and words[left].lower() in BREAK_WORDS
        ):
            split_index = left
            break

        if (
            right < len(words)
            and words[right].lower() in BREAK_WORDS
        ):
            split_index = right
            break

    if split_index is None:
        split_index = center

    first = " ".join(words[:split_index]).strip()
    second = " ".join(words[split_index:]).strip()

    return [first, second]


with open(INPUT_FILE, "r", encoding="utf-8") as f:
    segments = json.load(f)

captions = []
caption_id = 1

for seg in segments:

    text = seg["text"].strip()

    if not text:
        continue

    parts = smart_split(text)

    start = seg["start"]
    end = seg["end"]

    duration = end - start

    if len(parts) == 1:

        captions.append(
            {
                "start": start,
                "end": end,
                "text": parts[0]
            }
        )

    else:

        midpoint = start + duration / 2

        captions.append(
            {
                "start": start,
                "end": midpoint,
                "text": parts[0]
            }
        )

        captions.append(
            {
                "start": midpoint,
                "end": end,
                "text": parts[1]
            }
        )

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
    f"Created {OUTPUT_FILE}"
)