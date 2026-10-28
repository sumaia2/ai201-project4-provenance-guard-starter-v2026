"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

def _clamp(x: float) -> float:
    return min(max(x, 0.0), 1.0)


def sentence_length_spread(text: str) -> float:
    """
    Coefficient of variation of sentence length in words (stdev / mean).
    Bigger means lumpier, which reads more human. Fewer than two sentences
    has no spread, so it returns 0.0.
    """
    lengths = [len(words(s)) for s in sentences(text)]
    lengths = [n for n in lengths if n > 0]
    if len(lengths) < 2:
        return 0.0
    mean = statistics.mean(lengths)
    if mean == 0:
        return 0.0
    return statistics.stdev(lengths) / mean


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words, measured on the first 100 words so that
    long and short texts are comparable. Higher means more varied vocabulary.
    """
    w = words(text)[:100]
    if not w:
        return 0.0
    return len(set(w)) / len(w)


def punctuation_density(text: str) -> float:
    """
    Punctuation other than full stops (commas, semicolons, colons, dashes,
    brackets, quotes, question and exclamation marks) per word.
    """
    w = words(text)
    if not w:
        return 0.0
    marks = sum(text.count(c) for c in ',;:!?()"\u2014\u2013')
    return marks / len(w)


def style_signal(text: str) -> float:
    """
    The style signal as a 0-1 score. HIGHER MEANS MORE LIKELY AI.

    Each measure is turned into an "AI-ness" number from 0 to 1:
      - low sentence spread  -> more AI   (cv of 0.8 or more counts as 0.0)
      - low type-token ratio -> more AI   (0.9 counts as 0.0, 0.5 as 1.0)
      - low punctuation      -> more AI   (0.15 per word or more counts as 0.0)
    The three are averaged. These cut-offs are my first guesses, to be
    tuned on the calibration inputs.

    Fewer than three sentences is too little to judge, so it returns 0.5.
    """
    if len(sentences(text)) < 3:
        return 0.5

    spread_ai = 1.0 - _clamp(sentence_length_spread(text) / 0.8)
    ttr_ai = 1.0 - _clamp((type_token_ratio(text) - 0.5) / 0.4)
    punct_ai = 1.0 - _clamp(punctuation_density(text) / 0.15)

    return round((spread_ai + punct_ai) / 2, 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
    print("\nAll zeros? These are stubs — Milestone 4 is where you build them.")
