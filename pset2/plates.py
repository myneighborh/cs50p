def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    length = len(s)

    if length < 2 or length > 6:
        return False

    if not s[:2].isalpha():
        return False

    for i in range(length):
        if s[i].isdigit():
            if s[i] == '0':
                return False
            if any(c.isalpha() for c in s[i+1:]):
                return False
            break

    if not s.isalnum():
        return False

    return True


if __name__ == "__main__":
    main()
