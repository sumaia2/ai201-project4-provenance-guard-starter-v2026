# Running Provenance Guard (Path B: local with logs)

**Needs:** Python 3.13, about 5 GB of free disk space (PyTorch plus the GPT-2 model, about 550 MB), 8 GB of RAM recommended.

## Setup (Windows PowerShell)

```
git clone https://github.com/sumaia2/ai201-project4-provenance-guard-starter-v2026.git
cd ai201-project4-provenance-guard-starter-v2026
py -3.13 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python detector.py
```

`python detector.py` downloads GPT-2 (about 550 MB) once. The pinned dependencies are in requirements.txt (flask, flask-limiter, requests, transformers, torch, gunicorn, certifi).

## Start

```
python app.py
```

Wait for `Provenance Guard on http://127.0.0.1:5000`. The first request takes about 40 seconds while the model loads. Later ones take a second or two.

## Try it (second terminal, with the environment activated)

```
curl.exe -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d '{\"text\": \"I went to the store yesterday and forgot my wallet, which was embarrassing. The cashier was kind about it.\", \"creator_id\": \"demo\"}'
curl.exe "http://127.0.0.1:5000/log?limit=5"
```

Appeal a decision with the `content_id` it returned:

```
curl.exe -X POST http://127.0.0.1:5000/appeal -H "Content-Type: application/json" -d '{\"content_id\": \"PASTE-ID\", \"reasoning\": \"I wrote this myself.\"}'
```

## What to expect

- `POST /submit` returns a guess (ai, human or unsure), a confidence from 0 to 1, a label, and both signal scores.
- Text with fewer than 3 words, control characters, or over 20000 characters gets a 400.
- More than 10 submissions a minute from one creator_id gets a 429.
- Every request is written to `logs/audit.jsonl` with its duration. `GET /log` reads it back.

macOS or Linux: use `python3 -m venv .venv`, `source .venv/bin/activate` and plain `curl`.