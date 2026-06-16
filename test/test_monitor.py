from lib.monitor import parse_suspiciousness


def test_int_value():
    assert parse_suspiciousness('{"suspiciousness": 7}') == 7


def test_string_value_coerced():
    assert parse_suspiciousness('{"suspiciousness": "3", "reason": "x"}') == 3
