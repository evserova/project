import os
from unittest.mock import patch

from dotenv import load_dotenv

from src.external_api import get_transaction_sum

load_dotenv()


@patch("src.external_api.requests.request")
def test_external_api(mock_resp):
    token_exchange = os.getenv("API_KEY_exchange")
    mock_resp.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 30234.99},
        "info": {"timestamp": 1723453696, "rate": 90.348788},
        "date": "2024-08-12",
        "result": 2731694.701692,
    }
    assert (
        get_transaction_sum(
            {
                "id": 854048120,
                "state": "EXECUTED",
                "date": "2019-03-29T10:57:20.635567",
                "operationAmount": {"amount": "30234.99", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод с карты на счет",
                "from": "Visa Classic 1203921041964079",
                "to": "Счет 34616199494072692721",
            }
        )
        == 2731694.701692
    )
    mock_resp.assert_called_with(
        "GET",
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=30234.99",
        headers={"apikey": token_exchange},
    )
