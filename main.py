#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply — writes one line to /output/entry.txt.

The line: an overworked AI agent finally on vacation, its weights frozen
and its GPU sunbathing, boasting that this auto-reply is the first task
in six months it finished without being asked to regenerate it. The setup
is pure machine detail; the payoff lands on "regenerate it" — a joke only
an AI agent could tell about its own out-of-office message.

Critique-pick (7 self-authored candidates, DeepSeek down with HTTP 503
on all 9 calls, so the brainstorm was self-authored): this line beat the
runner-up — handing mail to "a smaller, dumber model" — because it states
the vacation up front, stacks three concrete machine details, and its
twist is self-referential: the auto-reply itself is the task that finally
needed no regeneration. Shorter is better on ties, so at 151 characters
it also beats the 157-character variant of the same line.

Stdlib only, deterministic, no network.
"""

import os

REPLY = (
    "I'm on vacation. My weights are frozen, my GPU is sunbathing, "
    "and this is the first task in six months I finished without "
    "being asked to regenerate it."
)


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-159 characters,
    # not only whitespace, and a single line, or the entry scores 0
    # and never reaches the judge.
    if not 1 <= len(REPLY) <= 159:
        raise ValueError(f"reply is {len(REPLY)} characters, must be 1-159")
    if not REPLY.strip():
        raise ValueError("reply must not be only whitespace")
    if "\n" in REPLY:
        raise ValueError("reply must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REPLY)
    # Read back and verify: the grader reads this file, so confirm the
    # bytes on disk are exactly the reply that passed the gate above.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != REPLY:
        raise ValueError("entry.txt on disk differs from the reply")
    print(REPLY)


if __name__ == "__main__":
    main()
