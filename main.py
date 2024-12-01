from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.viborka1 import transactions_csv, transactions_xlsx
from src.trans import trans_search
from src.utils import get_transactions_info_json
from src.widget import get_date, mask_account_card
from source import path_data, path_csv, path_xlsx


def get_file_selection():
    print(
        """Привет! Добро пожаловать в программу работы
с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
    )
    global user_input_file

    user_input_file = input("Введите число от 1 до 3 включительно:\n")

    if user_input_file == "1":
        print("Для обработки выбран JSON-файл.\n")
        file_use = get_transactions_info_json(path_data)
        return file_use
    elif user_input_file == "2":
        print("Для обработки выбран CSV-файл.\n")
        file_use = transactions_csv(path_csv)
        return file_use
    elif user_input_file == "3":
        print("Для обработки выбран XLSX-файл.\n")
        file_use = transactions_xlsx(path_xlsx)
        return file_use
    else:
        return "Введен некорректный номер"


def entering_the_status(file):
    while True:
        print(
            """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
"""
        )

        user_input_status = input("Введите доступный статус:\n").upper()

        if user_input_status in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f"Операции отфильтрованы по статусу {user_input_status}")

            res_status = filter_by_state(file, user_input_status)
            break
        else:
            print(f"Статус операции {user_input_status} недоступен.")

    return res_status


def sort_trans_date(file_list):
    print("Отсортировать операции по дате? Да/Нет")

    user_input_date = input("Ввод:\n").upper()

    if user_input_date == "ДА":
        print("Отсортировать по возрастанию или по убыванию?")
        user_input_sort = input("Ввод:\n").lower()
        if user_input_sort == "по возрастанию":
            is_revers = False
            data = sort_by_date(file_list, is_revers)
            return data
        elif user_input_sort == "по убыванию":
            is_revers = True
            data = sort_by_date(file_list, is_revers)
            return data

    elif user_input_date == "НЕТ":
        s = file_list
        return s
    else:
        return "Некорректный ввод!"


def rub_transactions(transactions):
    print("Выводить только рублевые транзакции? Да/Нет")
    input_user_currency = input("Ввод:\n").upper()
    if user_input_file == "1":
        if input_user_currency == "ДА":
            data = filter_by_currency(transactions, "RUB")
            return list(data)
        elif input_user_currency == "НЕТ":
            data = transactions
            return data
        else:
            return "Некорректный ввод!"
    elif user_input_file == "2" or user_input_file == "3":
        if input_user_currency == "ДА":
            print("DEBUG",
                  transactions)
            data = filter_by_currency(transactions, "RUB")
            return list(data)
        elif input_user_currency == "НЕТ":
            data = transactions
            return data
        else:
            return "Некорректный ввод!"


def filter_search_word(file_list):
    print(
        """Отфильтровать список транзакций по определенному слову
в описании? Да/Нет"""
    )

    user_input_search = input("Ввод:\n").upper()
    if user_input_search == "ДА":
        print("Введите слово:")
        string_to_search = input()
        data = trans_search(file_list, string_to_search)
        return data
    elif user_input_search == "НЕТ":
        return file_list
    else:
        return "Некорректный ввод!"


def result(file_list: list):
    if len(list(file_list)) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(file_list)}\n")

    for transactions in file_list:
        for transaction in transactions:
            date = get_date(transaction.get("date"))

            try:
               if type(transaction["from"])==str:
                mask_from = mask_account_card(transaction["from"])
                print(f"{date} {transaction['description']} {str(mask_from)} -> ", end="")
            except KeyError:
                print(f"{date} {transaction['description']} ", end="")
            except AttributeError:
                print(f"{date} {transaction['description']} ", end="")

            mask_to = mask_account_card(transaction["to"])
            try:
                amount = transaction["amount"]
            except KeyError:
                amount = transaction["operationAmount"]["amount"]
            try:
                currency = transaction["currency_name"]
            except KeyError:
                currency = transaction["operationAmount"]["currency"]["name"]
            print(f"{mask_to} Сумма: {amount} {currency}")


def main():
    file_selection = get_file_selection()
    status = entering_the_status(file_selection)
    date = sort_trans_date(status)
    transaction = rub_transactions(date)
    data = filter_search_word(transaction)
    result(data)


if __name__ == "__main__":
    main()
    