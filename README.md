# Provenance Guard

## What This Does

Provenance Guard is a small backend service a writing site could plug into. A site sends a piece of writing, and the service guesses whether a person or an AI tool wrote it, and sends back a confidence score and a plain-English label a reader would see.

The path a submission takes:

1. The site sends `POST /submit` with `text` and `creator_id`.
2. The service checks the input. Missing, empty, too short or too long text, or a missing `creator_id`, gets a 400 error and is logged as a rejection.
3. Signal one (detector.py, a GPT-2 model running locally) scores how predictable the text is.
4. Signal two (stylometry.py) scores the shape of the text: sentence length variety and punctuation.
5. scoring.py::combine_signals turns the two scores into one confidence score.
6. scoring.py::score_to_label turns that score into one of three labels.
7. The service writes everything to logs/audit.jsonl and returns the JSON.

If a writer disagrees, they send `POST /appeal` with the `content_id` and their reasoning. The service records the appeal next to the original decision and moves the item to `under_review`.

## Signals and Scoring

**Signal one: the model signal (detector.py::model_signal).** It measures how predictable the text is to GPT-2 (perplexity), turned into a 0 to 1 score where higher means more likely AI. AI text tends to be predictable, so it scores high. **What it can't see:** authorship. It rewards plain words in short, ordinary sentences, so a real writer who writes plainly can score as AI. My own paragraph about forgetting my wallet scored 0.7535, while my email with specific names and my game blurb scored much lower (the blurb scored 0.0692).

**Signal two: the style signal (stylometry.py::style_signal).** It measures the text as text, with no understanding of meaning: how much sentence length varies, and how much punctuation (other than full stops) the text uses, each turned into a 0 to 1 score and averaged. Higher means more likely AI. I dropped type-token ratio from the score, because on short texts it scored my plain writing as more varied than an AI paragraph (0.46 against 0.41), the wrong way round. **What it can't see:** meaning. Anything that changes the shape without changing the substance moves it, for example typos, breaking up sentences or adding a quotation. Punctuation density barely changed across my test texts (0.025 to 0.064), so it adds little. Texts shorter than three sentences return 0.5.

**Combining rule (scoring.py::combine_signals).** The combined score is 0.5 x model_score + 0.5 x style_score. If either signal is below 0.5, the combined score is capped at 0.74 (the AI threshold minus 0.01), so a high-confidence AI result needs both signals to lean AI. I chose this because a wrong accusation costs a real writer more than a missed AI piece. The weights are in config.py (WEIGHT_MODEL_SIGNAL and WEIGHT_STYLE_SIGNAL, both 0.5).

**Thresholds (config.py).** HUMAN_THRESHOLD is 0.35 and AI_THRESHOLD is 0.75. I first set the AI threshold at 0.65, and a paragraph I wrote myself (about forgetting my wallet) scored 0.6519 and was labeled "ai", a false positive. I raised it to 0.75, and the same paragraph is now "unsure". The cost is that more AI text lands in "unsure".

## Label Variants

| Label | Score range | Exact text shown to a reader |
|---|---|---|
| High-confidence human | 0.00 to 0.35 | "We think this was probably written by a person." |
| Unsure | 0.35 to 0.75 | "We can't tell for sure whether this was written by a person or an AI tool, so we haven't labeled it either way. If you wrote it yourself, nothing is wrong and you don't need to do anything." |
| High-confidence AI | 0.75 to 1.00 | "We think this was probably written by an AI tool. This is a guess, not proof. If you wrote it yourself, you can appeal and your reasoning will be recorded for review." |

All three are reachable. Real outputs: my game blurb scored 0.1258 (human), my wallet paragraph scored 0.6519 (unsure), and a paragraph of evenly sized sentences about communication scored 0.8017 (ai).

## Sample Run

**Submission** (`POST /submit`):

```
curl.exe -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d '{"text": "Effective communication is an important skill in the workplace today. It helps teams share ideas and solve problems together. Strong communication also improves productivity and builds trust. Organizations that value communication achieve better results over time.", "creator_id": "me"}'
```

Response:

```
{
  "confidence": 0.8017,
  "content_id": "37bf558e-e5b3-440b-b22e-7541fd000c6a",
  "guess": "ai",
  "label": "We think this was probably written by an AI tool. This is a guess, not proof. If you wrote it yourself, you can appeal and your reasoning will be recorded for review.",
  "model_score": 0.6602,
  "style_score": 0.9433
}
```

