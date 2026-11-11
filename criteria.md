# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. False positives

Of 10 pieces of writing that I wrote myself (each at least 100 words), at most 1 receives the high-confidence AI label.

**Why this target:** a wrong accusation costs a real writer far more than a missed AI piece, because it can end their relationship with the site. My first signal (GPT-2 perplexity) measures how predictable text is, and careful or formal human writing is predictable too, so some false positives are likely. I allow 1 in 10 because 0 is unrealistic for a detector this simple, and 2 in 10 would mean accusing one writer in five.

---

## 2. Score spread

The average combined confidence score of 5 pieces that an AI tool generated is at least 0.30 higher than the average of 5 pieces that I wrote myself.

**Why this target:** my two signals measure different things (predictability, and sentence and word patterns), but neither is strong alone. A gap of 0.30 is about a third of the 0 to 1 scale, enough to put clearly-AI and clearly-human text in different label ranges. A smaller gap would mean the "unsure" label swallows nearly everything.

---

## 3. Label coverage

I can produce each of the three labels (likely AI, likely human, not sure) at least once by submitting text to POST /submit. That is 3 of 3 labels reached, each with a piece of text I name.

**Why this target:** the labels are chosen by score ranges in scoring.py::score_to_label, and a gap or overlap in the ranges would leave some scores with no label or the wrong one. This is a plain code check, so it should pass every time, and scoring.label_ranges() prints the ranges so I can see where a gap would be.

---

## 4. The appeal path

In 5 of 5 test appeals, each using a valid content_id from an earlier submission, POST /appeal returns the status `under_review`, and GET /log then shows that content_id with the status `under_review` and the writer's reasoning.

**Why this target:** the appeal is the only way a writer who was wrongly labeled can push back, so it must never fail silently. It is plain code with no model involved, so any failure would be a bug in my handler, not randomness. That is why the target is 5 of 5.

---

## 5. Bad input

In 5 of 5 tries, POST /submit with bad input returns HTTP status 400 and an error message saying what is wrong. The five inputs are: no `text` field, an empty string for `text`, text made only of spaces, a number instead of a string for `text`, and no `creator_id`.

**Why this target:** a detector that crashes or returns a score for empty text would give writers a label on nothing. The check is a few lines of code before either signal runs, so it is deterministic, and anything below 5 of 5 would mean a gap in that check.



---


---

# Capstone criteria (Unit 9)

These are for the hardening extension: input validation, per-request logging with duration, and the run path. They were written before any capstone results.

## 1. Junk input is rejected

Four junk inputs sent to POST /submit each return HTTP 400: a text made only of control characters, a text made only of punctuation, a text that is one 200-character word, and a text made only of emoji. That is 4 of 4.

**Why this target:** in the Unit 8 attack run my service scored all four and called the control-character one "human" at 0.250. A score on text with no real words accuses or clears a writer on nothing, so I allow no exceptions, and 3 of 4 would mean one kind of junk still gets through.

## 2. Every request leaves a log record with a duration

I send 20 requests to POST /submit: 10 valid texts and 10 invalid ones, each with its own creator_id so the rate limiter is not involved. Each of the 20 produces an entry in logs/audit.jsonl with `"event": "request"`, a `status_code` and a `duration_ms`. That is 20 of 20.

**Why this target:** in Unit 8 a request that was rejected left no trace of how long it took, and an attack that shows up only as an absence is one I would never find. The log is plain code with no model in it, so any miss would be a bug in my hook and not randomness.

## 3. A warm valid request is fast

After the model has loaded (at least one earlier request to the running service), a valid 30-word text gets a response in under 3 seconds, in at least 9 of 10 requests, measured by the `duration_ms` field in the log.

**Why this target:** the first request took 39,242 ms because GPT-2 loads then, so this criterion is about warm requests only and says so. Nothing in the pipeline is random, so after warm-up I expect almost all requests to be fast, and 9 of 10 leaves room for one slow request from the machine itself.

## 4. Bad requests fail cleanly and leave a record

Five bad requests get HTTP 400 (never a 500) and each leaves an entry with `"event": "rejected"` in the log: no text field, a text of 25,000 characters, text given as a number, a body that is a JSON array and not an object, and a missing creator_id. That is 5 of 5.

**Why this target:** a crash on a malformed input is one of the most common real failures, and in Unit 8 my attack set found these paths. A 400 without a record would hide the failure, so I require both.

## 5. What already worked still works

(a) The 11th valid submission from one creator_id inside a minute gets HTTP 429. (b) In 5 of 5 tests, POST /appeal on a real content_id returns `"status": "under_review"` and the appeal appears in the log. Both must hold.

**Why this target:** this unit adds code to the same route, and an extension that breaks the rate limiter or the appeal path is a regression. The appeal is the only thing a wrongly accused writer can do, so it has to work every time.