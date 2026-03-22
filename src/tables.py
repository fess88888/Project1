import pandas as pd
import os
import csv
from typing import List, Dict, Any, Hashable


PATH_TO_FILE_CSV = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions.csv")
PATH_TO_FILE_EXCEL = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions_excel.xlsx")


def read_financial_transactions_from_csv(path: str) -> List[Dict[Hashable, Any]]:
    """Функция, которая принимает на вход путь до CSV-файла, считывает из него финансовые операции и
    выдает список словарей с транзакциями."""

    try:
        transactions_csv = pd.read_csv(path, delimiter=delimiter)
        transactions_csv_list = transactions_csv.to_dict(orient='records')
        return transactions_csv_list
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден: {path}")
    except csv.Error as e:
        raise csv.Error(f"Ошибка при чтении CSV‑файла: {e}")
    except ValueError as e:
        raise ValueError(f"Проблема с содержимым файла: {e}")


def read_financial_transactions_from_excel(path: str) -> List[Dict[Hashable, Any]]:
    """Функция, которая принимает на вход путь до Excel-файла, считывает из него финансовые операции и
    выдает список словарей с транзакциями."""

    try:
        transactions_excel = pd.read_excel(path)
        transactions_excel_list = transactions_excel.to_dict(orient='records')
        return transactions_excel_list
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден: {path}")
    except ValueError as e:
        raise ValueError(f"Проблема с содержимым файла: {e}")


if __name__ == '__main__':
    delimiter = ';'
    tr_csv = read_financial_transactions_from_csv(PATH_TO_FILE_CSV)
    print(tr_csv[: 3])
    tr_excel = read_financial_transactions_from_excel(PATH_TO_FILE_EXCEL)
    print(tr_excel[: 3])
