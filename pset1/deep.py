def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    answer = answer.strip().lower()
    print(is_true(answer))


def is_true(t):
    if t == "42" or t == "forty two" or t == "forty-two":
        return "Yes"
    else:
        return "No"


if __name__ == "__main__":
    main()
