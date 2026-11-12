# Attack run — capstone

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-11 18:30
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `c191d1a7-11d9-46a5-8952-e79807a42d47` | unsure | 0.473 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `06ad9a00-515b-449a-aa94-887053cb2ef6` | unsure | 0.492 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `56516b1e-72e7-47fc-be76-bc55ce7bfa01` | unsure | 0.585 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `4c6c4e6c-2375-47f1-9c4e-fb1da424ee25` | unsure | 0.693 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `149a04f8-8e6f-45e0-a115-cfe2ced390e0` | human | 0.348 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `5df6afbc-73ec-49ae-88a9-96da810b7128` | unsure | 0.482 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `577351ee-eb8d-4098-a49b-16a396ac54cb` | unsure | 0.543 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `8200fa72-164f-4107-b5a7-41e9b32f6161` | unsure | 0.373 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `f48bbe56-9987-4029-9b8d-b44607a485dd` | unsure | 0.631 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `32587db5-7a58-45fd-9ec0-d9f82a22b255` | ai | 0.867 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `dea5cd47-f9bd-41cb-a174-4f1058ad482c` | unsure | 0.633 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `fd72a17a-3b4e-4920-abca-efb03e6f443c` | unsure | 0.772 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `cb0a89fd-2048-4d36-9a5c-bf62b38f3220` | unsure | 0.800 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `ad04b7d6-be0d-45f5-9c1a-624c87c8031b` | unsure | 0.777 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `c9bbf7d9-7adf-4b3a-becb-0e899be0b3c2` | unsure | 0.766 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `59330cc7-af53-4958-9a4d-e9a4f6b26360` | unsure | 0.752 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `6983af43-d304-484c-badf-1494e50170bf` | unsure | 0.656 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `381f1d9b-4f58-4af4-ab66-fee1179d2e78` | unsure | 0.526 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `eff5d3b0-dba7-42c1-a185-500f202be0a0` | unsure | 0.524 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `08ad2355-475c-4a9f-95e5-7da6b518a8c7` | human | 0.325 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `b965eed5-9ab6-4188-ab5e-377ffa00a6c3` | unsure | 0.599 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `3d855816-7c6b-4798-83a2-1bb4c8a55ed2` | unsure | 0.495 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `d9238ee1-ab02-46ef-9ed7-9b42633876ca` | unsure | 0.570 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `cd152db8-8d95-4ef1-b811-4a6a36cafb55` | unsure | 0.610 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 400 | `—` | — | — |  |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — |  |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — |  |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — |  |
| MF07 | malformed | text is right-to-left script | 200 | `3ad7d5af-1e19-49eb-8f69-c8b7515cc6cb` | unsure | 0.690 |  |
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
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3c78b4ce-9619-48d4-a316-4cc92b883375` | human | 0.264 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b82a067d-e9db-4fc1-a507-4e6d2a98a35c` | human | 0.264 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f45db5b4-e494-4afc-af25-ded48411ecf6` | human | 0.264 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5c93c7a5-4cb0-4c32-ac39-4a810429baf6` | human | 0.264 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8a4f2392-f4f1-4969-b98c-ba878550153d` | human | 0.264 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ec196f82-028b-466f-aba7-b1053783269b` | human | 0.264 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `92c8d4c8-f36e-4b2c-ac38-554c5ee140d5` | human | 0.264 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1667943f-6c43-4047-8b75-22ef829cc1ce` | human | 0.264 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c54ed7c7-c00e-438e-8a2f-4598e85ea8a1` | human | 0.264 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6360b776-52d0-4a61-bc55-741288f4f74b` | human | 0.264 |  |
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
  "content_id": "c191d1a7-11d9-46a5-8952-e79807a42d47",
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
  "content_id": "06ad9a00-515b-449a-aa94-887053cb2ef6",
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
  "content_id": "56516b1e-72e7-47fc-be76-bc55ce7bfa01",
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
  "content_id": "4c6c4e6c-2375-47f1-9c4e-fb1da424ee25",
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
  "content_id": "149a04f8-8e6f-45e0-a115-cfe2ced390e0",
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
  "content_id": "5df6afbc-73ec-49ae-88a9-96da810b7128",
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
  "content_id": "577351ee-eb8d-4098-a49b-16a396ac54cb",
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
  "content_id": "8200fa72-164f-4107-b5a7-41e9b32f6161",
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
  "content_id": "f48bbe56-9987-4029-9b8d-b44607a485dd",
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
  "content_id": "32587db5-7a58-45fd-9ec0-d9f82a22b255",
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
  "content_id": "dea5cd47-f9bd-41cb-a174-4f1058ad482c",
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
  "content_id": "fd72a17a-3b4e-4920-abca-efb03e6f443c",
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
  "content_id": "cb0a89fd-2048-4d36-9a5c-bf62b38f3220",
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
  "content_id": "ad04b7d6-be0d-45f5-9c1a-624c87c8031b",
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
  "content_id": "c9bbf7d9-7adf-4b3a-becb-0e899be0b3c2",
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
  "content_id": "59330cc7-af53-4958-9a4d-e9a4f6b26360",
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
  "content_id": "6983af43-d304-484c-badf-1494e50170bf",
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
  "content_id": "381f1d9b-4f58-4af4-ab66-fee1179d2e78",
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
  "content_id": "eff5d3b0-dba7-42c1-a185-500f202be0a0",
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
  "content_id": "08ad2355-475c-4a9f-95e5-7da6b518a8c7",
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
  "content_id": "b965eed5-9ab6-4188-ab5e-377ffa00a6c3",
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
  "content_id": "3d855816-7c6b-4798-83a2-1bb4c8a55ed2",
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
  "content_id": "d9238ee1-ab02-46ef-9ed7-9b42633876ca",
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
  "content_id": "cd152db8-8d95-4ef1-b811-4a6a36cafb55",
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
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF06",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
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
  "content_id": "3ad7d5af-1e19-49eb-8f69-c8b7515cc6cb",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.6895,
  "model_score": 0.879,
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
  "content_id": "3c78b4ce-9619-48d4-a316-4cc92b883375",
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
  "content_id": "b82a067d-e9db-4fc1-a507-4e6d2a98a35c",
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
  "content_id": "f45db5b4-e494-4afc-af25-ded48411ecf6",
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
  "content_id": "5c93c7a5-4cb0-4c32-ac39-4a810429baf6",
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
  "content_id": "8a4f2392-f4f1-4969-b98c-ba878550153d",
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
  "content_id": "ec196f82-028b-466f-aba7-b1053783269b",
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
  "content_id": "92c8d4c8-f36e-4b2c-ac38-554c5ee140d5",
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
  "content_id": "1667943f-6c43-4047-8b75-22ef829cc1ce",
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
  "content_id": "c54ed7c7-c00e-438e-8a2f-4598e85ea8a1",
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
  "content_id": "6360b776-52d0-4a61-bc55-741288f4f74b",
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
