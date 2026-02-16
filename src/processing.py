def filter_by_state(list_filtered_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция, которая принимает список словарей и опционально значение для ключа state. Возвращает новый список
    словарей, содержащий только те словари, у которых ключ state соответствует указанному значению"""

    new_dict = []
    for filtered_dict in list_filtered_dict:
        if filtered_dict.get("state") == state:
            new_dict.append(filtered_dict)

    return new_dict


def sort_by_date(list_sorted_dict: list[dict], reverse_order: bool = True) -> list[dict]:
    """Функция, которая принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание).
    Возвращает новый список, отсортированный по дате (date)."""

    sorted_dict = sorted(list_sorted_dict, key=lambda x: x['date'], reverse=reverse_order)
    return sorted_dict
