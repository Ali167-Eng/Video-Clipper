import json

with open("transcript.json", "r", encoding="utf-8") as f:
    segments = json.load(f)

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

print(f"Original segments: {len(segments)}")
print(f"Merged segments: {len(merged)}")

print("\nFIRST 5 MERGED SEGMENTS:\n")

for clip in merged[:5]:

    print(
        f"{clip['start']:.2f} -> {clip['end']:.2f}"
    )

    print(clip["text"][:200])

    print("-" * 50)