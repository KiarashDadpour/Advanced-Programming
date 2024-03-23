# This Python script fetches the current price of Bitcoin from CoinDesk's API and calculates the value of a given number of Bitcoins in US dollars.

import sys
import requests

api = "https://api.coindesk.com/v1/bpi/currentprice.json"


def main():
    coin_count = float_count()
    print(f"${coin_desk(coin_count):,.4f}")



def float_count():
    try:
        if len(sys.argv) != 2:
            print("Missing command-line argument")
            sys.exit()
        elif not float(sys.argv[1]):
            print("Command-line argument is not a number")
            sys.exit()
        else:
            return float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit()


def coin_desk(coin_count):
    try:
        response = requests.get(api)
        a = response.json()
        b = a["bpi"]["USD"]["rate_float"]
        c = coin_count * b

    except requests.RequestException:
        print("CONNECTION ERROR!")
        sys.exit()

    return c



main()
