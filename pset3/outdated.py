def main():
    month, day, year = convert_to_iso()
    print(f"{year}-{month:02}-{day:02}")


def convert_to_iso():
    month_list = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        try:
            date = input("Date: ").strip()

            if '/' in date:
                month, day, year = map(int, date.split('/'))
            elif ',' in date:
                parts = date.split()
                if len(parts) != 3:
                    raise ValueError
                month_str = parts[0]
                month = month_list.index(month_str.capitalize()) + 1
                day = int(parts[1].strip(','))
                year = int(parts[2])
            else:
                raise ValueError

            if 1 <= month <= 12 and 1 <= day <= 31:
                return month, day, year

        except (ValueError, IndexError):
            continue


if __name__ == "__main__":
    main()
