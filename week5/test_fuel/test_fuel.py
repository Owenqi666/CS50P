import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("100/100") == 100
    assert convert("99/100") == 99
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("1/100") == 1
    assert convert("0/100") == 0
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("9/6")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"