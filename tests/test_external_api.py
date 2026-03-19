import pytest
import requests
from unittest.mock import patch, Mock
from src.external_api import converting_currency, API_KEY


def test_valid_converting_currency_rub() -> None:
    """Тест с валютой RUB — возвращается сумма без конвертации."""
    transaction = {
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {"code": "RUB"}
        }
    }
    assert converting_currency(transaction) == 31957.58


def test_valid_converting_currency_other() -> None:
    """Тест для успешной конвертации других валют."""
    transaction = {
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {"code": "USD"}
        }
    }
    with patch('requests.get') as mock_get:
        mock_response = Mock()
        mock_response.json.return_value = {"result": 520543.42}
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        result = converting_currency(transaction)
        assert result == 520543.42


def test_invalid_amount_format() -> None:
    """Тест, amount не число"""
    transaction = {
        "operationAmount": {
            "amount": "not_a_number",
            "currency": {"code": "USD"}
        }
    }
    with pytest.raises(ValueError, match="Invalid amount format"):
        converting_currency(transaction)


def test_missing_amount() -> None:
    """Тест, когда отсутствует amount"""
    transaction = {
        "operationAmount": {
            "currency": {"code": "USD"}
        }
    }
    with pytest.raises(ValueError, match="'amount' is missing"):
        converting_currency(transaction)


def test_missing_currency_code() -> None:
    """Тест, когда отсутствует код валюты"""
    transaction = {
        "operationAmount": {
            "amount": "100"
        }
    }
    with pytest.raises(ValueError, match="Currency code is missing"):
        converting_currency(transaction)


def test_api_request_format() -> None:
    """Тест для проверки корректности формирования URL для API."""
    transaction = {
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {"code": "USD"}
        }
    }
    with patch('requests.get') as mock_get:
        converting_currency(transaction)
        url = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=31957.58&date=2019-08-26"
        mock_get.assert_called_once_with(url, headers={"apikey": API_KEY})


def test_api_connection_error() -> None:
    """Тест для ошибки соединения."""
    transaction = {
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {"code": "USD"}
        }
    }
    with patch('requests.get') as mock_get:
        mock_get.side_effect = requests.exceptions.ConnectionError("Connection failed")
        result = converting_currency(transaction)
        assert result == 0.0


def test_http_error_404() -> None:
    """Тест для HTTP ошибки"""
    transaction = {
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {"code": "USD"}
        }
    }
    with patch('requests.get') as mock_get:
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")
        mock_get.return_value = mock_response
        result = converting_currency(transaction)
        assert result == 0.0
