# Проект "Виджет банковских операций"

## Описание:

Программа показывает последние успешные банковские операции клиента. Фильтрует их по дате и оплате.

## Требования к окружению:

* Python 3.12.5
* flake8 = "7.1.0"
* black = "24.4.2"
* isort = "5.13.2"
* mypy = "1.10.0"

## Установка:

* Клонируйте репозиторий:
```
git clone https://github.com/evserova/project.git
```

* Установите зависимости:
```
pip install -r requirements.txt
```

## Использование:

1. Модуль masks.py принимает на вход номер карты или счета и маскирует их.
2. Модуль widget.py принимает наименование карты или счет и номер и возвращает замаскированный номер.
3. Модуль processing.py принимает список операций и возвращает отсортированные списки.

