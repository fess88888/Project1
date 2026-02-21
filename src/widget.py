from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_or_card_number: str) -> str:
    """Функция, которая принимает на вход номер счета или тип и номер карты, и возвращает маску счета или карты"""

    name_card_or_account = ""
    for letter in account_or_card_number:
        if letter.isalpha():
            name_card_or_account += letter
        elif letter == " ":
            name_card_or_account += letter
    if account_or_card_number.startswith("Счет"):
        account_number = int(account_or_card_number[5:])
        return str(name_card_or_account + get_mask_account(account_number))
    else:
        card_number = int(account_or_card_number[-16:])
        return str(name_card_or_account + get_mask_card_number(card_number))


def get_date(long_date: str) -> str:
    """Функция, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024")"""

    short_date = long_date[0:10].replace("-", ".")
    date = short_date[-2:] + short_date[4:7] + "." + short_date[0:4]
    return date
