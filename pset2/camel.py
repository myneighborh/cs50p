def main():
    camel_case = input("camelCase: ")
    snake_case = convert_to_snake(camel_case)
    print(f"snake_case: {snake_case}")


def convert_to_snake(camel):
    result = []

    for char in camel:
        if char.isupper():
            result.append('_')
            result.append(char.lower())
        else:
            result.append(char)

    return ''.join(result)


if __name__ == "__main__":
    main()