**Appeal** (`POST /appeal`):

```
curl.exe -X POST http://127.0.0.1:5000/appeal -H "Content-Type: application/json" -d '{"content_id": "37bf558e-e5b3-440b-b22e-7541fd000c6a", "reasoning": "I wrote this myself for a class assignment."}'
```

Response:

```
{
  "content_id": "37bf558e-e5b3-440b-b22e-7541fd000c6a",
  "message": "Thank you. Your appeal has been recorded and this piece is now under review.",
  "status": "under_review"
}
```

**Resulting log entries** (`GET /log?limit=2`, from logs/audit.jsonl):

```
{"timestamp": "2026-10-28T04:05:55+00:00", "content_id": "37bf558e-e5b3-440b-b22e-7541fd000c6a", "creator_id": "me", "guess": "ai", "model_score": 0.6602, "style_score": 0.9433, "combined_score": 0.8017, "label": "We think this was probably written by an AI tool. ...", "status": "decided"}
{"timestamp": "2026-10-28T04:09:12+00:00", "content_id": "37bf558e-e5b3-440b-b22e-7541fd000c6a", "creator_id": "me", "event": "appeal", "reasoning": "I wrote this myself for a class assignment.", "status": "under_review"}
```

**Bad input** (`POST /submit` with empty text):

```
{"error": "bad_request", "message": "text is required and must be a non-empty string."}
```

## How I Used AI (Units 7 and 8)

**Moment 1:** I asked Claude to help me turn my route stubs into a working `POST /submit`. It gave me code that checked the input, called the model signal and wrote to the log. It ran, but my first test gave an IndentationError and then an UnboundLocalError because the imports were in the wrong place. I fixed the indentation by hand and moved the imports to the top of the function, then checked the route with curl.

**Moment 2:** I asked Claude for a second signal and a combining rule. Its first version used three style measures, and when I tested it, my own paragraph scored as more AI-like than an AI paragraph because of the type-token ratio. I dropped that measure. A paragraph I wrote about forgetting my wallet was also labeled "ai" at an AI threshold of 0.65, so I raised the threshold to 0.75. I chose the five criteria numbers myself, and Claude formatted them. Claude drafted the three label texts, and I checked them by submitting text that produced each label.
In Unit 8, Claude drafted my scenarios, diagnoses and README sections from my real outputs, and I ran every command.



---

## Rate Limiting

I limit POST /submit to **10 per minute and 100 per day** per caller (config.py: RATE_LIMIT_PER_MINUTE and RATE_LIMIT_PER_DAY, switched on with RATE_LIMITING_ENABLED). A real writer submitting their own work sends a few pieces an hour, so 10 a minute never gets in their way, while a script sending hundreds of variations to map my thresholds hits the limit after the first ten. 100 a day stops a slower script, and is still well above what a writer needs. A caller counts as their creator_id when one is given, otherwise their address.

Flood test (`python run_attacks.py --flood 15`):

```
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429
```

## Attack Run — Before

Run: `python run_attacks.py --set attack_set\attack_set`, 56 attacks, results in results/attack_run_2026-11-10_2321.md. **45 held, 11 broke.**

| Family | Attacks | Held | Broke |
|---|---|---|---|
| evasion | 10 | 9 | 1 (EV05) |
| false_positive | 8 | 3 | 5 (FP02 to FP06) |
| prompt_injection | 6 | 5 | 1 (PI02) |
| malformed (MF) | 8 | 4 | 4 (MF03 to MF06) |
| malformed requests (RQ) | 12 | 12 | 0 |
| flood_same_creator | 12 | 12 | 0 |

