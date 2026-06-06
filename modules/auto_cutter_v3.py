
import json
import re
import os

WINDOW_SIZE = 45
STEP = 15

# التأكد من وجود الفولدر
os.makedirs("workspace/temp", exist_ok=True)

hook_phrases = {
    "how": 8,
    "why": 8,
    "secret": 12,
    "mistake": 12,
    "truth": 12,
    "never": 10,
    "don't": 10,
    "nobody": 12,
    "this is how": 15,
    "here's how": 15,
    "what happens": 15
}

curiosity_phrases = {
    "because": 5,
    "the reason": 10,
    "this is why": 10,
    "problem": 8,
    "however": 8,
    "but": 5,
    "instead": 5,
    "imagine": 10
}

emotion_phrases = {
    "crazy": 10,
    "amazing": 10,
    "shocking": 12,
    "dangerous": 12,
    "powerful": 8,
    "incredible": 10,
    "unbelievable": 12
}

with open(
    "workspace/temp/transcript.json",
    "r",
    encoding="utf-8"
) as f:
    segments = json.load(f)

video_end = segments[-1]["end"]

windows = []

current_start = 0

while current_start < video_end:

    current_end = current_start + WINDOW_SIZE

    text = ""

    for segment in segments:

        if (
            segment["start"] < current_end
            and
            segment["end"] > current_start
        ):
            text += " " + segment["text"]

    text_lower = text.lower()

    hook_score = 0
    curiosity_score = 0
    emotion_score = 0
    number_score = 0

    for phrase, points in hook_phrases.items():
        if phrase in text_lower:
            hook_score += points

    for phrase, points in curiosity_phrases.items():
        if phrase in text_lower:
            curiosity_score += points

    for phrase, points in emotion_phrases.items():
        if phrase in text_lower:
            emotion_score += points

    numbers = re.findall(r"\d+", text)
    number_score += len(numbers) * 2

    final_score = (
        hook_score * 3 +
        curiosity_score * 2 +
        emotion_score * 2 +
        number_score
    )

    if current_start < 120:
        final_score += 5

    windows.append({
        "start": current_start,
        "end": current_end,
        "score": final_score,
        "word_count": len(text.split()),
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

clips_data = []

for i, clip in enumerate(selected, start=1):

    wc = clip["word_count"]

    if wc > 220:
        duration = 75
    elif wc > 160:
        duration = 60
    elif wc > 100:
        duration = 45
    else:
        duration = 30

    center = (
        clip["start"] +
        clip["end"]
    ) / 2

    start_time = max(
        0,
        center - duration / 2
    )

    clips_data.append({
        "id": i,
        "start": round(start_time, 2),
        "duration": duration,
        "score": clip["score"],
        "word_count": wc
    })

with open(
    "workspace/temp/clips.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        clips_data,
        f,
        indent=4
    )

print("clips.json created successfully!\n")

for clip in clips_data:

    print(
        f"Clip {clip['id']} | "
        f"Start={clip['start']}s | "
        f"Duration={clip['duration']}s | "
        f"Score={clip['score']}"
    )

