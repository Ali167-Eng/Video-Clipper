import json

with open("transcript.json", "r", encoding="utf-8") as f:
    segments = json.load(f)

keywords = {
    "rich": 5,
    "money": 4,
    "million": 5,
    "success": 5,
    "secret": 4,
    "mistake": 4
}

results = []

for segment in segments:

    text = segment["text"].lower()

    score = 0

    for word, points in keywords.items():

        if word in text:
            score += points

    if score > 0:

        start = max(0, segment["start"] - 15)
        end = segment["end"] + 30

        results.append({
            "score": score,
            "start": start,
            "end": end,
            "text": segment["text"]
        })

results.sort(key=lambda x: x["score"], reverse=True)

for i, clip in enumerate(results[:5], start=1):

    print(
        f"CLIP {i}"
    )

    print(
        f"START: {clip['start']:.2f}"
    )

    print(
        f"END: {clip['end']:.2f}"
    )

    print(
        f"SCORE: {clip['score']}"
    )

    print(
        clip["text"]
    )

    print("=" * 50)