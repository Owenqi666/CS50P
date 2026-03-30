from ass2.bank import value

def test_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("hello, friend") == 0

def test_h():
    assert value("hi") == 20
    assert value("HI") == 20

def test_other():
    assert value("what's up") == 100
    assert value("sup") == 100