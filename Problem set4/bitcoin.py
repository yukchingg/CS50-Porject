import requests
import sys

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()
    current_price = data["bpi"]["EUR"]["rate_float"]
except requests.RequestException:
    sys.exit()

try:
    n = float(sys.argv[1])
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")

output = n * current_price
print(f"{output:,.4f}")