import pytest

from server.oanda_client import format_price


@pytest.mark.parametrize(
    "price,instrument,expected",
    [
        (1.1234567, "EUR_USD", "1.12346"),   # rounded to 5 decimals
        (1.12100, "EUR_USD", "1.121"),       # trailing zeros trimmed
        (1.0, "EUR_USD", "1"),               # whole number stays a valid DecimalNumber
        (155.12346, "USD_JPY", "155.123"),   # JPY pairs rounded to 3 decimals
        (155.10000, "usd_jpy", "155.1"),     # case-insensitive instrument match
    ],
)
def test_format_price(price, instrument, expected):
    assert format_price(price, instrument) == expected
