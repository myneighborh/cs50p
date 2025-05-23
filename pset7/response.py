import validators


def main():
    email = input("Email: ").strip()
    if is_valid(email):
        print("Valid")
    else:
        print("Invalid")


def is_valid(email):
    return validators.email(email)


if __name__ == "__main__":
    main()
