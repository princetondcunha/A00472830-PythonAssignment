import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

apikey = os.getenv("API_KEY")

def fetch_coin_id(symbol):
    url = "https://api.coingecko.com/api/v3/coins/list"
    headers = {"x-cg-demo-api-key": apikey}
    response = requests.get(url, headers=headers)

    for item in response.json():
        if item['name'].lower() == symbol.lower():
            return item['id']
    return None

def fetch_crypto_price(id,days):
    url = f"https://api.coingecko.com/api/v3/coins/{id}/market_chart?vs_currency=cad&days={days}&precision=3"
    headers = {"x-cg-demo-api-key": apikey}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        prices = []
        for price in response.json()['prices']:
            prices.append({'Date': datetime.fromtimestamp(price[0]/1000), 'Price': price[1]})
        df = pd.DataFrame(prices)
        return df
