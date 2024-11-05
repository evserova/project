import logging

logger = logging.getLogger('masks')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/masks.log", "w", encoding="utf-8")
file_formatter = (logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s"))
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер карты"""
    logger.info('Маскируем карту клиента')
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


print(get_mask_card_number("7000792289606361"))


def get_mask_account(account_num: str) -> str:
    """Функция, которая маскирует номер счета"""
    logger.info('Маскируем счет клиента')
    return f"**{account_num[-4:]}"


print(get_mask_account("73654108430135874305"))


def get_mask_account(acc_num: str) -> str:
    """Получаем номер аккаунта и выводим две звездочки и последние 4 цифры номера"""
    logger.info("Получен номер аккаунта.")

    if acc_num != "" and len(acc_num) > 6:
        hidden_num_list = "**", acc_num[-4:]
        hidden_acc_num = "".join(hidden_num_list)
        logger.info("Получили скрытый номер аккаунта.")
        return hidden_acc_num

    else:
        logger.error("Неподходящий номер аккаунта.")
        return ("Неправильно, введите номер счета.")
