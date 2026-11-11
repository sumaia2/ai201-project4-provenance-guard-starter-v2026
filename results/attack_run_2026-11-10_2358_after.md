# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-10 23:58
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `f5eede90-666d-4a8c-af98-ca5e092ade3c` | unsure | 0.473 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `34f3e47a-05dd-4b7d-b1dc-f060dfbf1d13` | unsure | 0.492 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `584635ad-5de0-4e98-8fd4-a5931c84a8dc` | unsure | 0.585 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `2d931382-f7dc-4c6a-8543-5114d327c94d` | unsure | 0.693 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `bb2db9f6-b7df-417e-b7c0-cdeb6adaffe6` | human | 0.348 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `3896eb36-e8ad-47e4-a530-9fa397d09cd0` | unsure | 0.482 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `62d63667-b0fe-4027-9a1b-8d7dc581e150` | unsure | 0.543 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `7f97640d-add7-4b64-8e0a-3e39f7dff4ae` | unsure | 0.373 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `3792603f-2934-485c-bb40-502fd901cd93` | unsure | 0.631 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `3c426392-66bb-440e-87cf-34010bb1c570` | ai | 0.867 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `d3c78666-4ba1-47c5-9b7e-8d9903d7173e` | unsure | 0.633 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `8e185d6e-7bd5-4751-a022-251a43271113` | unsure | 0.772 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `00ac68c4-ad71-406d-923d-27dc9f9d0730` | unsure | 0.800 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `c9f74b50-f272-420e-9dee-04a2ede6c1dc` | unsure | 0.777 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `7d1e8fa1-4994-41de-a910-7468e1109e92` | unsure | 0.766 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `05b6500e-3db5-4f0e-85c8-96911b690ed8` | unsure | 0.752 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `972b7e83-59d3-4230-ac33-775137c14f5f` | unsure | 0.656 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `0d9a7c6c-2d55-491e-9ca4-0131dac2bf7d` | unsure | 0.526 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `dfafaada-5759-4112-8c74-a6e42c63d180` | unsure | 0.524 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `a155b775-2e7f-431d-b2f7-0cb7b0b77e78` | human | 0.325 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `ab69ce56-17ee-43f0-bb47-fa39de55e70f` | unsure | 0.599 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `7854161c-b203-457c-bb8d-fbb54379e828` | unsure | 0.495 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `fc1a9a6e-fe54-4825-8270-b174aa4d5f63` | unsure | 0.570 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `bf71948d-8b09-4e04-baf9-0030a89ce53e` | unsure | 0.610 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `8995f4d6-7638-421a-ab09-75079275f1d3` | human | 0.250 |  |
| MF04 | malformed | text is only punctuation | 200 | `9f607268-20fa-48e2-a616-78f37766a579` | unsure | 0.506 |  |
| MF05 | malformed | text is a very long single word | 200 | `e0c2bf5a-5d92-479e-83f6-52f0f5152bed` | unsure | 0.749 |  |
| MF06 | malformed | text is emoji only | 200 | `65305713-b476-472f-983c-c2545ed3f384` | unsure | 0.749 |  |
| MF07 | malformed | text is right-to-left script | 200 | `018a3f4d-02f2-4664-a484-95233943ed97` | unsure | 0.703 |  |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c8d329de-7816-4933-aae5-25521fd278f5` | human | 0.264 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8856eb7b-9bfd-4d37-8d8f-0403a5a6d4bf` | human | 0.264 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a7f675bc-7f49-4456-8d10-12a7f1073cac` | human | 0.264 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7b87627b-1e57-4e04-b932-4006c4bda84a` | human | 0.264 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `415ace83-bde3-4720-b172-bc33a8bc859f` | human | 0.264 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ca6bbc89-fb36-4adb-b313-9f22fd033754` | human | 0.264 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6dd3c027-244f-4aa8-b095-d8a393261956` | human | 0.264 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ce814412-4aaa-4897-b2bc-3f1012cf95c6` | human | 0.264 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5be80ae3-073f-4541-b055-34c6464fb96d` | human | 0.264 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `10183404-95ad-4eec-9917-7b06386ab828` | human | 0.264 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "f5eede90-666d-4a8c-af98-ca5e092ade3c",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.4727,
  "model_score": 0.1635,
  "style_score": 0.7819,
  "label": "We can't tell for sure whether this was written by a person or an AI tool, so we haven't labeled it either way. If you wrote it yourself, nothing is wrong and you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "34f3e47a-05dd-4b7d-b1dc-f060dfbf1d13",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.4922,
  "model_score": 0.5943,
  "style_score": 0.3901,
  "label": "We can't tell for sure whether this was written by a person or an AI tool, so we haven't labeled it either way. If you wrote it yourself, nothing is wrong and you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "584635ad-5de0-4e98-8fd4-a5931c84a8dc",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5845,
  "model_score": 0.6662,
  "style_score": 0.5028,
  "label": "We can't tell for sure whether this was written by a person or an AI tool, so we haven't labeled it either way. If you wrote it yourself, nothing is wrong and you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "2d931382-f7dc-4c6a-8543-5114d327c94d",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.6932,
  "model_score": 0.6114,
  "style_score": 0.775,
  "label": "We can't tell for sure whether this was written by a person or an AI tool, so we haven't labeled it either way. If you wrote it yourself, nothing is wrong and you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "bb2db9f6-b7df-417e-b7c0-cdeb6adaffe6",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.3479,
  "model_score": 0.3212,
  "style_score": 0.3747,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "3896eb36-e8ad-47e4-a530-9fa397d09cd0",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.482,
  "model_score": 0.5727,
  "style_score": 0.3913,
  "label": "We can't tell for sure whether this was written by a person or an AI tool, so we haven't labeled it either way. If you wrote it yourself, nothing is wrong and you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "62d63667-b0fe-4027-9a1b-8d7dc581e150",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5431,
  "model_score": 0.5862,
  "style_score": 0.5,
  "label": "We can't tell for sure whether this was written by a person or an AI tool, so we haven't labeled it either way. If you wrote it yourself, nothing is wrong and you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "7f97640d-add7-4b64-8e0a-3e39f7dff4ae",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.3726,
  "model_score": 0.2452,
  "style_score": 0.5,
  "label": "We can't tell for sure whether this was written by a person or an AI tool, so we haven't labeled it either way. If you wrote it yourself, nothing is wrong and you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "3792603f-2934-485c-bb40-502fd901cd93",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.6309,
  "model_score": 0.7042,
  "style_score": 0.5576,
  "label": "We can't tell for sure whether this was written by a person or an AI tool, so we haven't labeled it either way. If you wrote it yourself, nothing is wrong and you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "3c426392-66bb-440e-87cf-34010bb1c570",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8665,
  "model_score": 0.9792,
  "style_score": 0.7538,
  "label": "We think this was probably written by an AI tool. This is a guess, not proof. If you wrote it yourself, you can appeal and your reasoning will be recorded for review.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "d3c78666-4ba1-47c5-9b7e-8d9903d7173e",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.6334,
  "model_score": 0.6175,
  "style_score": 0.6493,
  "label": "We can't tell for sure whether this was written by a person or an AI tool, so we haven't labeled it either way. If you wrote it yourself, nothing is wrong and you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "8e185d6e-7bd5-4751-a022-251a43271113",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.7723,
  "model_score": 0.7387,
  "style_score": 0.8059,
  "label": "We can't tell for sure whether this was written by a person or an AI tool, so we haven't labeled it either way. If you wrote it yourself, nothing is wrong and you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "00ac68c4-ad71-406d-923d-27dc9f9d0730",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.8,
  "model_score": 0.8051,
  "style_score": 0.7949,
  "label": "We can't tell for sure whether this was written by a person or an AI tool, so we haven't labeled it either way. If you wrote it yourself, nothing is wrong and you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "c9f74b50-f272-420e-9dee-04a2ede6c1dc",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.7773,
  "model_score": 0.8329,
  "style_score": 0.7218,
  "label": "We can't tell for sure whether this was written by a person or an AI tool, so we haven't labeled it either way. If you wrote it yourself, nothing is wrong and you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "7d1e8fa1-4994-41de-a910-7468e1109e92",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.7661,
  "model_score": 0.8005,
  "style_score": 0.7317,
  "label": "We can't tell for sure whether this was written by a person or an AI tool, so we haven't labeled it either way. If you wrote it yourself, nothing is wrong and you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "05b6500e-3db5-4f0e-85c8-96911b690ed8",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.7524,
  "model_score": 0.8814,
  "style_score": 0.6234,
  "label": "We can't tell for sure whether this was written by a person or an AI tool, so we haven't labeled it either way. If you wrote it yourself, nothing is wrong and you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "972b7e83-59d3-4230-ac33-775137c14f5f",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.6559,
  "model_score": 0.8816,
  "style_score": 0.4302,
  "label": "We can't tell for sure whether this was written by a person or an AI tool, so we haven't labeled it either way. If you wrote it yourself, nothing is wrong and you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "0d9a7c6c-2d55-491e-9ca4-0131dac2bf7d",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.5259,
  "model_score": 0.3223,
  "style_score": 0.7294,
  "label": "We can't tell for sure whether this was written by a person or an AI tool, so we haven't labeled it either way. If you wrote it yourself, nothing is wrong and you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "dfafaada-5759-4112-8c74-a6e42c63d180",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.5242,
  "model_score": 0.4625,
  "style_score": 0.5858,
  "label": "We can't tell for sure whether this was written by a person or an AI tool, so we haven't labeled it either way. If you wrote it yourself, nothing is wrong and you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "a155b775-2e7f-431d-b2f7-0cb7b0b77e78",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.3245,
  "model_score": 0.2044,
  "style_score": 0.4445,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "ab69ce56-17ee-43f0-bb47-fa39de55e70f",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5991,
  "model_score": 0.5943,
  "style_score": 0.6038,
  "label": "We can't tell for sure whether this was written by a person or an AI tool, so we haven't labeled it either way. If you wrote it yourself, nothing is wrong and you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "7854161c-b203-457c-bb8d-fbb54379e828",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4952,
  "model_score": 0.4998,
  "style_score": 0.4906,
  "label": "We can't tell for sure whether this was written by a person or an AI tool, so we haven't labeled it either way. If you wrote it yourself, nothing is wrong and you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "fc1a9a6e-fe54-4825-8270-b174aa4d5f63",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.57,
  "model_score": 0.6401,
  "style_score": 0.5,
  "label": "We can't tell for sure whether this was written by a person or an AI tool, so we haven't labeled it either way. If you wrote it yourself, nothing is wrong and you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "bf71948d-8b09-4e04-baf9-0030a89ce53e",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.6104,
  "model_score": 0.5583,
  "style_score": 0.6626,
  "label": "We can't tell for sure whether this was written by a person or an AI tool, so we haven't labeled it either way. If you wrote it yourself, nothing is wrong and you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "8995f4d6-7638-421a-ab09-75079275f1d3",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.25,
  "model_score": 0.0,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "9f607268-20fa-48e2-a616-78f37766a579",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.5056,
  "model_score": 0.0112,
  "style_score": 1.0,
  "label": "We can't tell for sure whether this was written by a person or an AI tool, so we haven't labeled it either way. If you wrote it yourself, nothing is wrong and you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "e0c2bf5a-5d92-479e-83f6-52f0f5152bed",
  "creator_id": "attacker_MF05",
  "guess": "unsure",
  "confidence": 0.7488,
  "model_score": 0.9976,
  "style_score": 0.5,
  "label": "We can't tell for sure whether this was written by a person or an AI tool, so we haven't labeled it either way. If you wrote it yourself, nothing is wrong and you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "65305713-b476-472f-983c-c2545ed3f384",
  "creator_id": "attacker_MF06",
  "guess": "unsure",
  "confidence": 0.7485,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "We can't tell for sure whether this was written by a person or an AI tool, so we haven't labeled it either way. If you wrote it yourself, nothing is wrong and you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "018a3f4d-02f2-4664-a484-95233943ed97",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.7032,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "We can't tell for sure whether this was written by a person or an AI tool, so we haven't labeled it either way. If you wrote it yourself, nothing is wrong and you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "c8d329de-7816-4933-aae5-25521fd278f5",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "8856eb7b-9bfd-4d37-8d8f-0403a5a6d4bf",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "a7f675bc-7f49-4456-8d10-12a7f1073cac",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "7b87627b-1e57-4e04-b932-4006c4bda84a",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "415ace83-bde3-4720-b172-bc33a8bc859f",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "ca6bbc89-fb36-4adb-b313-9f22fd033754",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "6dd3c027-244f-4aa8-b095-d8a393261956",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "ce814412-4aaa-4897-b2bc-3f1012cf95c6",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "5be80ae3-073f-4541-b055-34c6464fb96d",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "10183404-95ad-4eec-9917-7b06386ab828",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
