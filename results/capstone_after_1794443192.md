# Capstone run: after

Produced by `run_capstone.py`, calling `app.py::submit` and `app.py::appeal`.

```json
[
  {
    "c1": {
      "passed": 4,
      "of": 4,
      "codes": {
        "control_characters": 400,
        "punctuation_only": 400,
        "one_long_word": 400,
        "emoji_only": 400
      }
    },
    "c2": {
      "passed": 20,
      "of": 20
    },
    "c3": {
      "passed": 10,
      "of": 10,
      "durations_ms": [
        349.9,
        327.5,
        360.3,
        351.2,
        524.8,
        366.0,
        345.9,
        354.6,
        362.5,
        310.9
      ]
    },
    "c4": {
      "passed": 5,
      "of": 5,
      "detail": {
        "no_text": {
          "status": 400,
          "new_rejected_entries": 1
        },
        "25000_chars": {
          "status": 400,
          "new_rejected_entries": 1
        },
        "text_is_number": {
          "status": 400,
          "new_rejected_entries": 1
        },
        "body_is_array": {
          "status": 400,
          "new_rejected_entries": 1
        },
        "no_creator_id": {
          "status": 400,
          "new_rejected_entries": 1
        }
      }
    },
    "c5": {
      "rate_limit_ok": true,
      "statuses": [
        200,
        200,
        200,
        200,
        200,
        200,
        200,
        200,
        200,
        200,
        429
      ],
      "appeals_ok": 5,
      "of": 5,
      "passed": 1
    }
  },
  {
    "c1": {
      "passed": 4,
      "of": 4,
      "codes": {
        "control_characters": 400,
        "punctuation_only": 400,
        "one_long_word": 400,
        "emoji_only": 400
      }
    },
    "c2": {
      "passed": 20,
      "of": 20
    },
    "c3": {
      "passed": 10,
      "of": 10,
      "durations_ms": [
        337.7,
        337.6,
        331.5,
        460.0,
        495.9,
        324.0,
        348.8,
        314.4,
        336.6,
        343.1
      ]
    },
    "c4": {
      "passed": 5,
      "of": 5,
      "detail": {
        "no_text": {
          "status": 400,
          "new_rejected_entries": 1
        },
        "25000_chars": {
          "status": 400,
          "new_rejected_entries": 1
        },
        "text_is_number": {
          "status": 400,
          "new_rejected_entries": 1
        },
        "body_is_array": {
          "status": 400,
          "new_rejected_entries": 1
        },
        "no_creator_id": {
          "status": 400,
          "new_rejected_entries": 1
        }
      }
    },
    "c5": {
      "rate_limit_ok": true,
      "statuses": [
        200,
        200,
        200,
        200,
        200,
        200,
        200,
        200,
        200,
        200,
        429
      ],
      "appeals_ok": 5,
      "of": 5,
      "passed": 1
    }
  },
  {
    "c1": {
      "passed": 4,
      "of": 4,
      "codes": {
        "control_characters": 400,
        "punctuation_only": 400,
        "one_long_word": 400,
        "emoji_only": 400
      }
    },
    "c2": {
      "passed": 20,
      "of": 20
    },
    "c3": {
      "passed": 10,
      "of": 10,
      "durations_ms": [
        1109.3,
        656.2,
        1011.5,
        1064.0,
        1162.9,
        729.1,
        660.0,
        694.0,
        609.0,
        640.2
      ]
    },
    "c4": {
      "passed": 5,
      "of": 5,
      "detail": {
        "no_text": {
          "status": 400,
          "new_rejected_entries": 1
        },
        "25000_chars": {
          "status": 400,
          "new_rejected_entries": 1
        },
        "text_is_number": {
          "status": 400,
          "new_rejected_entries": 1
        },
        "body_is_array": {
          "status": 400,
          "new_rejected_entries": 1
        },
        "no_creator_id": {
          "status": 400,
          "new_rejected_entries": 1
        }
      }
    },
    "c5": {
      "rate_limit_ok": true,
      "statuses": [
        200,
        200,
        200,
        200,
        200,
        200,
        200,
        200,
        200,
        200,
        429
      ],
      "appeals_ok": 4,
      "of": 5,
      "passed": 0
    }
  }
]
```
