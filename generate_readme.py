import os
import re
import urllib.parse

PROBLEM_DIR = "problems"
README = "README.md"

def extract_number(filename):
    match = re.match(r"(\d+)", filename)
    return int(match.group(1)) if match else float("inf")

files = os.listdir(PROBLEM_DIR)

# Sort by numeric problem ID
files.sort(key=extract_number)

lines = [
    "# LeetCode Solutions\n\n",
    "| # | Problem | Link |\n",
    "|---|--------|------|\n"
]

for f in files:
    name = f.rsplit(".", 1)[0]

    # Extract problem number
    num_match = re.match(r"(\d+)", f)
    number = num_match.group(1) if num_match else "?"

    # Clean display name
    title = name.split(".", 1)[-1].strip()

    # URL encode filename (fixes spaces issue)
    encoded_path = urllib.parse.quote(f)

    lines.append(
        f"| {number} | {title} | [{f}]({PROBLEM_DIR}/{encoded_path}) |\n"
    )

with open(README, "w", encoding="utf-8") as f:
    f.writelines(lines)