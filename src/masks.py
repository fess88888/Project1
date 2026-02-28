def get_mask_account(account_number: int | str) -> str:
    """Функция, которая принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX, где X — это цифра номера."""

    account_number_str = str(account_number)
    if not account_number_str.isdigit():
        raise ValueError("Номер счета должен содержать только цифры и не быть пустым")
    if len(account_number_str) < 4:
        return "**" + account_number_str
    else:
        return "**" + account_number_str[-4:]


def get_mask_card_number(card_number: int | str) -> str:
    """Функция, которая принимает на вход номер карты и возвращает ее маску.
    Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX, где X — это цифра номера."""

    card_number_str = str(card_number)
    if len(card_number_str) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр.")
    elif not card_number_str.isdigit():
        raise ValueError("Номер карты должен содержать только цифры.")
    mask_card_number = card_number_str[0:4] + " " + card_number_str[4:6] + "** **** " + card_number_str[-4:]
    return mask_card_number
