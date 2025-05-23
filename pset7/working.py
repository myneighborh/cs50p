import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        sys.exit("ValueError")


def convert(s):
    match = re.search(r"^(?P<start_hour>[1]?[0-9])(:(?P<start_min>[0-5][0-9]))? (?P<start>AM|PM) to (?P<end_hour>[1]?[0-9])(:(?P<end_min>[0-5][0-9]))? (?P<end>PM|AM)$", s)
    if not match:
        raise ValueError

    start_ampm = match.group("start")
    start_hour = int(match.group("start_hour"))
    start_min = match.group("start_min")

    if start_hour > 12:
        raise ValueError

    if start_ampm == "AM":
        if start_hour == 12:
            start_hour = 0
    else:
        if start_hour != 12:
            start_hour += 12
    start_min = start_min if start_min else "00"

    end_ampm = match.group("end")
    end_hour = int(match.group("end_hour"))
    end_min = match.group("end_min")

    if end_hour > 12:
        raise ValueError

    if end_ampm == "AM":
        if end_hour == 12:
            end_hour = 0
    else:
        if end_hour != 12:
            end_hour += 12
    end_min = end_min if end_min else "00"

    return f"{start_hour:02}:{start_min} to {end_hour:02}:{end_min}"


if __name__ == "__main__":
    main()
