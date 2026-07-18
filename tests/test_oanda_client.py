import pytest

from server.oanda_client import format_price


@pytest.mark.parametrize(
    "price,expected",
    [
        (1.1234567, "1.12346"),   # rounded to 5 decimals
        (1.12100, "1.121"),       # trailing zeros trimmed
        (150.123, "150.123"),     # JPY-style precision preserved
        (1.0, "1"),               # whole number stays a valid DecimalNumber
    ],
)
def test_format_price(price, expected):
    assert format_price(price) == expected
