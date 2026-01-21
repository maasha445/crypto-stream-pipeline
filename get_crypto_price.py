import requests
import pandas as pd
from datetime import datetime

coins = ["bitcoin", "ethereum", "solana", "ripple", "dogecoin"]

url = "https://api.coingecko.com/api/v3/simple/price"

params = {
    "ids": ",".join(coins),
    "vs_currencies": "usd"
}

response = requests.get(url, params=params)
data = response.json()

rows = []

for coin in coins:
    rows.append({
        "timestamp": datetime.now(),
        "coin": coin,
        "price_usd": data[coin]["usd"]
    })

df = pd.DataFrame(rows)
df.to_csv("crypto_prices.csv", index=False)

print("Saved crypto_prices.csv")
