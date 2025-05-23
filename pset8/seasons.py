import sys
from datetime import date, datetime

import inflect


def main():
    birthday = input("Date of Birth: ")
    today = date.today()

    try:
        birth_date = parse_date(birthday, today)
    except ValueError as e:
        sys.exit(e)

    minutes = calculate_minutes(birth_date, today)
    words = convert_to_words(minutes)
    print(f"{words} minutes")


def parse_date(birthday, today):
    try:
        birth_date = datetime.strptime(birthday, "%Y-%m-%d").date()
        if birth_date > today:
            raise ValueError("Date must be in the past")
        return birth_date
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
