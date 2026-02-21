import pytest
from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(mask_card_number: int | str) -> None:
    assert get_mask_card_number(7000792289606361) == mask_card_number


def test_get_short_card_number() -> None:
    """Введен короткий номер"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(123456)
    assert str(exc_info.value) == "Номер карты должен содержать 16 цифр."


def test_get_long_card_number() -> None:
    """Введен длинный номер"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(123456789123456789)
    assert str(exc_info.value) == "Номер карты должен содержать 16 цифр."


def test_get_wrong_card_number() -> None:
    """Введен номер состоящий из цифр, букв и других знаков"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("123a456s789@2222")
    assert str(exc_info.value) == "Номер карты должен содержать только цифры."


def test_get_empty_card_number() -> None:
    """Введен пустой номер"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("")
    assert str(exc_info.value) == "Номер карты должен содержать 16 цифр."


@pytest.mark.parametrize("mask_account, expected", [(12345678912345678912, "**8912"),
                                                    ("5656565656", "**5656"),
                                                    (4444, "**4444")])
def test_get_mask_account(mask_account: int | str, expected: str) -> None:
    assert get_mask_account(mask_account) == expected


def test_get_wrong_account() -> None:
    """Введен номер состоящий из цифр, букв и других знаков"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_account("123c45vsb67#89")
    assert str(exc_info.value) == "Номер счета должен содержать только цифры и не быть пустым"


def test_get_empty_account() -> None:
    """Введен пустой номер"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_account("")
    assert str(exc_info.value) == "Номер счета должен содержать только цифры и не быть пустым"


@pytest.mark.parametrize("incorrect_account, expected", [(123, "**123"),
                                                    ("6", "**6")])
def test_get_incorrect_account(incorrect_account: int | str, expected: str) -> None:
    """Введен короткий номер"""
    assert get_mask_account(incorrect_account) == expected