"""Capstone: run my five criteria three times.
Usage: python run_capstone.py --label before
Needs the service running (python app.py)."""
import json
import sys
import time
import urllib.error
import urllib.request

BASE = "http://127.0.0.1:5000"
LABEL = sys.argv[sys.argv.index("--label") + 1] if "--label" in sys.argv else "before"
STAMP = str(int(time.time()))

VALID = ("I went to the store yesterday and forgot my wallet, which was "
         "embarrassing. The cashier was kind about it, and I came back later "
         "with my card. It was fine.")


def send(path, body, raw=False):
    data = body if raw else json.dumps(body).encode()
    req = urllib.request.Request(
        BASE + path, data=data, method="POST",
        headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return r.status, json.load(r)
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.load(e)
        except Exception:
            return e.code, {}


def log():
    with urllib.request.urlopen(BASE + "/log?limit=5000") as r:
        return json.load(r)["entries"]


def rejected_count():
    return sum(1 for e in log() if e.get("event") == "rejected")


def run_trial(n):
    cid = lambda name: f"cap_{LABEL}_{STAMP}_t{n}_{name}"
    out = {}

    # Criterion 1: four junk inputs must each get a 400
    junk = {
        "control_characters": "\x00\x01\x02 \x03\x04",
        "punctuation_only": "!!! ??? ... ,,, ;;;",
        "one_long_word": "a" * 200,
        "emoji_only": "\U0001F600" * 8,
    }
    codes = {k: send("/submit", {"text": v, "creator_id": cid("junk_" + k)})[0]
             for k, v in junk.items()}
    out["c1"] = {"passed": sum(c == 400 for c in codes.values()), "of": 4, "codes": codes}

    # Warm the model so criterion 3 measures warm requests
    send("/submit", {"text": VALID, "creator_id": cid("warmup")})

    # Criterion 2: 10 valid + 10 invalid requests, each logged with a duration
    ids = []
    for i in range(10):
        ids.append(cid(f"c2_valid_{i}"))
        send("/submit", {"text": VALID, "creator_id": ids[-1]})
    invalid_texts = ["", "   ", 12345, None, "hi", "!!!", "\x00\x01\x02 \x03",
                     "x" * 200, "\U0001F600" * 5, "word " * 5000]
    for i, t in enumerate(invalid_texts):
        ids.append(cid(f"c2_bad_{i}"))
        send("/submit", {"text": t, "creator_id": ids[-1]})
    entries = log()
    logged = 0
    for c in ids:
        ok = any(e.get("event") == "request" and e.get("creator_id") == c
                 and isinstance(e.get("status_code"), int)
                 and isinstance(e.get("duration_ms"), (int, float)) for e in entries)
        logged += ok
    out["c2"] = {"passed": logged, "of": 20}

    # Criterion 3: warm valid requests under 3000 ms, from the log
    fast_ids = [cid(f"c3_{i}") for i in range(10)]
    for c in fast_ids:
        send("/submit", {"text": VALID, "creator_id": c})
    entries = log()
    durations = []
    for c in fast_ids:
        for e in entries:
            if e.get("event") == "request" and e.get("creator_id") == c:
                durations.append(e.get("duration_ms"))
    out["c3"] = {"passed": sum(1 for d in durations if d is not None and d < 3000),
                 "of": 10, "durations_ms": durations}

    # Criterion 4: five bad requests -> 400 and a "rejected" log entry each
    bad = [
        ("no_text", {"creator_id": cid("c4_a")}, False),
        ("25000_chars", {"text": "word " * 5000, "creator_id": cid("c4_b")}, False),
        ("text_is_number", {"text": 12345, "creator_id": cid("c4_c")}, False),
        ("body_is_array", json.dumps([1, 2, 3]).encode(), True),
        ("no_creator_id", {"text": VALID}, False),
    ]
    good = 0
    detail = {}
    for name, body, raw in bad:
        before = rejected_count()
        code, _ = send("/submit", body, raw=raw)
        after = rejected_count()
        ok = code == 400 and after > before
        detail[name] = {"status": code, "new_rejected_entries": after - before}
        good += ok
    out["c4"] = {"passed": good, "of": 5, "detail": detail}

    # Criterion 5: (a) 11th submission in a minute is a 429, (b) 5 appeals work
    rl = cid("c5_rate")
    statuses = [send("/submit", {"text": VALID, "creator_id": rl})[0] for _ in range(11)]
    a_ok = statuses[:10] == [200] * 10 and statuses[10] == 429
    appeals = 0
    appeal_ids = []
    for i in range(5):
        code, body = send("/submit", {"text": VALID, "creator_id": cid(f"c5_ap_{i}")})
        content_id = body.get("content_id")
        if content_id:
            _, ap = send("/appeal", {"content_id": content_id, "reasoning": "I wrote this."})
            appeal_ids.append((content_id, ap.get("status")))
    entries = log()
    for content_id, status in appeal_ids:
        appeals += (status == "under_review" and any(
            e.get("content_id") == content_id and e.get("event") == "appeal"
            and e.get("status") == "under_review" for e in entries))
    out["c5"] = {"rate_limit_ok": a_ok, "statuses": statuses,
                 "appeals_ok": appeals, "of": 5,
                 "passed": int(a_ok and appeals == 5)}
    return out


results = []
for n in (1, 2, 3):
    print(f"--- trial {n} ---")
    r = run_trial(n)
    results.append(r)
    print("c1 junk -> 400:      ", r["c1"]["passed"], "of 4")
    print("c2 logged w/ time:   ", r["c2"]["passed"], "of 20")
    print("c3 warm under 3s:    ", r["c3"]["passed"], "of 10")
    print("c4 bad -> 400+log:   ", r["c4"]["passed"], "of 5")
    print("c5 429 + appeals:    ", "429 ok" if r["c5"]["rate_limit_ok"] else "429 MISSED",
          "|", r["c5"]["appeals_ok"], "of 5 appeals")
    if n < 3:
        time.sleep(65)

path = f"results/capstone_{LABEL}_{STAMP}.md"
with open(path, "w", encoding="utf-8") as f:
    f.write(f"# Capstone run: {LABEL}\n\nProduced by `run_capstone.py`, calling `app.py::submit` "
            f"and `app.py::appeal`.\n\n```json\n{json.dumps(results, indent=2)}\n```\n")
print("Wrote", path)