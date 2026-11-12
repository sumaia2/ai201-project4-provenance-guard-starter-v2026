import json

lines = [json.loads(l) for l in open("logs/audit.jsonl", encoding="utf-8") if l.strip()]
req = [e for e in lines if e.get("event") == "request"
       and str(e.get("creator_id", "")).startswith("cap_before_")]
ok = [e for e in req if e.get("status_code") == 200][:5]
bad = [e for e in req if e.get("status_code") == 400][:5]
block = "```\n" + "\n".join(json.dumps(e, ensure_ascii=False) for e in ok + bad) + "\n```\n"
text = open("README.md", encoding="utf-8").read()
marker = 'Ten request entries from logs/audit.jsonl (capstone "before" run; five accepted, five rejected with a 400):'
assert marker in text, "marker line not found in README.md"
text = text.replace(marker, marker + "\n\n" + block, 1)
open("README.md", "w", encoding="utf-8").write(text)
print(len(ok + bad), "entries added")