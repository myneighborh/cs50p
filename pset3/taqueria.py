def main():
    total = 0
    while True:
        try:
            item = input("Item: ")
            total += calculate_total(item)
            print(f"Total: ${total:.2f}")
        except EOFError:
            print()
            break
        except KeyError:
            continue


def calculate_total(item):
    menus = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    item = item.title()
    if item in menus:
        price = menus.get(item)
        return price
    else:
        raise KeyError


if __name__ == "__main__":
    main()
