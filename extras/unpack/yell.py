def main():
    yell("This", "is", "CS50")


def yell(*args):
    # Map can only be iterated once
    uppercased = map(str.upper, args)
    print(*uppercased)

    # Convert map to a list to make it reusable
    # List comprehension
    uppercased = [word.upper() for word in args]
    print(*uppercased)
    print('/'.join(uppercased))


if __name__ == "__main__":
    main()
