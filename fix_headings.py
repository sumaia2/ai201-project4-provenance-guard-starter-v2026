t = open("README.md", encoding="utf-8").read()
pairs = [
    ("\n## Run Log and Verdicts\n", "\n## Run Log and Verdicts (Unit 8)\n"),
    ("\n## The Improvement\n", "\n## The Improvement (Unit 8)\n"),
    ("\n## What's Still Broken\n", "\n## What's Still Broken (Unit 8)\n"),
    ("\n## How I Used AI\n", "\n## How I Used AI (Units 7 and 8)\n"),
]
for old, new in pairs:
    assert old in t, old
    t = t.replace(old, new, 1)  # only the first (older) copy
open("README.md", "w", encoding="utf-8").write(t)
print("renamed", len(pairs))