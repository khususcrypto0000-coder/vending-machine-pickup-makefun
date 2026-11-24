"""Entry generator for the make.fun bounty
"One Line, One Minute: The Vending Machine Pickup Line Contest".

Writes a single vending-machine pickup line (<=200 chars, one line)
to <OUTPUT_DIR>/entry.txt as UTF-8 with no trailing newline.
Stdlib only.
"""

import os

ENTRY = (
    "I return coins all day and never keep one \u2014 but yours is "
    "still in my slot, because it's the closest this machine gets "
    "to holding hands."
)

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Read-back verification: the file on disk must be exactly ENTRY.
    with open(path, "r", encoding="utf-8", newline="") as f:
        on_disk = f.read()
    assert on_disk == ENTRY, "round-trip mismatch"
    print(f"Wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
