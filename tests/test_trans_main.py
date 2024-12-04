import pytest
from collections import Counter
from src.trans import count_trans  # Замените `your_module` на имя вашего файла с функцией


@pytest.fixture
def sample_data():
    '''
    фикстура, которая возвращает пример данных для использования в тестах.
    :return:
    '''
    list_trans = [
        {'description': 'Grocery store payment'},
        {'description': 'Online subscription payment'},
        {'description': 'Grocery store payment'},
        {'description': 'Salary deposit'},
        {'description': 'payment for utilities'},
        {'description': 'Dining out payment'}
    ]

    list_category = ['Grocery', 'Subscription', 'Utilities', 'Dining', 'Salary']

    return list_trans, list_category


def test_trans(sample_data):

    '''
    проверяет, правильно ли функция count_trans считает транзакции по категориям.
    :param sample_data:
    :return:
    '''
    list_trans, list_category = sample_data

    expected_output = Counter({
        'Grocery': 2,
        'Subscription': 1,
        'Utilities': 1,
        'Dining': 1,
        'Salary': 1
    })

    output = count_trans(list_trans, list_category)

    assert output == expected_output, f"Expected {expected_output}, but got {output}"


def test_trans_empty():
    '''
    проверяет, как функция ведет себя при пустых входных списках транзакций и категорий.
    :return:
    '''
    list_trans = []
    list_category = []

    expected_output = Counter()

    output = count_trans(list_trans, list_category)

    assert output == expected_output, f"Expected {expected_output}, but got {output}"
