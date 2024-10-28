import json
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"logs.utils.log", "w")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(asctime)s %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def get_info(path) -> list:
    """Функция получения объекта Python от JSON-файла"""
    try:
        logger.info("Попытка преобразовать файл")
        with open(path) as file:
            py_file = json.load(file)
            return py_file
    except (FileNotFoundError, json.JSONDecodeError):
        logger.error("Файл не найден")
        return ["Ошибка"]