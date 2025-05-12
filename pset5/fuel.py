def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            continue


def convert(fraction):
    numerator, denominator = map(int, fraction.split('/'))
    if denominator == 0:
        raise ZeroDivisionError
    if numerator > denominator:
        raise ValueError

    percentage = round(numerator / denominator * 100)

    return percentage


def gauge(percentage):
    if percentage >= 99:
        return 'F'
    elif percentage <= 1:
        return 'E'
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
