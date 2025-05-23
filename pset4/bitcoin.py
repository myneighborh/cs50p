import requests
import sys


API_KEY = "YOUR_API_KEY"


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        coins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    price = get_bitcoin_price()
    print(f"${bitcoin_to_dollar(coins, price):,.4f}")


def get_bitcoin_price():
    url = "https://rest.coincap.io/v3/assets/bitcoin"
    headers = {
        "Authorization":f"Bearer {API_KEY}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return float(data["data"]["priceUsd"])
    except (requests.RequestException, KeyError, ValueError):
        sys.exit()


def bitcoin_to_dollar(coins, price):
    return coins * price


if __name__ == "__main__":
    main()
