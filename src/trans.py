import re
from collections import Counter


def trans_search(transactions, string_search, transaction=None):
    """"
    принимает список словарей с данными о банковских операциях и строку поиска, а возвращает список словарей,
    у которых в описании есть данная строка
    :param transaction:
    :param transactions:
    :param string_search:
    :return:
    """
    list_result = []
    pattern = re.compile(re.escape(string_search), re.I)

    for transaction in transactions:
        description = transaction.get('description')
        if isinstance(description, str) and re.search(pattern, description):
            list_result.append(transactions)

    return list_result


def count_trans(list_trans, list_category):
    """
    принимает список словарей с данными о банковских операциях и список категорий операций, а возвращает словарь,
    в котором ключи — это названия категорий, а значения — это количество операций в каждой категории.
    :param list_trans:
    :param list_category:
    :return:
    """

    count_operation = Counter()

    for transaction in list_trans:
        description = transaction['description']

        for category in list_category:
            if category.lower() in description.lower():
                count_operation[category] += 1
                break

    return count_operation
