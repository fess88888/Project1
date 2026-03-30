import json
import logging
import os

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "utils.log"), "w", encoding="utf-8"
)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")


def get_financial_transaction_data(path: str) -> list[dict]:
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""

    try:
        logger.info(f"Открываем для чтения JSON файл по указанному пути {path}.")
        with open(path, "r", encoding="utf-8") as transaction_file:
            logger.info("Преобразуем данные из файла в формате JSON в Python объект.")
            transaction_data = json.load(transaction_file)
            logger.info("Проверяем является ли Python объект списком.")
            if isinstance(transaction_data, list):
                logger.info(f"Python объект список. Возвращаем {transaction_data}")
                return transaction_data
            else:
                logger.info("Python объект не список. Возвращаем пустой список")
                return []
    except (FileNotFoundError, json.JSONDecodeError) as ex:
        logger.error(f"Произошла ошибка: {ex}")
        pass
    return []


if __name__ == "__main__":
    print(get_financial_transaction_data(PATH_TO_FILE)[:4])
