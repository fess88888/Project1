import logging
import os

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "masks.log"), "w", encoding="utf-8"
)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_account(account_number: int | str) -> str:
    """Функция, которая принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX, где X — это цифра номера."""

    logger.info("Принимаем номер счета.")
    account_number_str = str(account_number)
    logger.info("Проверяем, что номер счета содержит только цифры и не пустой.")
    if not account_number:
        logger.error(f"Номер счёта пуст. Получено: '{account_number}'")
        raise ValueError("Номер счёта должен содержать только цифры и не быть пустым")
    elif not account_number_str.isdigit():
        logger.error(f"Номер счёта содержит недопустимые символы. Получено: '{account_number}'")
        raise ValueError("Номер счёта должен содержать только цифры и не быть пустым")
    logger.info("Получаем маску счета.")
    if len(account_number_str) < 4:
        mask_account = "**" + account_number_str
        logger.info(f"Получаем маску счета: {mask_account}")
        return mask_account
    else:
        mask_account = "**" + account_number_str[-4:]
        logger.info(f"Получаем маску счета: {mask_account}")
        return mask_account


def get_mask_card_number(card_number: int | str) -> str:
    """Функция, которая принимает на вход номер карты и возвращает ее маску.
    Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX, где X — это цифра номера."""

    logger.info("Принимаем номер карты.")
    card_number_str = str(card_number)
    logger.info("Проверяем, что номер карты содержит только цифры и их шестнадцать.")
    if len(card_number_str) != 16:
        logger.error("Номер карты не содержит шестнадцать цифр. Получено: '{card_number}'")
        return 'Не указан'
    elif not card_number_str.isdigit():
        logger.error(f"Номер карты должен содержать только цифры. Получено: '{card_number}'")
        return 'Не указан'
    else:
        mask_card_number = card_number_str[0:4] + " " + card_number_str[4:6] + "** **** " + card_number_str[-4:]
        logger.info(f"Получаем маску карты: {mask_card_number}")
        return mask_card_number


if __name__ == "__main__":
    mask_user_account = get_mask_account(73654108430135874305)
    mask_user_card_number = get_mask_card_number(7000792289606361)
    print(mask_user_account)
    print(mask_user_card_number)
