import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_transaction_sum(transaction: dict) -> float:
    code = transaction["operationAmount"]["currency"]["code"]
    amount_fiat = transaction["operationAmount"]["amount"]
    if code == "RUB":
        return amount_fiat
    if code == "USD" or code == "EUR":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount_fiat}"
        token_exchange = os.getenv("API_KEY_exchange")
        headers = {"apikey": token_exchange}
        response = requests.request("GET", url, headers=headers)
        result = dict(response.json())
        return float(result["result"])
