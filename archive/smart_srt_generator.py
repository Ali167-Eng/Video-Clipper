import os

INPUT_FOLDER = "srt"
OUTPUT_FOLDER = "smart_srt"

MAX_WORDS_PER_LINE = 5

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

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

                text = lines[i].strip()

                words = text.split()

                chunks = []

                for j in range(
                    0,
                    len(words),
                    MAX_WORDS_PER_LINE
                ):
                    chunk = " ".join(
                        words[j:j+MAX_WORDS_PER_LINE]
                    )

                    chunks.append(chunk)

                result.append("\n".join(chunks))
            else:
                result.append("")

        i += 1

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as f:

        f.write("\n".join(result))

    print(f"Created {output_file}")

print("\nDone!")