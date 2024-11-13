from unittest.mock import patch
import pandas as pd

from src.viborka1 import transactions_xlsx


@patch("pandas.read_excel")
def test_read_trans_xlsx(mock_read_excel):
    """"
    проверяет успешное чтение Excel-файла и проверяет, что результат соответствует ожидаемому списку словарей.
    :param mock_read_excel:
    :return:
    """
    mock_data = [{"transaction_id": 1, "amount": 100}, {"transaction_id": 2, "amount": 200}]
    mock_read_excel.return_value = pd.DataFrame(mock_data)

    result = transactions_xlsx("test_file.xlsx")

    assert result == mock_data


def test_empty_filename():
    """
    проверяет, что функция возвращает пустой список, если имя файла пустое.
    :return:
    """
    result = transactions_xlsx("")
    assert result == []


@patch("pandas.read_excel")
def test_file_not_found(mock_read_excel):
    """
    проверяет, что функция возвращает пустой список, если файл не найден.
    :param mock_read_excel:
    :return:
    """
    mock_read_excel.side_effect = FileNotFoundError
    result = transactions_xlsx("test_file.xlsx")
    assert result == []
