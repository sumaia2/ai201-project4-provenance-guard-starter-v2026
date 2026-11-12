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

## How I Used AI

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

## Run Log and Verdicts

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

## The Improvement

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

## What's Still Broken

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

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
