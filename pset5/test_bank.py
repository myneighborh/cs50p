from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("  hello there") == 0
    assert value("HELLO!!!") == 0


def test_h():
    assert value("hi") == 20
    assert value("Hey there") == 20
    assert value("h") == 20
    assert value("HOLA amigo") == 20


def test_else():
    assert value("good morning") == 100
    assert value("yo") == 100
    assert value("   what's up") == 100
    assert value("Nice to meet you") == 100


def test_return_type():
    assert isinstance(value("hello"), int)
    assert isinstance(value("hi"), int)
    assert isinstance(value("bye"), int)
