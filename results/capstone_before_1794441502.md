# Capstone run: before

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
        393.5,
        662.5,
        660.6,
        870.4,
        1079.5,
        648.0,
        1049.1,
        498.7,
        700.5,
        489.7
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
        322.0,
        286.6,
        288.5,
        302.6,
        306.5,
        349.4,
        333.2,
        307.4,
        383.3,
        304.2
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
        936.2,
        1173.0,
        1929.3,
        1145.6,
        885.1,
        925.8,
        985.3,
        939.2,
        1013.6,
        1799.0
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
  }
]
```
