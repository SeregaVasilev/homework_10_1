import pytest


@pytest.fixture
def card_number():
    return "7000 79** **** 6361"


@pytest.fixture
def account():
    return "**4305"


@pytest.fixture
def mask_account():
    return "Счет **5421"


@pytest.fixture
def account_card_number():
    return "VisaPlatinum 7000 79** **** 6361"


@pytest.fixture
def date():
    return "11.03.2024"


@pytest.fixture
def list_dict():
    return [
        {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
        {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
    ]
