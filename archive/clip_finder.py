import whisper

keywords = [
    "rich",
    "money",
    "success",
    "million",
    "secret",
    "mistake"
]

model = whisper.load_model("base")

result = model.transcribe("video.mp4")

print("\nPossible Clips:\n")

for segment in result["segments"]:

    text = segment["text"].lower()

    for word in keywords:

        if word in text:

            print(
                f"{segment['start']:.2f} -> "
                f"{segment['end']:.2f} | "
                f"{segment['text']}"
            )

            break