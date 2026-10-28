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

**Combining rule (scoring.py::combine_signals).** The combined score is 0.5 x model_score + 0.5 x style_score. If either signal is below 0.5, the combined score is capped at 0.64 (the AI threshold minus 0.01), so a high-confidence AI result needs both signals to lean AI. I chose this because a wrong accusation costs a real writer more than a missed AI piece. The weights are in config.py (WEIGHT_MODEL_SIGNAL and WEIGHT_STYLE_SIGNAL, both 0.5).

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

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
