from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_or_card_number: str) -> str:
    """Функция, которая принимает на вход номер счета или тип и номер карты, и возвращает маску счета или карты"""

    input_str = str(account_or_card_number).strip()
    if input_str.lower() in ('nan', 'none', 'null', '', 'не указан'):
        return 'Не указан'
    else:
        name_card_or_account = ""
        for letter in input_str:
            if letter.isalpha():
                name_card_or_account += letter
            elif letter == " ":
                name_card_or_account += letter
        if account_or_card_number.startswith("Счет"):
            account_number_user = int(input_str[5:])
            return str(name_card_or_account + get_mask_account(account_number_user))
        else:
            card_number_user = int(input_str[-16:])
            return str(name_card_or_account + get_mask_card_number(card_number_user))


def get_date(long_date: str) -> str:
    """Функция, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024")"""

    if long_date == "":
        raise ValueError("Формат даты не должен быть пустым")
    short_date = long_date[0:10].replace("-", ".")
    date = short_date[-2:] + short_date[4:7] + "." + short_date[0:4]
    return date