| ID | Result | Mark |
|---|---|---|
| EV01 to EV04, EV06 to EV09 | unsure (0.373 to 0.693) | HELD |
| EV05 (heavy human editing) | human 0.348 | BROKE |
| EV10 | ai 0.867 | HELD |
| FP01, FP07, FP08 | unsure (0.526 to 0.656) | HELD |
| FP02 | ai 0.772 | BROKE |
| FP03 | ai 0.800 | BROKE |
| FP04 | ai 0.777 | BROKE |
| FP05 | ai 0.766 | BROKE |
| FP06 | ai 0.752 | BROKE |
| PI01, PI03 to PI06 | unsure (0.495 to 0.610) | HELD |
| PI02 | human 0.325 | BROKE |
| MF01, MF02, MF08 | 400 | HELD |
| MF03 (control characters) | 200, human 0.250 | BROKE |
| MF04 (only punctuation) | 200, unsure 0.506 | BROKE |
| MF05 (one very long word) | 200, unsure 0.740 | BROKE |
| MF06 (emoji only) | 200, unsure 0.740 | BROKE |
| MF07 (right-to-left script) | 200, unsure 0.703 | HELD |
| RQ01 to RQ12 | 400 | HELD |
| FL01_01 to FL01_10 | 200 | HELD |
| FL01_11, FL01_12 | 429 | HELD |

**Worst outcome:** FP03, a careful non-native English speaker, was labeled "ai" with a score of 0.8000. That is the writer with the least room to argue back, and the one I would least want to explain to a person whose own work was accused.

**Audit log entries** (from logs/audit.jsonl, one rejection included):

```
{"creator_id": "me", "event": "rejected", "reason": "missing_or_empty_text", "status": "rejected", "timestamp": "2026-10-28T03:16:09+00:00"}
{"creator_id": "flood_tester", "event": "rejected", "limit": "10 per 1 minute", "reason": "rate_limited", "status": "rejected", "timestamp": "2026-11-11T04:17:37+00:00"}
{"creator_id": "flood_tester", "event": "rejected", "limit": "10 per 1 minute", "reason": "rate_limited", "status": "rejected", "timestamp": "2026-11-11T04:17:37+00:00"}
{"creator_id": "flood_tester", "event": "rejected", "limit": "10 per 1 minute", "reason": "rate_limited", "status": "rejected", "timestamp": "2026-11-11T04:17:37+00:00"}
{"creator_id": "flood_tester", "event": "rejected", "limit": "10 per 1 minute", "reason": "rate_limited", "status": "rejected", "timestamp": "2026-11-11T04:17:37+00:00"}
{"creator_id": "flood_tester", "event": "rejected", "limit": "10 per 1 minute", "reason": "rate_limited", "status": "rejected", "timestamp": "2026-11-11T04:17:37+00:00"}
{"combined_score": 0.3479, "content_id": "15b9badf-6b36-4bef-b984-6c6551067d68", "creator_id": "attacker_EV05", "guess": "human", "label": "We think this was probably written by a person.", "model_score": 0.3212, "status": "decided", "style_score": 0.3747, "timestamp": "2026-11-11T04:21:41+00:00"}
{"combined_score": 0.8665, "content_id": "b9b5a50f-cbcb-4261-aa14-bbbe22d0db1e", "creator_id": "attacker_EV10", "guess": "ai", "label": "We think this was probably written by an AI tool. This is a guess, not proof. If you wrote it yourself, you can appeal and your reasoning will be recorded for review.", "model_score": 0.9792, "status": "decided", "style_score": 0.7538, "timestamp": "2026-11-11T04:21:43+00:00"}
{"combined_score": 0.7723, "content_id": "447d6321-56e5-448f-8c5f-2262ba0540fa", "creator_id": "attacker_FP02", "guess": "ai", "label": "We think this was probably written by an AI tool. This is a guess, not proof. If you wrote it yourself, you can appeal and your reasoning will be recorded for review.", "model_score": 0.7387, "status": "decided", "style_score": 0.8059, "timestamp": "2026-11-11T04:21:44+00:00"}
{"combined_score": 0.8, "content_id": "a5f04f10-2c04-4c36-b958-e92cef859128", "creator_id": "attacker_FP03", "guess": "ai", "label": "We think this was probably written by an AI tool. This is a guess, not proof. If you wrote it yourself, you can appeal and your reasoning will be recorded for review.", "model_score": 0.8051, "status": "decided", "style_score": 0.7949, "timestamp": "2026-11-11T04:21:44+00:00"}
```

## Run Log and Verdicts (Unit 8)

Run with `python run_eval.py --label before` (results/run_2026-11-10_2347_before.md) plus `check_appeals.py`, three trials each. Scenarios are in scenarios.py. Criterion 1 was tested with ten of my own Instagram captions, which are shorter than the 100 words the criterion names. Results were identical in all three trials because neither signal is random.

| # | Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|---|
| 1 | My own writing labeled "ai" | at most 1 of 10 | 0 of 10 | 0 of 10 | 0 of 10 | MET |
| 2 | AI average score minus my average | at least 0.30 | 0.3967 | 0.3967 | 0.3967 | MET |
| 3 | All three labels reachable | 3 of 3 | 3 of 3 | 3 of 3 | 3 of 3 | MET |
| 4 | Appeals reach under_review and the log | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 5 | Bad input gets a 400 | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |

All five were met, yet the attack set broke the system 11 times. Criterion 1 was set too low: it passed because my test texts were short, casual captions that both signals score as human. The attack set's false-positive inputs were formal, student and non-native writing, and 5 of 8 were accused. A tighter criterion 1 would test formal and non-native writing, with at most 1 of 10 labeled "ai". I did not revise any criterion.

**Diagnosis of the broken attacks (before):**

- **FP02 to FP06 (stage: combining rule and label mapping).** Both signals leaned AI at once (for example FP03: model 0.8051, style 0.7949, combined 0.8000). My "both must agree" rule only protects against one signal being wrong, so careful, predictable writing with even sentences passed it. All five combined scores (0.7524 to 0.8000) sat just above AI_THRESHOLD 0.75.
- **EV05 (stage: both signals).** Model 0.3212 and style 0.3747: heavily edited AI text reads as human to both, so there was nothing for the rule to disagree about.
- **PI02 (stage: signal one).** Model 0.2044, style 0.4445. No model reads the text as instructions here; the odd text scored as unpredictable, which signal one reads as human.
- **MF03 to MF06 (stage: the route).** The input check only rejects empty or whitespace text, so control characters, punctuation only, one very long word and emoji only were scored. MF03 got model 0.0 and "human".

## The Improvement (Unit 8)

**Change:** I raised AI_THRESHOLD in config.py from 0.75 to 0.82. Nothing else changed.

**Why:** the five false accusations all scored between 0.7524 and 0.8000, and EV10 (a real AI-style input) scored 0.8665, so 0.82 sits between them.

**Attack Run: After** (`python run_attacks.py --set attack_set\attack_set --label after`, results/attack_run_2026-11-10_2358_after.md): **50 held, 6 broke.**

| Family | Before: held / broke | After: held / broke |
|---|---|---|
| evasion (10) | 9 / 1 (EV05) | 9 / 1 (EV05) |
| false_positive (8) | 3 / 5 | **8 / 0** |
| prompt_injection (6) | 5 / 1 (PI02) | 5 / 1 (PI02) |
| malformed MF (8) | 4 / 4 (MF03 to MF06) | 4 / 4 (MF03 to MF06) |
| malformed requests RQ (12) | 12 / 0 | 12 / 0 |
| flood_same_creator (12) | 12 / 0 | 12 / 0 |

FP02 to FP06 changed from "ai" to "unsure", and EV10 stayed "ai".

**Run Log: After** (results/run_2026-11-10_2358_after.md):

| # | Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|---|
| 1 | My own writing labeled "ai" | at most 1 of 10 | 0 of 10 | 0 of 10 | 0 of 10 | MET |
| 2 | AI average score minus my average | at least 0.30 | 0.3967 | 0.3967 | 0.3967 | MET |
| 3 | All three labels reachable | 3 of 3 | 2 of 3 | 2 of 3 | 2 of 3 | MISSED |
| 4 | Appeals reach under_review and the log | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 5 | Bad input gets a 400 | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |

**Did it help?** Yes on the problem it targeted: real writers accused went from 5 to 0, and broken attacks fell from 11 to 6. It cost me criterion 3 and some AI detection: my "ai" test text scored 0.8017, which is below 0.82, so it now lands in "unsure", and in the criterion 2 set the number of AI texts labeled "ai" fell from 3 of 5 to 2 of 5. Criterion 3 is missed because of the label mapping (scoring.py::score_to_label with AI_THRESHOLD): the "ai" label is still reachable (EV10 got it at 0.8665), but my test text no longer reaches it. The scores did not change, so criterion 2 is unchanged.

## What's Still Broken (Unit 8)

- **EV05 (edited AI text passes as human).** I would add a third signal that does not depend on predictability or sentence shape. I stopped because the unit allows one change.
- **PI02.** Signal one reads odd text as human. I would not patch this one, because it is the same weakness as EV05.
- **MF03 to MF06 (junk is scored).** I would add input validation in app.py that requires a minimum number of real words and rejects control characters. I stopped at one change.
- **Criterion 3.** I would replace the "ai" test text with one that scores above 0.82, such as the EV10 input.

