import pytest

from server.config import ConfigError, Settings


def base_env(**overrides):
    env = {
        "OANDA_API_TOKEN": "token",
        "OANDA_ACCOUNT_ID": "account",
        "OANDA_ENVIRONMENT": "practice",
        "WEBHOOK_SECRET": "secret",
        "MAX_ORDER_UNITS": "10000",
        "LIVE_TRADING_CONFIRM": "",
    }
    env.update(overrides)
    return env


def test_practice_environment_does_not_require_confirmation():
    settings = Settings(base_env())
    assert settings.oanda_base_url == "https://api-fxpractice.oanda.com"


def test_live_environment_requires_exact_confirmation_phrase():
    with pytest.raises(ConfigError):
        Settings(base_env(OANDA_ENVIRONMENT="live", LIVE_TRADING_CONFIRM="yes"))


def test_live_environment_accepted_with_correct_confirmation_phrase():
    settings = Settings(
        base_env(
            OANDA_ENVIRONMENT="live",
            LIVE_TRADING_CONFIRM="I_UNDERSTAND_THIS_TRADES_REAL_MONEY",
        )
    )
    assert settings.oanda_base_url == "https://api-fxtrade.oanda.com"


def test_invalid_environment_rejected():
    with pytest.raises(ConfigError):
        Settings(base_env(OANDA_ENVIRONMENT="staging"))
