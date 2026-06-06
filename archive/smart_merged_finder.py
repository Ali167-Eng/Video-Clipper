import json

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

# دمج Segments
merged = []

current = {
    "start": segments[0]["start"],
    "end": segments[0]["end"],
    "text": segments[0]["text"]
}

for segment in segments[1:]:

    gap = segment["start"] - current["end"]

    if gap <= 2:

        current["end"] = segment["end"]
        current["text"] += " " + segment["text"]

    else:

        merged.append(current)

        current = {
            "start": segment["start"],
            "end": segment["end"],
            "text": segment["text"]
        }

merged.append(current)

# حساب Score

results = []

for clip in merged:

    text = clip["text"].lower()

    score = 0

    for word, points in keywords.items():

        if word in text:
            score += points

    duration = clip["end"] - clip["start"]

    # أفضل مدة للكليبات
    if 20 <= duration <= 90:
        score += 5

    if score > 0:

        results.append({
            "score": score,
            "start": clip["start"],
            "end": clip["end"],
            "duration": duration,
            "text": clip["text"]
        })

results.sort(
    key=lambda x: x["score"],
    reverse=True
)

print("\nTOP 10 CLIPS\n")

for clip in results[:10]:

    print(
        f"Score={clip['score']} | "
        f"{clip['duration']:.1f}s | "
        f"{clip['start']:.1f} -> {clip['end']:.1f}"
    )

    print(clip["text"][:250])

    print("=" * 60)