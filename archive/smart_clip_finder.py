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

results = []

for segment in segments:

    text = segment["text"].lower()

    score = 0

    for word, points in keywords.items():

        if word in text:
            score += points

    if score > 0:

        results.append({
            "start": segment["start"],
            "end": segment["end"],
            "score": score,
            "text": segment["text"]
        })

results = sorted(
    results,
    key=lambda x: x["score"],
    reverse=True
)

print("\nTOP CLIPS:\n")

for clip in results[:10]:

    print(
        f"Score: {clip['score']} | "
        f"{clip['start']:.2f} -> {clip['end']:.2f}"
    )

    print(clip["text"])
    print("-" * 50)