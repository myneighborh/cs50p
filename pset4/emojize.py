import emoji


def main():
    text = input("Input: ").strip()
    emojized_text = emojize(text)
    print(f"Output: {emojized_text}")


def emojize(text):
    return emoji.emojize(text, language='alias')


if __name__ == "__main__":
    main()
