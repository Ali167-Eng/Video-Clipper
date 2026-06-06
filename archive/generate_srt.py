import json

def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)

    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"

with open("transcript.json", "r", encoding="utf-8") as f:
    segments = json.load(f)

with open("captions.srt", "w", encoding="utf-8") as srt:

    for i, segment in enumerate(segments, start=1):

        start = format_time(segment["start"])
        end = format_time(segment["end"])
        text = segment["text"].strip()

        srt.write(f"{i}\n")
        srt.write(f"{start} --> {end}\n")
        srt.write(f"{text}\n\n")

print("captions.srt created successfully!")