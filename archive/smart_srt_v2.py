import os
import re

INPUT_FOLDER = "srt"
OUTPUT_FOLDER = "smart_srt_v2"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

MAX_LINE_LENGTH = 38

BREAK_WORDS = [
    "because",
    "but",
    "and",
    "so",
    "then",
    "if",
    "when",
    "while",
    "however"
]

def split_text(text):

    text = text.strip()

    # لو قصيرة نخليها سطر واحد
    if len(text) <= MAX_LINE_LENGTH:
        return text

    words = text.split()

    best_split = None
    center = len(words) // 2

    # ندور على كلمة مناسبة حوالين النص
    for i in range(max(1, center - 4), min(len(words)-1, center + 4)):

        if words[i].lower() in BREAK_WORDS:
            best_split = i
            break

    # لو ملقيناش كلمة مناسبة نقسم من النص
    if best_split is None:
        current_len = 0

        for i, word in enumerate(words):

            current_len += len(word) + 1

            if current_len >= len(text) / 2:
                best_split = i
                break

    line1 = " ".join(words[:best_split+1]).strip()
    line2 = " ".join(words[best_split+1:]).strip()

    # لو السطر التاني فاضي
    if not line2:
        return line1

    return line1 + "\n" + line2

for filename in os.listdir(INPUT_FOLDER):

    if not filename.endswith(".srt"):
        continue

    input_file = os.path.join(INPUT_FOLDER, filename)
    output_file = os.path.join(OUTPUT_FOLDER, filename)

    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    result = []

    i = 0

    while i < len(lines):

        line = lines[i].rstrip()

        result.append(line)

        if "-->" in line:

            i += 1

            if i < len(lines):

                subtitle_text = lines[i].strip()

                result.append(
                    split_text(subtitle_text)
                )

        i += 1

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(result))

    print(f"Created {output_file}")

print("\nDone!")