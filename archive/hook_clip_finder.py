import json

WINDOW_SIZE = 45
STEP = 15

keywords = {
    "rich": 5,
    "money": 4,
    "million": 5,
    "success": 5,
    "secret": 4,
    "mistake": 4
}

hook_phrases = {
    "poor people": 20,
    "this is how": 15,
    "don't": 10,
    "never": 10,
    "mistake": 15,
    "secret": 15,
    "nobody": 15,
    "truth": 15,
    "rich": 5
}

curiosity_phrases = {
    "because": 5,
    "the reason": 10,
    "this is why": 10,
    "i'm going to show you": 20,
    "i will show you": 20,
    "here's how": 15,
    "the problem is": 10,
    "what happens": 15,
    "let's get into": 10,
    "the four paths": 15,
    "this is how you": 15
}

with open("transcript.json", "r", encoding="utf-8") as f:
    segments = json.load(f)

video_end = segments[-1]["end"]

windows = []

current_start = 0

while current_start < video_end:

    current_end = current_start + WINDOW_SIZE

    text = ""
    score = 0

    for segment in segments:

        if segment["start"] < current_end and segment["end"] > current_start:
            text += " " + segment["text"]

    text_lower = text.lower()

    # Keyword Score
    for word, points in keywords.items():
        if word in text_lower:
            score += points

    # Hook Score
    for phrase, points in hook_phrases.items():
        if phrase in text_lower:
            score += points

    # Curiosity Score
    for phrase, points in curiosity_phrases.items():
        if phrase in text_lower:
            score += points

    # Bonus لأول دقيقتين
    if current_start < 120:
        score += 5

    word_count = len(text.split())

    windows.append({
        "start": current_start,
        "end": current_end,
        "score": score,
        "word_count": word_count,
        "text": text
    })

    current_start += STEP

# ترتيب حسب السكور
windows.sort(
    key=lambda x: x["score"],
    reverse=True
)

# منع التداخل
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

print("\nBEST HOOK + CURIOSITY CLIPS\n")

for i, clip in enumerate(selected, start=1):

    if clip["score"] >= 60:
        suggested_duration = 60

    elif clip["score"] >= 40:
        suggested_duration = 45

    else:
        suggested_duration = 30

    print(f"\nCLIP {i}")
    print(f"Score = {clip['score']}")
    print(f"Suggested Duration = {suggested_duration} seconds")
    print(f"Word Count = {clip['word_count']}")
    print(f"Time = {clip['start']:.1f} -> {clip['end']:.1f}")

    print("\nPreview:")
    print(clip["text"][:300])

    print("\n" + "=" * 70)