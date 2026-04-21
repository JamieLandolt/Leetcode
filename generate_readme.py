import os

PROBLEM_DIR = "problems"
README = "README.md"

files = sorted(os.listdir(PROBLEM_DIR))

lines = [
    "# LeetCode Solutions\n\n",
    "| Problem | File |\n",
    "|--------|------|\n"
]

for f in files:
    name = f.replace("-", " ").split(".")[0].title()
    lines.append(f"| {name} | [{f}]({PROBLEM_DIR}/{f}) |\n")

with open(README, "w") as f:
    f.writelines(lines)