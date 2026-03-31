from typing import Any

from src.widget import mask_account_card, get_date
from src.utils import get_financial_transaction_data
from src.tables import read_financial_transactions_from_csv, read_financial_transactions_from_excel
from src.regular_expressions import process_bank_search
from src.processing import filter_by_state, sort_by_date


def get_transaction_currency(transaction: dict) -> str | Any:
    """Универсальная функция для получения валюты транзакции."""
    if "operationAmount" in transaction and "currency" in transaction["operationAmount"]:
        return transaction["operationAmount"]["currency"].get("code", "")
    return transaction.get("currency_code", "")


def main():
    transactions_ = []
    operations_sort_state = []
    operations_sort_data = []
    transactions_rubles = []
    filtered_transactions = []

    while True:
        print("\nПривет!\nДобро пожаловать в программу работы с банковскими транзакциями.\n")
        print(
            "Выберите необходимый пункт меню:\n"
            "1. Получить информацию о транзакциях из JSON-файла\n"
            "2. Получить информацию о транзакциях из CSV-файла\n"
            "3. Получить информацию о транзакциях из XLSX-файла:"
        )
        users_choice = (input("\nВаш выбор: ")).strip()
        if users_choice == '1':
            print("Для обработки выбран JSON-файл.")
            file_path = 'data/operations.json'
            transactions_ = get_financial_transaction_data(file_path)
            break
        elif users_choice == '2':
            print("Для обработки выбран CSV-файл.")
            path_csv = 'data/transactions.csv'
            transactions_ = read_financial_transactions_from_csv(path_csv)
            break
        elif users_choice == '3':
            print("Для обработки выбран XLSX-файл.")
            path_excel = 'data/transactions_excel.xlsx'
            transactions_ = read_financial_transactions_from_excel(path_excel)
            break
        else:
            print("\nНеверный выбор. Выберите 1,2 или 3")
            continue

    while True:
        print("\nВведите статус, по которому необходимо выполнить фильтрацию.\n"
              "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        status = ['EXECUTED', 'CANCELED', 'PENDING']
        user_status = (input("\nВаш выбор: ")).strip().upper()
        if user_status in status:
            status_filter = user_status
            print(f"Был выбран статус: {status_filter}")
            operations_sort_state = filter_by_state(transactions_, status_filter)
            break
        else:
            print(f'Статус операции "{user_status}" недоступен')
            continue

    while True:
        sort_by_date_choice = input("Отсортировать операции по дате? Да/Нет\n").strip().lower()
        if sort_by_date_choice in ['да', 'нет']:
            if sort_by_date_choice == 'да':
                while True:
                    order_choice = input(
                        'Отсортировать по возрастанию или по убыванию?\n'
                        'Введите "по возрастанию" или "по убыванию"\n').strip().lower()
                    if order_choice == 'по возрастанию':
                        order_filter = False
                        operations_sort_data = sort_by_date(operations_sort_state, order_filter)
                        break
                    elif order_choice == 'по убыванию':
                        order_filter = True
                        operations_sort_data = sort_by_date(operations_sort_state, order_filter)
                        break
                    else:
                        print(f'Ввод "{order_choice}" некорректен. Пожалуйста, попробуйте снова.')
            else:
                operations_sort_data = operations_sort_state
            break
        else:
            print(f'Ввод "{sort_by_date_choice}" некорректен. Наберите Да или Нет.')
            continue

    while True:
        rub_filter = input("Выводить только рублёвые транзакции? Да/Нет\n").strip().lower()
        if rub_filter == 'да':
            filter_currency = 'RUB'
            transactions_rubles = [transaction for transaction in operations_sort_data if
                                   get_transaction_currency(transaction) == filter_currency]
            break
        elif rub_filter == 'нет':
            transactions_rubles = operations_sort_data
            print("Фильтрация по валюте пропущена. Использованы все транзакции.")
            break
        else:
            print('Ввод некорректен. Введите "да" или "нет".')
            continue

    while True:
        word_filter = input(
            "Отфильтровать список транзакций по определённому слову в описании? Да/Нет\n").strip().lower()
        if word_filter == 'да':
            categories = ['Открытие вклада', 'Перевод с карты на карту', 'Перевод организации',
                          'Перевод со счета на счет']
            search_word = input(f"Введите слово для фильтрации транзакций по описанию {categories}: ").strip()
            filtered_transactions = process_bank_search(transactions_rubles, search_word)
            print(f"После фильтрации по слову '{search_word}' осталось {len(filtered_transactions)} транзакций.")
            break
        elif word_filter == 'нет':
            filtered_transactions = transactions_rubles
            break
        else:
            print('Ввод некорректен. Введите "да" или "нет".')
            continue

    print('\nРаспечатываю итоговый список транзакций...')
    print(f'\nВсего банковских операций в выборке: {len(filtered_transactions)}\n')
    if len(filtered_transactions) != 0:
        for transaction in filtered_transactions:
            if 'operationAmount' in transaction:
                amount = transaction.get('operationAmount').get('amount', 'Нет суммы')
                currency = transaction.get('operationAmount').get('currency').get('code')
            else:
                amount = transaction.get('amount', 'Нет суммы')
                currency = transaction.get('currency_code', 'Нет валюты')
            date = transaction.get('date', 'Дата не указана')
            correct_date = get_date(date)
            description = transaction.get('description', 'Описание отсутствует')
            from_account = mask_account_card(transaction.get('from', 'Не указан'))
            to_account = mask_account_card(transaction.get('to', 'Не указан'))
            print(f"{correct_date} {description}")
            print(f"{from_account} -> {to_account}")
            print(f"Сумма: {amount} {currency}")
            print()
    else:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == '__main__':
    main()
