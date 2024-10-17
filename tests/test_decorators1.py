import pytest
from src.decorators import log


def test_log_different_types_str(capsys):
    # Проверка ошибки: missing 2 required positional arguments: 'x' and 'y'.
    @log(filename="test_log.txt")
    def my_function(x, y):
        return x + y

    try:
        my_function("a", "b")
    except TypeError as e:
        captured = capsys.readouterr()
        assert "my function error: " in captured.out


def test_log_lack_argument(capsys):
    # Проверка ошибки: missing 1 required positional argument: 'y'.
    @log(filename="test_log.txt")
    def my_function(x, y):
        return x + y

    try:
        my_function(1, )
    except TypeError as e:
        captured = capsys.readouterr()
        assert "my function error: " in captured.out


def test_log_different_types_argument(capsys):
    # Проверка ошибки: unsupported operand type(s) for +: 'int' and 'str'.
    @log(filename="test_log.txt")
    def my_function(x, y):
        return x + y

    try:
        my_function(1, "")
    except TypeError as e:
        captured = capsys.readouterr()
        assert "my function error: " in captured.out


def test_log_different_types_no_argument(capsys):
    # Проверка ошибки: missing 2 required positional arguments: 'x' and 'y'.
    @log(filename="test_log.txt")
    def my_function(x, y):
        return x + y

    try:
        my_function()
    except TypeError as e:
        captured = capsys.readouterr()
        assert "my function error: " in captured.out