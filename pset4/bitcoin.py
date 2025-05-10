import requests
import sys


API_KEY = "YOUR_API_KEY"


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoin = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    price = get_bitcoin_price()
    if price is not None:
        dollar = bitcoin * price
        print(f"${dollar:,.4f}")


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


if __name__ == "__main__":
    main()
