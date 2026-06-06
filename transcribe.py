
import whisper
import json
import sys
import os

# إنشاء الفولدرات لو مش موجودة
os.makedirs("workspace/temp", exist_ok=True)

if len(sys.argv) < 2:
    print("Usage: python transcribe.py video_path")
    exit()

video_path = sys.argv[1]

print("Loading model...")

model = whisper.load_model("base")

print("Transcribing...")

result = model.transcribe(video_path)

# حفظ النص الكامل
with open(
    "workspace/temp/transcript.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(result["text"])

# حفظ الـ Segments
with open(
    "workspace/temp/transcript.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        result["segments"],
        f,
        ensure_ascii=False,
        indent=4
    )

print("Transcript saved!")

