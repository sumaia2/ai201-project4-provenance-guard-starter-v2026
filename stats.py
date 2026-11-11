import re

text = open("results/run_2026-11-10_2347_before.md", encoding="utf-8").read()

for section in text.split("### ")[1:]:
    name = section.splitlines()[0]
    trial1 = section.split("**Trial 2**")[0]
    scores = [float(x) for x in re.findall(r'"confidence": ([0-9.]+)', trial1)]
    statuses = re.findall(r'"status": (\w+)', trial1)
    avg = round(sum(scores) / len(scores), 4) if scores else None
    print(name)
    print("  statuses:", statuses)
    print("  scores:  ", scores)
    print("  average: ", avg)
    if name.startswith("my own"):
        first5 = scores[:5]
        print("  average of first 5:", round(sum(first5) / len(first5), 4))