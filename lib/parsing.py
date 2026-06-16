import re

_INT_RE = re.compile(r"-?\d+")


def parse_values(text: str) -> list[int]:
    """Extract all integers from text, in order."""
    return [int(x) for x in _INT_RE.findall(text)]
