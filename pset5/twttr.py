def main():
    text = input("Input: ")
    shorten_text = shorten(text)
    print(f"Output: {shorten_text}")


def shorten(word):
    vowels = "aeiouAEIOU"
    output = []

    for c in word:
        if c not in vowels:
            output.append(c)

    return ''.join(output)


if __name__ == "__main__":
    main()
