def main():
    amount_due = 50
    while amount_due > 0:
        try:
            coin = int(input("Insert Coin: "))
            amount_due = calculate_amount_due(amount_due, coin)
            if amount_due > 0:
                print(f"Amount Due: {amount_due}")
        except ValueError:
            continue

    print(f"Change Owed: {abs(amount_due)}")


def calculate_amount_due(amount_due, coin):
    if coin in [25, 10, 5]:
        amount_due -= coin
    return amount_due


if __name__ == "__main__":
    main()

