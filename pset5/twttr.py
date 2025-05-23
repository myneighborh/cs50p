def main():
    text = input("Input: ")
    print(f"Output: {shorten(text)}")


def shorten(text):
    vowels = "aeiouAEIOU"
    output = []

    for c in text:
        if c not in vowels:
            output.append(c)

    return ''.join(output)


if __name__ == "__main__":
    main()
