import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "account_card, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ],
)
def test_mask_account_card(account_card: str, expected: str) -> None:
    assert mask_account_card(account_card) == expected


def test_ask_account_card_empty() -> None:
    """Введена пустая строка"""
    with pytest.raises(ValueError) as exc_info:
        mask_account_card("")
    assert str(exc_info.value) == "Номер счета или тип и номер карты не должен быть пустым"


@pytest.mark.parametrize(
    "input_date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2026-02-22T00:00:00.000000", "22.02.2026"),
        ("2025-12-31T23:59:59.999999", "31.12.2025"),
    ],
)
def test_get_date_various_formats(input_date: str, expected: str) -> None:
    assert get_date(input_date) == expected


def test_get_date_empty() -> None:
    """Введена пустая строка"""
    with pytest.raises(ValueError) as exc_info:
        get_date("")
    assert str(exc_info.value) == "Формат даты не должен быть пустым"
