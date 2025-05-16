import pytest

from jar import Jar


def test_init():
    jar = Jar(capacity=10)
    assert jar.capacity == 10

    with pytest.raises(ValueError):
        jar = Jar(capacity="10")


def test_cannot_change_capacity():
    jar = Jar(10)
    with pytest.raises(AttributeError):
        jar.capacity = 5


def test_cannot_change_size():
    jar = Jar(10)
    with pytest.raises(AttributeError):
        jar.size = 5


def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"

    with pytest.raises(ValueError):
        jar.deposit(13)


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(7)
    assert str(jar) == "🍪🍪🍪🍪🍪"

    with pytest.raises(ValueError):
        jar.withdraw(13)


def test_deposit_type_error():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit("five")


def test_withdraw_type_error():
    jar = Jar()
    jar.deposit(5)
    with pytest.raises(ValueError):
        jar.withdraw(2.5)
