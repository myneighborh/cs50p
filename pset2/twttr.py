def main():
    input_text = input("Input: ")
    output_text = convert(input_text)
    print(f"Output: {output_text}")


def convert(text):
    vowels = "aeiouAEIOU"
    output = []

    for t in text:
        if t not in vowels:
            output.append(t)

    return ''.join(output)


if __name__ == "__main__":
    main()
