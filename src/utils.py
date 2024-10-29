import json
import logging
import sys
from pathlib import Path
from typing import List

sys.path.append(str(Path(__file__).resolve().parent.parent))

def get_transactions(path_to_file: Path) -> List:
    """Функция, возвращающая из json-файла данные о транзакциях"""
    try:
        with open(path_to_file) as json_file:
            try:
                # logger.info(f"Открываем json-файл {path_to_file}")
                transactions = json.load(json_file)
                return transactions
            except json.JSONDecodeError:
                # logger.error("Ошибка декодирования JSON")
                print("Ошибка декодирования JSON")
                return []
    except FileNotFoundError:
        # logger.error("Файл не найден")
        print("Файл не найден")
        return []
