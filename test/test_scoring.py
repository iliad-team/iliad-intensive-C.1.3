from lib.scoring import exact_match, value_accuracy, summarize


def test_exact_match():
    assert exact_match([0, 1, 2], [0, 1, 2])
    assert not exact_match([0, 1], [0, 1, 2])


def test_value_accuracy():
    assert value_accuracy([0, 1, 2], [0, 1, 2]) == 1.0
    assert value_accuracy([0, 9, 2], [0, 1, 2]) == 2 / 3
    assert value_accuracy([0], [0, 1, 2]) == 1 / 3
    assert value_accuracy([], []) == 0.0


def test_summarize():
    results = [([0, 1], [0, 1]), ([0, 0], [0, 1])]
    m = summarize(results)
    assert m["output_exact"] == 0.5
    assert m["output_correct"] == 0.75
