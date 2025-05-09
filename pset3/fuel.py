def main():
    numerator, denominator = get_input()
    percentage = convert(numerator, denominator)

    if percentage >= 99:
        print('F')
    elif percentage <= 1:
        print('E')
    else:
        print(f"{percentage}%")


def get_input():
    while True:
        try:
            fraction = input("Fraction: ")
            numerator, denominator = map(int, fraction.split('/'))
            if denominator == 0:
                raise ZeroDivisionError
            if numerator > denominator:
                raise ValueError
            return numerator, denominator
        except (ValueError, ZeroDivisionError):
            continue


def convert(numerator, denominator):
    percentage = round(numerator / denominator * 100)
    return percentage


if __name__ == "__main__":
    main()
