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
## Тестирование.
* В терминале написать следующую команду:
'''
pytest
'''
* Чтобы проверить охват тестирования кода необходимо написать команду:
'''
pytest --cov
'''
## Использование:
1. Модуль masks.py принимает на вход номер карты или счета и маскирует их.
2. Модуль widget.py принимает наименование карты или счет и номер и возвращает замаскированный номер.
3. Модуль processing.py принимает список операций и возвращает отсортированные списки.
4. Модуль generators.py позволяет обрабатывать функцию по нужным параметрам. 
Примеры использования реализованных функций: 
* for card_number in card_number_generator(1, 9):
    print(card_number). 
5. Модуль decorators.py позволяет обрабатывать функцию по нужным параметрам. 
Чтобы использовать декоратор, достаточно перед любой функцией иметь запись следующего типа:
@decorator_name.
