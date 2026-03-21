from typing import Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Generator[dict[str, str], None, None]:
    """Функция, которая принимает на вход список словарей, представляющих транзакции. Возвращает итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)."""

    if not transactions:
        raise ValueError("Список транзакций пуст")
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Generator[None, None, None]:
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции
    по очереди."""

    if not transactions:
        raise ValueError("Список транзакций пуст")
    for transaction in transactions:
        description = transaction.get("description")
        yield description


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999."""

    for n in range(start, stop + 1):
        if 0 < start <= 9999999999999999 and 0 < stop <= 9999999999999999 and start <= stop:
            number = "0" * (16 - len(str(n))) + str(n)
            card_number = number[:4] + " " + number[4:8] + " " + number[8:12] + " " + number[12:]
            yield card_number
        else:
            raise ValueError("Введенные параметры не входят в диапазон")
