from src.regular_expressions import process_bank_operations, process_bank_search


def test_process_bank_search_found_matches() -> None:
    """Поиск находит совпадения в поле description."""
    data = [
        {'id': 1, 'description': 'Перевод организации ООО "Спектр"'},
        {'id': 2, 'description': 'Оплата услуг интернет'},
        {'id': 3, 'description': 'Перевод организации АО "Вектор"'}
    ]
    result = process_bank_search(data, 'Перевод организации')
    assert len(result) == 2
    assert result[0]['id'] == 1
    assert result[1]['id'] == 3


def test_process_bank_search_no_matches() -> None:
    """Строка поиска не найдена ни в одном описании."""
    data = [
        {'id': 1, 'description': 'Покупка в магазине'},
        {'id': 2, 'description': 'Снятие наличных'}
    ]
    result = process_bank_search(data, 'Перевод организации')
    assert len(result) == 0


def test_process_bank_search_case_insensitive() -> None:
    """Регистронезависимый поиск."""
    data = [
        {'id': 1, 'description': 'перевод организации'},
        {'id': 2, 'description': 'ПЕРЕВОД ОРГАНИЗАЦИИ'},
        {'id': 3, 'description': 'Перевод Организации'}
    ]
    result = process_bank_search(data, 'перевод организации')
    assert len(result) == 3


def test_process_bank_search_empty_data() -> None:
    """Пустая коллекция данных."""
    result = process_bank_search([], 'Перевод организации')
    assert len(result) == 0


def test_process_bank_search_empty_search_string() -> None:
    """Пустая строка поиска."""
    data = [
        {'id': 1, 'description': 'Перевод организации'},
        {'id': 2, 'description': 'Оплата услуг интернет'},
        {'id': 3, 'description': 'Оплата услуг'}
    ]
    result = process_bank_search(data, '')
    assert len(result) == 3
    assert result[0]['id'] == 1
    assert result[1]['id'] == 2
    assert result[2]['id'] == 3


def test_process_bank_operations_basic_counting() -> None:
    """Подсчёт операций по категориям."""
    data = [
        {'id': 1, 'description': 'Покупка в магазине'},
        {'id': 2, 'description': 'Оплата услуг'},
        {'id': 3, 'description': 'Покупка в магазине'},
        {'id': 4, 'description': 'Перевод'},
        {'id': 5, 'description': 'Оплата услуг'},
        {'id': 6, 'description': 'Оплата проезда'}
    ]
    categories = ['Покупка в магазине', 'Оплата услуг', 'Перевод']
    result = process_bank_operations(data, categories)
    assert result == {'Покупка в магазине': 2, 'Оплата услуг': 2, 'Перевод': 1}


def test_process_bank_operations_empty_data() -> None:
    """Пустой список операций."""
    result = process_bank_operations([], ['Покупка', 'Перевод'])
    assert result == {}


def test_process_bank_operations_empty_categories() -> None:
    """Пустой список категорий."""
    data = [
        {'id': 1, 'description': 'Покупка'},
        {'id': 2, 'description': 'Перевод'}
    ]
    result = process_bank_operations(data, [])
    assert result == {}


def test_process_bank_operations_no_matching_categories() -> None:
    """Нет совпадений между описаниями и категориями."""
    data = [
        {'id': 1, 'description': 'Снятие наличных'},
        {'id': 2, 'description': 'Пополнение счёта'}
    ]
    categories = ['Покупка', 'Оплата услуг']
    result = process_bank_operations(data, categories)
    assert result == {}
