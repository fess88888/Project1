def filter_by_state(list_filtered_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция, которая принимает список словарей и опционально значение для ключа state. Возвращает новый список
    словарей, содержащий только те словари, у которых ключ state соответствует указанному значению"""

    new_dict = []
    for filtered_dict in list_filtered_dict:
        if filtered_dict.get("state") == state:
            new_dict.append(filtered_dict)

    return new_dict
