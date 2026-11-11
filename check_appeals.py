import json
import urllib.request

BASE = "http://127.0.0.1:5000"
TEXT = ("Effective communication is an important skill in the workplace today. "
        "It helps teams share ideas and solve problems together. "
        "Strong communication also improves productivity and builds trust.")


def post(path, body):
    req = urllib.request.Request(
        BASE + path, data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req) as r:
        return json.load(r)


for trial in (1, 2, 3):
    passed = 0
    for i in range(1, 6):
        sub = post("/submit", {"text": TEXT, "creator_id": f"appeal_t{trial}_{i}"})
        cid = sub["content_id"]
        app = post("/appeal", {"content_id": cid, "reasoning": "I wrote this myself."})
        log = json.load(urllib.request.urlopen(BASE + "/log?limit=500"))["entries"]
        logged = any(e.get("content_id") == cid and e.get("event") == "appeal"
                     and e.get("status") == "under_review" for e in log)
        if app.get("status") == "under_review" and logged:
            passed += 1
    print(f"trial {trial}: {passed} of 5 appeals returned under_review and appear in the log")