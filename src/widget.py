import masks

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
        return name_card_or_account + masks.get_mask_account(account_number)
    else:
        card_number = int(account_or_card_number[-16:])
        return name_card_or_account + masks.get_mask_card_number(card_number)

