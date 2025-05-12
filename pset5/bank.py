def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def value(greeting):
    greeting = greeting.strip().lower()
    if greeting.startswith("hello"):
        return int(0)
    elif greeting.startswith('h'):
        return int(20)
    else:
        return int(100)


if __name__ == "__main__":
    main()
