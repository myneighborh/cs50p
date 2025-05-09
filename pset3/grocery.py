def main():
    grocery_list = {}
    while True:
        try:
            grocery = input().upper()
            grocery_list = update_count(grocery_list, grocery)
        except EOFError:
            print()
            break

    for key in sorted(grocery_list):
        print(f"{grocery_list[key]} {key}")


def update_count(grocery_list, item):
    if item in grocery_list:
        grocery_list[item] += 1
    else:
        grocery_list[item] = 1
    return grocery_list


if __name__ == "__main__":
    main()
