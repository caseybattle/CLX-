import os

LIVE_CONFIRM_PHRASE = "I_UNDERSTAND_THIS_TRADES_REAL_MONEY"

OANDA_HOSTS = {
    "practice": "https://api-fxpractice.oanda.com",
    "live": "https://api-fxtrade.oanda.com",
}


class ConfigError(Exception):
    pass


class Settings:
    def __init__(self, env: dict | None = None):
        env = env if env is not None else os.environ

        self.oanda_api_token = env.get("OANDA_API_TOKEN", "")
        self.oanda_account_id = env.get("OANDA_ACCOUNT_ID", "")
        self.oanda_environment = env.get("OANDA_ENVIRONMENT", "practice").strip().lower()
        self.webhook_secret = env.get("WEBHOOK_SECRET", "")
        self.max_order_units = int(env.get("MAX_ORDER_UNITS", "10000"))
        self.live_trading_confirm = env.get("LIVE_TRADING_CONFIRM", "")

        if self.oanda_environment not in OANDA_HOSTS:
            raise ConfigError(
                f"OANDA_ENVIRONMENT must be 'practice' or 'live', got {self.oanda_environment!r}"
            )

        if self.oanda_environment == "live" and self.live_trading_confirm != LIVE_CONFIRM_PHRASE:
            raise ConfigError(
                "OANDA_ENVIRONMENT is set to 'live' but LIVE_TRADING_CONFIRM does not match "
                f"the required confirmation phrase {LIVE_CONFIRM_PHRASE!r}. Refusing to start "
                "with live trading enabled until this is set explicitly."
            )

    @property
    def oanda_base_url(self) -> str:
        return OANDA_HOSTS[self.oanda_environment]
