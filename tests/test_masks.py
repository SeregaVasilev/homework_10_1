import pytest

from src.masks import get_mask_account, get_mask_card_number


# проверка правильности маскирования карты
def test_get_mask_card_number(card_number):
    assert get_mask_card_number("7000792289606361") == card_number


# тестирование на необходимое количетсво цифр
def test_invalid_card_number():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("70007922896063615")
    assert str(exc_info.value) == "Номер карты должен состоять из 16 цифр"


# проверка правильности маскирования аккаунта
def test_get_mask_account(account):
    assert get_mask_account("73654108430135874305") == account


# тестирование на необходимое количетсво цифр
def test_invalid_account():
    with pytest.raises(ValueError) as exc_info:
        get_mask_account("70007922896063615")
    assert str(exc_info.value) == "Номер аккаунта должен состоять из 20 цифр"
