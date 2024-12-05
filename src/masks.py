def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует номер карты"""
    return card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]


def get_mask_account(account_number: str) -> str:
    """Функция маскирует номер аккаунта"""
    return "**" + account_number[-4:]
