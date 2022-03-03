from hello import add


def test_add():
    assert 2 == add(1, 1)


def test_add_more():
    assert 5 == add(4, 1)