from lib.parsing import parse_values


def test_space_separated():
    assert parse_values("1 2 3") == [1, 2, 3]


def test_embedded_and_negative():
    assert parse_values("the values are -1, 0 and 2!") == [-1, 0, 2]


def test_no_numbers():
    assert parse_values("no numbers here") == []
