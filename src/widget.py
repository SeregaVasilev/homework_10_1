from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """Функция маскирующая номер карты или счета"""
    info_text = ""
    info_number = ""
    number_count = 0
    for i in info:
        if i.isalpha():
            info_text += i
        elif i.isdigit():
            info_number += i
            number_count += 1
    if number_count > 16:
        return f"{info_text} {get_mask_account(info_number)}"
    else:
        return f"{info_text} {get_mask_card_number(info_number)}"


def get_date(date: str) -> str:
    """Функция выводящая дату в привычный вид"""
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
