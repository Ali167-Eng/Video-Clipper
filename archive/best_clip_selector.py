import json

WINDOW_SIZE = 45
STEP = 15

keywords = {
    "rich": 5,
    "money": 4,
    "million": 5,
    "success": 5,
    "secret": 4,
    "mistake": 4,
    "best": 3,
    "never": 3,
    "don't": 3,
    "how": 2,
    "why": 2
}

with open("transcript.json", "r", encoding="utf-8") as f:
    segments = json.load(f)

video_end = segments[-1]["end"]

windows = []

current_start = 0

while current_start < video_end:

    current_end = current_start + WINDOW_SIZE

    score = 0
    text = ""

    for segment in segments:

        if segment["start"] < current_end and segment["end"] > current_start:

            segment_text = segment["text"].lower()

            text += " " + segment["text"]

            for word, points in keywords.items():

                if word in segment_text:
                    score += points

    windows.append({
        "start": current_start,
        "end": current_end,
        "score": score,
        "text": text
    })

    current_start += STEP

windows.sort(
    key=lambda x: x["score"],
    reverse=True
)

selected = []

for candidate in windows:

    overlap = False

    for chosen in selected:

        if not (
            candidate["end"] < chosen["start"]
            or
            candidate["start"] > chosen["end"]
        ):
            overlap = True
            break

    if not overlap:

        selected.append(candidate)

    if len(selected) == 5:
        break

print("\nBEST NON-OVERLAPPING CLIPS\n")

for i, clip in enumerate(selected, start=1):

    print(
        f"CLIP {i}"
    )

    print(
        f"Score={clip['score']}"
    )

    print(
        f"{clip['start']:.1f} -> {clip['end']:.1f}"
    )

    print(
        clip["text"][:250]
    )

    print("=" * 60)