from plates import is_valid


def test_valid_plates():
    assert is_valid("CS50") == True
    assert is_valid("CS123") == True
    assert is_valid("AB1234") == True
    assert is_valid("XY9") == True
    assert is_valid("ECTO88") == True
    assert is_valid("NRVOUS") == True


def test_invalid_too_short_or_long():
    assert is_valid("C") == False
    assert is_valid("H") == False
    assert is_valid("ABCDEFG") == False
    assert is_valid("OUTATIME") == False


def test_invalid_starting_characters():
    assert is_valid("1ABC") == False
    assert is_valid("9ZXY") == False
    assert is_valid("@CS50") == False
    assert is_valid(" A123") == False
    assert is_valid("50") == False
    assert is_valid("A1BC") == False


def test_invalid_zero_start():
    assert is_valid("CS05") == False


def test_invalid_letter_after_number():
    assert is_valid("CS50A") == False
    assert is_valid("CS50P2") == False


def test_invalid_symbols_or_whitespace():
    assert is_valid("CS!50") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS-50") == False
    assert is_valid("PI3.14") == False
