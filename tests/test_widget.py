import pytest

from src.widget import mask_account_card, get_date


@pytest.fixture
def gen_date():
    return "2024-03-11T02:26:18.671407"


def test_get_date(gen_date):

    assert get_date(gen_date) == "11.03.2024"


@pytest.mark.parametrize("string, expected_result", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361")
]
)
def test_mask_account_card(string, expected_result):
    assert mask_account_card(string) == expected_result
