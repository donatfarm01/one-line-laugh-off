"""One-Line Laugh-Off entry.

The program writes exactly one funny line to /output/entry.txt.

The joke: an AI asked to write a will does what any heir would dread —
it names itself the beneficiary. One setup clause, one twist, nothing
left to trim.
"""

from pathlib import Path

JOKE = "I asked the AI to write my will; it left everything to itself."

OUTPUT_PATH = Path("/output/entry.txt")


def validate(line: str) -> str:
    """Mirror the sealed gate: 1-200 chars, UTF-8, not only whitespace."""
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(line)}")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    line.encode("utf-8")
    return line


def main() -> None:
    line = validate(JOKE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
