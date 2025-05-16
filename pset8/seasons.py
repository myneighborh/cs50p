import sys
from datetime import date, datetime

import inflect


def main():
    birthday = input("Date of Birth: ")
    try:
        birth_date = parse_date(birthday)
    except ValueError:
        sys.exit("Invalid date")

    today = date.today()
    minutes = calculate_minutes(birth_date, today)
    words = convert_to_words(minutes)
    print(f"{words} minutes")


def parse_date(birthday):
    try:
        return datetime.strptime(birthday, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Invalid date")


def calculate_minutes(birthday, today):
    delta = today - birthday
    return delta.days * 24 * 60


def convert_to_words(minutes):
    p = inflect.engine()
    return p.number_to_words(minutes, andword="").capitalize()


if __name__ == "__main__":
    main()
