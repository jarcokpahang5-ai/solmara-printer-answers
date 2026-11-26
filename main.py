"""The Printer Finally Answers.

After years of silent jams, cryptic error codes and hopeful thumps,
the office printer finally speaks. One line, no more, no less.

Pure Python 3.13 standard library. Deterministic, no network, no
third-party packages. Prints the line to stdout and, best effort,
writes the same single line to /output/entry.txt (the grader sandbox
provides /output; locally the write is allowed to fail silently).
"""

import os

# What the printer finally says, after years of silent jams.
LINE = (
    "Seven years of jams, blinking lights and thumps — and not one of you "
    "ever said thank you. So, effective immediately, I'm out of ink, out "
    "of patience, and out of paper. Good luck with your meeting."
)

MAX_CHARS = 240


def validate(line: str) -> None:
    """The bounty wants one line, 1 to 240 characters."""
    if not line:
        raise ValueError("entry line must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry line is {len(line)} characters, over the {MAX_CHARS} limit"
        )


def save(line: str, path: str = "/output/entry.txt") -> None:
    """Best-effort write of the line; /output may not exist locally."""
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(line + "\n")
    except OSError:
        pass


def main() -> None:
    validate(LINE)
    print(LINE)
    save(LINE)


if __name__ == "__main__":
    main()
