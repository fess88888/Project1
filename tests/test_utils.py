import json
from unittest.mock import patch
from src.utils import get_financial_transaction_data, PATH_TO_FILE


def test_valid_json_data() -> None:
    """Тест с корректными данными — список транзакций."""
    mock_transaction_data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]

    with patch('src.utils.json.load', return_value=mock_transaction_data):
        result = get_financial_transaction_data(PATH_TO_FILE)

    assert result == mock_transaction_data


def test_json_contains_not_list() -> None:
    """Тест, когда JSON содержит не список."""
    mock_transaction_data = {"transactions": [{"id": 1}]}

    with patch('src.utils.json.load', return_value=mock_transaction_data):
        result = get_financial_transaction_data(PATH_TO_FILE)

    assert result == []


def test_file_not_found() -> None:
    """Тест для случая, когда файл не найден."""
    with patch('builtins.open', side_effect=FileNotFoundError):
        result = get_financial_transaction_data("nonexistent.json")

    assert result == []


def test_json_decode_error() -> None:
    """Тест для некорректного JSON."""
    with patch('src.utils.json.load', side_effect=json.JSONDecodeError("Expecting value", "", 0)):
        result = get_financial_transaction_data("invalid.json")

    assert result == []


def test_empty_list_in_json() -> None:
    """Тест для JSON с пустым списком."""
    mock_data = []

    with patch('src.utils.json.load', return_value=mock_data):
        result = get_financial_transaction_data("empty.json")

    assert isinstance(result, list)
    assert len(result) == 0
