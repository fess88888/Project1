import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска,
    возвращает список словарей, у которых в описании есть данная строка."""

    return [transaction for transaction in data if
            re.search(search, transaction.get('description', ''), flags=re.IGNORECASE)]


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция, принимает список словарей с данными о банковских операциях и список категорий операций,
    возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории."""

    descriptions = [transaction.get('description', '') for transaction in data]
    filtered_descriptions = [description for description in descriptions if description in categories]
    return dict(Counter(filtered_descriptions))
