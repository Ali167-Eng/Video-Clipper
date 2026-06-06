import json
import subprocess
import os

keywords = {
    "rich": 5,
    "money": 4,
    "million": 5,
    "success": 5,
    "secret": 4,
    "mistake": 4
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

        start = max(0, segment["start"] - 15)
        end = segment["end"] + 30

        results.append({
            "score": score,
            "start": start,
            "end": end,
            "text": segment["text"]
        })

results.sort(
    key=lambda x: x["score"],
    reverse=True
)

top_clips = results[:5]

os.makedirs("clips", exist_ok=True)

for i, clip in enumerate(top_clips, start=1):

    duration = clip["end"] - clip["start"]

    output_file = f"clips/clip_{i}.mp4"

    command = [
        "ffmpeg",
        "-y",
        "-i",
        "video.mp4",
        "-ss",
        str(clip["start"]),
        "-t",
        str(duration),
        "-c",
        "copy",
        output_file
    ]

    subprocess.run(command)

    print(f"Created: {output_file}")