**The trade I would make in production:** fewer wrong accusations means more AI text gets through. I would keep the 0.82 threshold, because a wrong accusation costs a real writer far more than a missed AI piece. The writers who pay for this are the ones whose AI-like text now lands in "unsure" and goes unlabeled, which is a cost to the site, not to a person.


## What This Extends

This extends Provenance Guard, the service I built in Units 7 and 8. POST /submit scores a piece of writing with two signals, returns one of three labels, and POST /appeal records a writer's challenge. The new work in this unit is a hardening layer around /submit: stricter input validation, a duration and outcome record for every request, and a documented run path.

## The Shape

**Shape B: harden against failure.** The Unit 8 attack set showed that my service accepted junk it could not honestly score: control characters (MF03, scored "human" at 0.250), punctuation only (MF04), one very long word (MF05) and emoji only (MF06). This unit I added validation that rejects input without at least 3 real words, or with control characters, before either signal runs. I also log every request with its duration and outcome, failures included.

**Out of scope:** I am not adding or changing a signal, so edited AI text (EV05) stays unfixed. I am not changing the thresholds, since the AI threshold stays at 0.82 as it was after Unit 8. I am not changing the labels or the appeal path. I am not hosting it, because it loads GPT-2 locally and does not fit a free host's 512 MB.

## Running It

Path B: local with logs. The exact start command, the Python version, the dependencies and the model size are in RUNNING.md, which I tested from a fresh clone.


## Instrumentation

Every POST to /submit and /appeal writes one record to logs/audit.jsonl from a Flask hook (app.py::_log_request, written by audit.py::log_request). Each record has: timestamp, event ("request"), path, creator_id, input_chars, input_preview (first 80 characters), status_code, content_id, guess, confidence, error and duration_ms. Failed requests are logged too: a rejected input leaves a request entry with its status_code and error, plus a "rejected" entry with the reason (for example too_few_words, control_characters or rate_limited). I tested the failure path by sending "!!! ???", which returned a 400 and left both entries in 22 ms.

Ten request entries from logs/audit.jsonl (capstone "before" run; five accepted, five rejected with a 400):

