def main():
    name_list = []

    while True:
        try:
            name = input("Name: ")
            name_list.append(name)
        except EOFError:
            break

    print(bye(name_list))


def bye(name_list):
    if len(name_list) == 1:
        return f"Adieu, adieu, to {name_list[0]}"
    elif len(name_list) == 2:
        return f"Adieu, adieu, to {name_list[0]} and {name_list[1]}"
    else:
        print("Adieu, adieu, to ", end='')
        for name in name_list[:-1]:
            print(f"{name}", end=', ')
        return f"and {name_list[-1]}"


if __name__ == "__main__":
    main()
