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

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
