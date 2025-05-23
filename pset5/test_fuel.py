import pytest

from fuel import convert, gauge


def test_convert_valid():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("0/4") == 0
    assert convert("99/100") == 99


def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_convert_invalid_value():
    with pytest.raises(ValueError):
        convert("abc/def")
    with pytest.raises(ValueError):
        convert("5/2")
    with pytest.raises(ValueError):
        convert("2.3/5")


def test_gauge():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(75) == "75%"
    assert gauge(50) == "50%"
