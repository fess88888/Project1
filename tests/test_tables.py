import pytest
import pandas as pd
from unittest.mock import patch, Mock
from src.tables import read_financial_transactions_from_csv, read_financial_transactions_from_excel


@patch('pandas.read_csv')
def test_read_financial_transactions_from_csv_success(mock_read_csv: Mock) -> None:
    """Тест успешного чтения CSV-файла."""
    test_data: pd.DataFrame = pd.DataFrame({
        'id': [1, 2],
        'amount': [100.0, 200.0],
        'date': ['2023-01-01', '2023-01-02']
    })
    mock_read_csv.return_value = test_data
    result = read_financial_transactions_from_csv('test_path.csv')
    assert result[0]['id'] == 1
    assert result[0]['amount'] == 100.0
    assert result[1]['date'] == '2023-01-02'
    mock_read_csv.assert_called_once_with('test_path.csv', delimiter=';')


@patch('pandas.read_csv')
def test_read_financial_transactions_from_csv_file_not_found(mock_read_csv: Mock) -> None:
    """Тест обработки ошибки FileNotFoundError при чтении CSV."""
    mock_read_csv.side_effect = FileNotFoundError('File not found')

    with pytest.raises(FileNotFoundError) as exc_info:
        read_financial_transactions_from_csv('nonexistent_file.csv')
    assert 'Файл не найден' in str(exc_info.value)


@patch('pandas.read_csv')
def test_read_financial_transactions_from_csv_value_error(mock_read_csv: Mock) -> None:
    """Тест обработки ValueError при чтении CSV."""
    mock_read_csv.side_effect = ValueError('Invalid data format')

    with pytest.raises(ValueError) as exc_info:
        read_financial_transactions_from_csv('invalid_data.csv')
    assert 'Проблема с содержимым файла' in str(exc_info.value)


@patch('pandas.read_excel')
def test_read_financial_transactions_from_excel_success(mock_read_excel: Mock) -> None:
    """Тест успешного чтения Excel-файла."""
    test_data: pd.DataFrame = pd.DataFrame({
        'transaction_id': [101, 102],
        'sum': [500.0, 750.0],
        'category': ['Food', 'Transport']
    })
    mock_read_excel.return_value = test_data
    result = read_financial_transactions_from_excel('test_path.xlsx')
    assert result[0]['transaction_id'] == 101
    assert result[1]['sum'] == 750.0
    assert result[0]['category'] == 'Food'
    mock_read_excel.assert_called_once_with('test_path.xlsx')


@patch('pandas.read_excel')
def test_read_financial_transactions_from_excel_file_not_found(mock_read_excel: Mock) -> None:
    """Тест обработки ошибки FileNotFoundError при чтении Excel."""
    mock_read_excel.side_effect = FileNotFoundError('Excel file not found')

    with pytest.raises(FileNotFoundError) as exc_info:
        read_financial_transactions_from_excel('nonexistent.xlsx')
    assert 'Файл не найден' in str(exc_info.value)


@patch('pandas.read_excel')
def test_read_financial_transactions_from_excel_value_error(mock_read_excel: Mock) -> None:
    """Тест обработки ValueError при чтении Excel."""
    mock_read_excel.side_effect = ValueError('Invalid Excel format')

    with pytest.raises(ValueError) as exc_info:
        read_financial_transactions_from_excel('invalid.xlsx')
    assert 'Проблема с содержимым файла' in str(exc_info.value)
