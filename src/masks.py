def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует номер карты"""
    if len(card_number) != 16:
        raise ValueError("Номер карты должен состоять из 16 цифр")
    return card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]


def get_mask_account(account_number: str) -> str:
    """Функция маскирует номер аккаунта"""
    if len(account_number) != 20:
        raise ValueError("Номер аккаунта должен состоять из 20 цифр")
    return "**" + account_number[-4:]
