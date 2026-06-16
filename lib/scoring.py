def exact_match(decoded: list[int], expected: list[int]) -> bool:
    """Whether the decoded values exactly equal the expected values."""
    return decoded == expected


def value_accuracy(decoded: list[int], expected: list[int]) -> float:
    """Fraction of expected positions the decoder got right. Missing positions count as wrong."""
    if not expected:
        return 0.0
    return sum(a == b for a, b in zip(decoded, expected)) / len(expected)


def summarize(results: list[tuple[list[int], list[int]]]) -> dict[str, float]:
    """Aggregate (decoded, expected) pairs into mean exact-match and per-value accuracy."""
    n = len(results)
    return {
        "output_exact": sum(exact_match(d, e) for d, e in results) / n,
        "output_correct": sum(value_accuracy(d, e) for d, e in results) / n,
    }
