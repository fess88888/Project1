import os

import requests
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

API_KEY = os.getenv("API_KEY")


def converting_currency(transaction: dict) -> float:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют
    и конвертации суммы операции в рубли."""

    amount = transaction.get("operationAmount", {}).get("amount")
    currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")
    if not amount:
        raise ValueError("Field 'amount' is missing in transaction")
    if not currency:
        raise ValueError("Currency code is missing in transaction")

    try:
        amount = float(amount)
    except ValueError:
        raise ValueError(f"Invalid amount format: {amount}")

    if currency == "RUB":
        return float(amount)
    else:
        date = transaction.get("date")[:10]
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}&date={date}"
        headers = {"apikey": API_KEY}
        try:
            exchange_rate = requests.get(url, headers=headers)
            exchange_rate.raise_for_status()
            result = exchange_rate.json().get("result")
            return round(float(result), 2)
        except requests.exceptions.RequestException as err:
            print(f"An error occurred: {err}.")
            return 0.0
