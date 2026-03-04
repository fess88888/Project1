import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 4, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003", "0000 0000 0000 0004"]),
        (7777777777777777, 7777777777777778, ["7777 7777 7777 7777", "7777 7777 7777 7778"]),
        (4444, 4444, ["0000 0000 0000 4444"]),
    ],
)
def test_card_number_generator(start: int, stop: int, expected: str) -> None:
    result = list(card_number_generator(start, stop))
    assert result == expected


def test_card_number_generator_incorrect_range() -> None:
    with pytest.raises(ValueError) as exc_info:
        list(card_number_generator(2, 222222222222222222222222222))
    assert str(exc_info.value) == "Введенные параметры не входят в диапазон"


def test_filter_by_currency(transactions_: list[dict]) -> None:
    result = list(filter_by_currency(transactions_, "USD"))
    assert result == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]
    result = list(filter_by_currency(transactions_, "EUD"))
    assert result == []
    result = list(filter_by_currency(transactions_, "RUB"))
    assert result == [
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


def test_filter_by_currency_empty(transactions_: list[dict]) -> None:
    with pytest.raises(ValueError) as exc_info:
        list(filter_by_currency([], "EUD"))
    assert str(exc_info.value) == "Список транзакций пуст"


def test_transaction_descriptions_empty(transactions_: list[dict]) -> None:
    with pytest.raises(ValueError) as exc_info:
        list(transaction_descriptions([]))
    assert str(exc_info.value) == "Список транзакций пуст"


def test_transaction_descriptions(transactions_: list[dict]) -> None:
    result = list(transaction_descriptions(transactions_))
    assert result == [
        "Перевод организации", "Перевод со счета на счет", "Перевод со счета на счет",
        "Перевод с карты на карту", "Перевод организации"
    ]
