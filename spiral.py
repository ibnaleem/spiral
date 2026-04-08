import sys, os
from collections import deque

def spiral(word: str) -> str:
    q = deque()

    right = True

    q.append(word[0])

    for i, c in enumerate(word):
        if i == 0:
            continue
        if right == True:
            q.append(c)
            right = False
        else:
            q.appendleft(c)
            right = True

    return "".join(q)

filepath = sys.argv[1]

if not os.path.exists(filepath):
    print(f"🫤 {filepath} does not exist...")
    sys.exit(1)

elif os.path.isdir(filepath):
    print(f"🤔 {filepath} is a directory...")
    sys.exit(1)
else:

    print("🌪️ spiral.py - a weird word obfuscation algorithm")

    print()

    print(f"👀 Reading {filepath}...")
    with open(filepath, "r") as f:
        lines = f.readlines()

    print(f"✅ Read {filepath} with {len(lines):,} lines!")

    print(f"✍️ Writing {filepath}-spiral.txt...")

    name = os.path.splitext(filepath)[0]

    with open(f"{name}-spiral.txt", "w") as f:
        for i in lines:
            modified = spiral(i)
            f.write(modified)

    print(f"🎉 Written {name}-spiral.txt!")

    print()

    print("👋 Goodbye")
