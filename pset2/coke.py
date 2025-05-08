def main():
    amount_due = calculate()
    print(f"Change Owed: {amount_due}")


def calculate():
    amount_due = 50

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        try:
            coin = int(input("Insert Coin: "))
        except ValueError:
            continue

        if coin in [25, 10, 5]:
            amount_due -= coin

    return abs(amount_due)


if __name__ == "__main__":
    main()

