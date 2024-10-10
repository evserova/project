import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.fixture
def mask_card_number():
    return "7000792289606361"


def test_get_mask_card_number():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


@pytest.fixture
def mask_account():
    return "73654108430135874305"


def test_get_mask_account(mask_account):
    assert get_mask_account(mask_account) == "**4305"


@pytest.mark.parametrize("string, expected_result", [
    ("7158300734726758", "7158 30** **** 6758"),
    ("7158300734726759", "7158 30** **** 6759"),
]
)
def test_get_mask_card_number(string, expected_result):
    assert get_mask_card_number(string) == expected_result