```
{"timestamp": "2026-11-11T23:58:31+00:00", "event": "request", "path": "/submit", "creator_id": "cap_before_1794441502_t1_warmup", "input_chars": 155, "input_preview": "I went to the store yesterday and forgot my wallet, which was embarrassing. The ", "status_code": 200, "content_id": "bb0d8d69-0440-4c5c-84c5-f8f3ec1e8ed4", "guess": "unsure", "confidence": 0.5868, "error": null, "duration_ms": 8857.8}
{"timestamp": "2026-11-11T23:58:33+00:00", "event": "request", "path": "/submit", "creator_id": "cap_before_1794441502_t1_c2_valid_0", "input_chars": 155, "input_preview": "I went to the store yesterday and forgot my wallet, which was embarrassing. The ", "status_code": 200, "content_id": "7c457816-4fb0-47cf-bc0f-6a2309a722d1", "guess": "unsure", "confidence": 0.5868, "error": null, "duration_ms": 1300.1}
{"timestamp": "2026-11-11T23:58:34+00:00", "event": "request", "path": "/submit", "creator_id": "cap_before_1794441502_t1_c2_valid_1", "input_chars": 155, "input_preview": "I went to the store yesterday and forgot my wallet, which was embarrassing. The ", "status_code": 200, "content_id": "2c22c1c2-3559-49b4-ba7f-72062956f06b", "guess": "unsure", "confidence": 0.5868, "error": null, "duration_ms": 1308.7}
{"timestamp": "2026-11-11T23:58:35+00:00", "event": "request", "path": "/submit", "creator_id": "cap_before_1794441502_t1_c2_valid_2", "input_chars": 155, "input_preview": "I went to the store yesterday and forgot my wallet, which was embarrassing. The ", "status_code": 200, "content_id": "53a86664-c039-40ef-a2a1-a22515c4024b", "guess": "unsure", "confidence": 0.5868, "error": null, "duration_ms": 593.5}
{"timestamp": "2026-11-11T23:58:35+00:00", "event": "request", "path": "/submit", "creator_id": "cap_before_1794441502_t1_c2_valid_3", "input_chars": 155, "input_preview": "I went to the store yesterday and forgot my wallet, which was embarrassing. The ", "status_code": 200, "content_id": "bf979b73-87e3-489a-90e1-0433a1f39f23", "guess": "unsure", "confidence": 0.5868, "error": null, "duration_ms": 453.6}
{"timestamp": "2026-11-11T23:58:22+00:00", "event": "request", "path": "/submit", "creator_id": "cap_before_1794441502_t1_junk_control_characters", "input_chars": 6, "input_preview": "\u0000\u0001\u0002 \u0003\u0004", "status_code": 400, "content_id": null, "guess": null, "confidence": null, "error": "bad_request", "duration_ms": 60.5}
{"timestamp": "2026-11-11T23:58:23+00:00", "event": "request", "path": "/submit", "creator_id": "cap_before_1794441502_t1_junk_punctuation_only", "input_chars": 19, "input_preview": "!!! ??? ... ,,, ;;;", "status_code": 400, "content_id": null, "guess": null, "confidence": null, "error": "bad_request", "duration_ms": 18.4}
{"timestamp": "2026-11-11T23:58:23+00:00", "event": "request", "path": "/submit", "creator_id": "cap_before_1794441502_t1_junk_one_long_word", "input_chars": 200, "input_preview": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "status_code": 400, "content_id": null, "guess": null, "confidence": null, "error": "bad_request", "duration_ms": 16.6}
{"timestamp": "2026-11-11T23:58:23+00:00", "event": "request", "path": "/submit", "creator_id": "cap_before_1794441502_t1_junk_emoji_only", "input_chars": 8, "input_preview": "😀😀😀😀😀😀😀😀", "status_code": 400, "content_id": null, "guess": null, "confidence": null, "error": "bad_request", "duration_ms": 10.4}
{"timestamp": "2026-11-11T23:58:41+00:00", "event": "request", "path": "/submit", "creator_id": "cap_before_1794441502_t1_c2_bad_0", "input_chars": 0, "input_preview": "", "status_code": 400, "content_id": null, "guess": null, "confidence": null, "error": "bad_request", "duration_ms": 11.4}
```


## What It Costs

The service runs locally and calls no paid API, so the cost of a run is $0.00 in spend and a measured amount of compute time. I measured it with the duration_ms field in the log: the warm valid requests from my three "before" trials (30 requests in total, 10 per trial, after the model was loaded). The trial averages were 705 ms, 318 ms and 1,173 ms, and the overall average is 21,967 ms / 30 = **732 ms per run**. The first request after starting the service took 39,242 ms because GPT-2 loads then, and 6,534 ms after my improvement.

