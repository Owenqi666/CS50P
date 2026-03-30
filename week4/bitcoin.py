import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    API_KEY = "679507a906b04d43ce82b38a93252ec3e80a689714f14d4ea9cecf9dc84e9d3f"
    response = requests.get(f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}")
    data = response.json()
    price = float(data["data"]["priceUsd"])
except requests.RequestException:
    sys.exit("Could not retrieve data")

print(f"${price * n:,.4f}")