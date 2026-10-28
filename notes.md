# Milestone 1: tracing a submission

## 1. The path a piece of text takes

1. A writing site sends `POST /submit` with `text` and `creator_id`.
2. The service checks the input (is the text there, is it too long). If not, it returns an error and stops.
3. Signal one (detector.py, the GPT-2 model) reads the text and returns a score from 0 to 1, where higher means more likely AI.
4. Signal two (stylometry.py, my own) measures the text as text: sentence length spread, word variety and punctuation. It returns its own score from 0 to 1.
5. scoring.py::combine_signals turns the two scores into one confidence score.
6. scoring.py::score_to_label turns that number into one of three labels: likely AI, likely human, or not sure.
7. The service writes everything to logs/audit.jsonl (both signal scores, the combined score, the label, a content_id) and sends the JSON back.

## 2. The two signals

**Signal one: the GPT-2 detector (perplexity).**
- What it measures: how predictable each word is to a language model.
- Why it differs: AI text tends to pick likely words, so it is predictable. Human text is more surprising.
- What it can’t see: authorship. It rewards common words in short, ordinary sentences, so a real writer who writes plainly (for example, in a second language) can score as AI, and dense ornate prose can score as human. The people it is most likely to accuse are the ones with the least room to argue back.

**Signal two: stylometry (the text as text).**
- What it measures: how much sentence length varies, the ratio of unique words to total words, and how much punctuation is used.
- Why it differs: people often write in uneven bursts (a short sentence, then a long one), and AI often writes evenly.
- What it can't see: meaning. It can't tell whether the ideas are original. A careful human writer with a smooth, even style looks AI, and AI text with typos or varied sentences looks human.

**Where they can disagree:** a polished essay by a human might score high on signal one (predictable) and low on signal two (varied sentences). The combining rule has to decide what to do with that split.

## 3. The false positive

A real writer submits a poem or essay they wrote themselves, in a plain-writing style. Signal one scores it as predictable (high), and signal two scores it as even (high). The combined score lands in the high range.

- What the label says to them: if it says "this was written by AI", they've been accused of cheating, which could end their relationship with the site.
- Because of this, my high-confidence AI label has to be hard to reach. The threshold for "likely AI" should sit high, and the middle range should show a careful "not sure" message, not an accusation.
- What they can do: send an appeal (`POST /appeal`) with their reasoning. The item moves to `under_review`, and the appeal is recorded next to the original decision.

## 4. The two endpoints

**POST /submit**
- In: `{"text": "...", "creator_id": "..."}`
- Out: `{"content_id": "...", "guess": "ai" or "human" or "unsure", "confidence": 0.0 to 1.0, "label": "the full sentence shown to a reader"}`
- Errors: missing or empty text returns a 400 with a message saying what is wrong.

**POST /appeal**
- In: `{"content_id": "...", "reasoning": "..."}`
- Out: `{"content_id": "...", "status": "under_review", "message": "confirmation text"}`
- Errors: an unknown content_id returns a 404.