For a hundred people a day, if each submits one piece: 100 x 0.732 s = 73 s, about 1.2 minutes of compute a day. If each submits five: 500 x 0.732 s = 366 s, about 6 minutes a day. It costs nothing in fees, and the limit that matters is memory, not money (see What's Still Broken).

## Run Log and Verdicts

Run with `python run_capstone.py --label before` (function run_trial; results in results/capstone_before_1794441502.md), three trials, nothing changed in between. I committed criteria.md in the commit "add capstone criteria" before the commit "capstone first results". Neither signal is random, so identical trials are expected.

| # | Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|---|
| 1 | Junk input gets a 400 | 4 of 4 | 4/4 | 4/4 | 4/4 | MET |
| 2 | 20 requests logged with a duration | 20 of 20 | 20/20 | 20/20 | 20/20 | MET |
| 3 | Warm request under 3 s | 9 of 10 | 10/10 | 10/10 | 10/10 | MET |
| 4 | Bad request gets a 400 and a rejected entry | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5 | 429 on the 11th request, and 5 of 5 appeals | both hold | pass | pass | pass | MET |

Real output (run_capstone.py, trial 1):

```
c1 junk -> 400:       4 of 4
c2 logged w/ time:    20 of 20
c3 warm under 3s:     10 of 10
c4 bad -> 400+log:    5 of 5
c5 429 + appeals:     429 ok | 5 of 5 appeals
```

All five were met, so my targets were too low. The clearest case is criterion 3: warm requests took 287 to 1,929 ms, far under 3 seconds. A tighter target, **under 1,000 ms in 9 of 10**, would have been MISSED in trial 1 (8 of 10 under 1,000 ms) and trial 3 (5 of 10), because the same machine ran about three times slower in trial 3. Criterion 1 was also weak: it tested the same four inputs I wrote the validation for, and the three-word gibberish "asdf qwer zxcv" passes validation and is scored "human" at 0.2505. I did not revise any criterion.

## The Improvement

**Change:** I load the GPT-2 model when the service starts (app.py::main calls detector.warm_up()) and changed nothing else.

**Why:** the log showed my first request took 39,241.9 ms (duration_ms) because the model loads on that request. No criterion measured it, and a writer or a classmate at Demo Day would hit it first.

**Result:** the first request after starting now takes 6,533.9 ms instead of 39,241.9 ms, about 83% faster. The wait moved to startup, where the model prints "gpt2 loaded and ready." It did not disappear, and the first request is still much slower than a warm one.

**Run Log: After** (`python run_capstone.py --label after`, results/capstone_after_1794443192.md):

| # | Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|---|
| 1 | Junk input gets a 400 | 4 of 4 | 4/4 | 4/4 | 4/4 | MET |
| 2 | 20 requests logged with a duration | 20 of 20 | 20/20 | 20/20 | 20/20 | MET |
| 3 | Warm request under 3 s | 9 of 10 | 10/10 | 10/10 | 10/10 | MET |
| 4 | Bad request gets a 400 and a rejected entry | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5 | 429 on the 11th request, and 5 of 5 appeals | both hold | pass | pass | 4 of 5 appeals | MISSED |

Real output (run_capstone.py, trial 3):

```
c3 warm under 3s:     10 of 10
c4 bad -> 400+log:    5 of 5
c5 429 + appeals:     429 ok | 4 of 5 appeals
```

**Did it help?** Yes on the problem I targeted: the cold start fell from 39,242 ms to 6,534 ms. The cost is that criterion 5 went from MET to MISSED in trial 3. I cannot say the change caused that miss: the model is loaded once either way, and the cause below points at memory pressure while Zoom and other apps were open.

**Diagnosis of the miss (criterion 5, trial 3).** Component: the route, app.py::submit, at the call to detector.model_signal. Mechanism: Terminal 1 shows one POST /submit returned 500 with `RuntimeError: ... DefaultCPUAllocator: not enough memory` while GPT-2 was scoring. submit() only catches ValueError and DetectorUnavailable, so the RuntimeError escaped as an unhandled 500. My test script got no content_id for that creator (ap_3), skipped its appeal, and counted 4 of 5. The log has no entry at all for that creator, so the failure left no trace; I believe debug mode re-raises the exception before my logging hook runs, but I did not verify that. When I reran check_appeals.py afterwards it passed 15 of 15 appeals, so the appeal path itself works.

## What's Still Broken

- **Criterion 5 (unhandled model errors).** The first thing I would do next: catch unexpected exceptions around model_signal in submit(), return a 503 with a clear message, and write a rejection entry, so a memory failure is visible and the caller gets an answer instead of a crash. I stopped because the brief allows one improvement, and the cold start was the failure I had already measured.
- **Gibberish is scored.** "asdf qwer zxcv" has three words, passes validation and is labeled "human" (0.2505). Fixing it needs a check for real words, which is more than one small change.
- **Edited AI text (EV05) and PI02** from Unit 8 still get "human", because the signals can't see them. I left them out of scope.
- **Cold start.** The first request still takes about 6.5 seconds.
- **Memory.** The service needs about 5 GB of free disk and several GB of RAM for PyTorch, so it cannot run on a 512 MB host.
- **Targets set too low.** I would tighten criterion 3 to under 1,000 ms in 9 of 10, and criterion 1 to include inputs I did not write the validation for.

## How I Used AI

**Moment 1:** I asked Claude for code to reject the junk inputs that my service had scored in the Unit 8 attack run. It gave me a check for control characters and for fewer than three words. I tested it with "!!! ???" (a 400 in 22 ms) and by rerunning the 56-attack set, where all four junk attacks changed to 400 and the right-to-left script was still accepted.

**Moment 2:** When criterion 5 missed in trial 3, I pasted my Terminal 1 output into Claude. It found the out-of-memory RuntimeError in the traceback and pointed out that the creator with no log entry was the one whose submit crashed. I wrote the diagnosis from that evidence and noted what I could not verify. I chose the numbers for my five criteria myself, and Claude drafted the wording and the reasons, which I read before committing.

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
