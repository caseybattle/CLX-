import requests

from server.config import Settings


class OandaError(Exception):
    pass


class OandaClient:
    """Thin wrapper around the OANDA v20 REST API for market orders and position closes.

    Docs: https://developer.oanda.com/rest-live-v20/introduction/
    """

    def __init__(self, settings: Settings):
        self.settings = settings
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Bearer {settings.oanda_api_token}",
                "Content-Type": "application/json",
            }
        )

    def _url(self, path: str) -> str:
        return f"{self.settings.oanda_base_url}/v3/accounts/{self.settings.oanda_account_id}{path}"

    def place_market_order(self, instrument: str, units: int) -> dict:
        """units > 0 buys, units < 0 sells."""
        body = {
            "order": {
                "type": "MARKET",
                "instrument": instrument,
                "units": str(units),
                "timeInForce": "FOK",
                "positionFill": "DEFAULT",
            }
        }
        resp = self.session.post(self._url("/orders"), json=body, timeout=10)
        if resp.status_code >= 400:
            raise OandaError(f"OANDA order request failed ({resp.status_code}): {resp.text}")
        return resp.json()

    def close_position(self, instrument: str) -> dict:
        body = {"longUnits": "ALL", "shortUnits": "ALL"}
        resp = self.session.put(
            self._url(f"/positions/{instrument}/close"), json=body, timeout=10
        )
        if resp.status_code >= 400:
            raise OandaError(f"OANDA close-position request failed ({resp.status_code}): {resp.text}")
        return resp.json()
