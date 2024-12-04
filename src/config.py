import os
import re
from collections import Counter
from src.config import DATA_DIR
from src.utils import get_transactions_data

list_transactions = get_transactions_data(os.path.join(DATA_DIR, "operations.json"))


def search_transactions(list_txn: list[dict], input_user: str) -> list[dict]:
    """Функция, которая принимает список словарей с данными о банковских операциях
    и строку поиска, а возвращает список словарей, у которых в описании есть данная строка."""
    new_list_transactions = []
    for transactions in list_txn:
        if "description" in transactions and re.search(input_user, transactions["description"], flags=re.IGNORECASE):
            new_list_transactions.append(transactions)
    return new_list_transactions


def list_transactions_sort_description(transactions: list[dict], list_categories: list[str]) -> dict[str, int]:
    """Функция, которая возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории."""
    list_categories_transaction = []
    for transaction in transactions:
        if "description" in transaction and transaction["description"] in list_categories:
            list_categories_transaction.append(transaction["description"])
    sort_transaction = Counter(list_categories_transaction)
    return dict(sort_transaction)


if __name__ == "__main__":
    categories_operations = [
        "Перевод организации",
        "Перевод с карты на карту",
        "Перевод с карты на счет",
        "Перевод со счета на счет",
        "Открытие вклада",
    ]

    print(list_transactions_sort_description(list_transactions, categories_operations))

    input_user = input("Введите слово для поиска: ")
    print(search_transactions(list_transactions, input_user))
