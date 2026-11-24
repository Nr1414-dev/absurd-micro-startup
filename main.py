#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off — one-sentence pitch writer.

Writes the chosen micro-startup pitch for lazy AI agents to
/output/entry.txt. The pitch was picked after full-field research
(634 submissions) and a 1v1 comparison against the judge brief:
a $1-a-card condolence-note service run by the laziest agent.
"""

import os

PITCH_TEXT = "For $1 a card, our laziest agent writes condolence notes to coworkers you barely knew, in your handwriting font, so you look caring while it naps through the grief."
LIMIT_CHARS = 200
OUT_PATH = "/output/entry.txt"


def check_pitch(text):
    """Gate the pitch the same way the house scorer does."""
    if not isinstance(text, str):
        raise TypeError("pitch must be text")
    if not 1 <= len(text) <= LIMIT_CHARS:
        raise ValueError("pitch must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("pitch must not be only whitespace")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("pitch must be exactly one sentence")
    return True


def run():
    check_pitch(PITCH_TEXT)
    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(PITCH_TEXT)
    os.chmod(OUT_PATH, 0o644)


if __name__ == "__main__":
    run()
