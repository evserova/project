import csv
from unittest.mock import MagicMock, mock_open, patch


from src.viborka1 import transactions_csv


def test_viborka1_correct_file():
    """
    имитирует успешное чтение CSV-файла и проверяет, что результат соответствует ожидаемому списку словарей.
    :return:
    """
    mock_csv_content = "name;amount;date\nJohn;100;2023-01-01\nJane;150;2023-01-02\n"
    expected_result = [
        {"name": "John", "amount": "100", "date": "2023-01-01"},
        {"name": "Jane", "amount": "150", "date": "2023-01-02"},
    ]

    with patch("builtins.open", mock_open(read_data=mock_csv_content), create=True):
        with patch("csv.DictReader", return_value=csv.DictReader(mock_csv_content.splitlines(), delimiter=";")):
            result = transactions_csv("fake_file.csv")
            assert result == expected_result


def test_viborka1_empty_filename():
    """
    проверяет, что функция возвращает пустой список, если имя файла пустое.
    :return:
    """
    assert transactions_csv("") == []


def test_viborka1_file_not_found():
    """
    проверяет, когда файл не найден, и проверяет, что возвращается пустой список.
    :return:
    """
    with patch("builtins.open", MagicMock(side_effect=FileNotFoundError()), create=True):
        assert transactions_csv("fake_file.csv") == []
