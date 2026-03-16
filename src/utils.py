import json


PATH_TO_FILE = r"C:\Users\fess8\PycharmProjects\MyProject_1\data\operations.json"


def get_financial_transaction_data(path: str) -> list[dict]:
    """ Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей
     с данными о финансовых транзакциях.
     Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""

    try:
        with open(path, 'r', encoding='utf-8') as transaction_file:
            transaction_data = json.load(transaction_file)
            if isinstance(transaction_data, list):
                return transaction_data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return []
