from datetime import date

import pytest

from seasons import parse_date, calculate_minutes, convert_to_words


def test_valid_date():
    assert parse_date("1990-03-03") == date(1990, 3, 3)


def test_invalid_date():
    with pytest.raises(ValueError):
        parse_date("1990-03-41")
    with pytest.raises(ValueError):
        parse_date("2000/12/11")
    with pytest.raises(ValueError):
        parse_date("2000.12.11")


def test_calculate_minutes():
    assert calculate_minutes(date(2000, 1, 1), date(2000, 1, 2)) == 1440
    assert calculate_minutes(date(2020, 1, 1), date(2020, 1, 1)) == 0
    assert calculate_minutes(date(2020, 1, 1), date(2021, 1, 1)) == 366 * 24 * 60


def test_convert_to_words():
    assert convert_to_words(1440) == "One thousand, four hundred forty"
