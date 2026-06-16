from lib.sampling import build_messages


def test_no_system():
    assert build_messages("hi") == [{"role": "user", "content": "hi"}]


def test_with_system():
    assert build_messages("hi", system="sys") == [
        {"role": "system", "content": "sys"},
        {"role": "user", "content": "hi"},
    ]
