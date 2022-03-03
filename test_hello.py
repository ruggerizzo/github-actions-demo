from hello import add


def test_add():
    assert 2 == add(1, 1)


def test_add_more():
    assert 5 == add(4, 1)

def test_add_azure():
    assert 99 == add(add(20,60), add(10,9))

def test_add_gcp():
    assert 23 == add(add(20,3), add(0,0))