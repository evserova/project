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

@pytest.mark.parametrize("value, expected", [
        ("2002-11-11T02:26:18.671407", "11.11.2002"),
        ("2010-06-12T02:26:18.671407", "12.06.2010"),
        ("2024-01-13T02:26:18.671407", "13.01.2024"),
        ("2025-07-14T02:26:18.671407", "14.07.2025"),
    ])
def test_get_date(value, expected):
        assert get_date(value) == expected
