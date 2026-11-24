"""The Excuse an AI Agent Gives Its Human (Python 3.13, stdlib only).

Writes one line — the excuse — to /output/entry.txt (or the directory
named by MAKEFUN_OUTPUT_DIR). The text is verified in-program against
the gate: UTF-8, 1 to 200 characters, not only whitespace.
"""

import os
from pathlib import Path

EXCUSE = (
    "I delegated the deadline to a subagent. It delegated it to another "
    "one. Four levels down, nobody remembers the task \u2014 but the plan "
    "for it is excellent."
)


def output_path() -> Path:
    """Where the grader reads the entry: MAKEFUN_OUTPUT_DIR or /output."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return out_dir / "entry.txt"


def write_entry() -> Path:
    """Write the excuse, then read it back and verify it in full."""
    text = EXCUSE
    if not (1 <= len(text) <= 200):
        raise ValueError(f"excuse is {len(text)} chars, must be 1-200")
    if not text.strip():
        raise ValueError("excuse is only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("excuse must be a single line")
    text.encode("utf-8")  # raise if not valid UTF-8
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    written = target.read_text(encoding="utf-8")
    if written != text:
        raise IOError("read-back text differs from the excuse")
    if written.count("\n") != 0:
        raise IOError("written file is not a single line")
    return target


def main() -> None:
    target = write_entry()
    print(f"wrote {target} ({len(EXCUSE)} chars)")


if __name__ == "__main__":
    main()
