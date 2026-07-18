import requests

from server.config import Settings


class OandaError(Exception):
    pass


def format_price(price: float) -> str:
    """Format a price for OANDA's DecimalNumber fields, trimming trailing zeros
    (OANDA rejects prices with more decimal places than the instrument allows,
    e.g. more than 3 for JPY pairs)."""
    return f"{price:.5f}".rstrip("0").rstrip(".")


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

    def place_market_order(
        self,
        instrument: str,
        units: int,
        stop_loss: float | None = None,
        take_profit: float | None = None,
    ) -> dict:
        """units > 0 buys, units < 0 sells. Optional stop_loss / take_profit prices
        are attached to the fill as broker-side orders, so the position stays
        protected even if this server or the TradingView alert feed goes down."""
        order = {
            "type": "MARKET",
            "instrument": instrument,
            "units": str(units),
            "timeInForce": "FOK",
            "positionFill": "DEFAULT",
        }
        if stop_loss is not None:
            order["stopLossOnFill"] = {"price": format_price(stop_loss)}
        if take_profit is not None:
            order["takeProfitOnFill"] = {"price": format_price(take_profit)}
        body = {"order": order}
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

    def close_position_partial(self, instrument: str, units: int) -> dict:
        """Close part of the net position (units is unsigned; side is looked up)."""
        resp = self.session.get(self._url(f"/positions/{instrument}"), timeout=10)
        if resp.status_code >= 400:
            raise OandaError(f"OANDA position lookup failed ({resp.status_code}): {resp.text}")
        position = resp.json().get("position", {})
        long_units = float(position.get("long", {}).get("units", "0"))
        short_units = float(position.get("short", {}).get("units", "0"))
        if long_units > 0:
            body = {"longUnits": str(units)}
        elif short_units < 0:
            body = {"shortUnits": str(units)}
        else:
            raise OandaError(f"no open {instrument} position to partially close")
        resp = self.session.put(
            self._url(f"/positions/{instrument}/close"), json=body, timeout=10
        )
        if resp.status_code >= 400:
            raise OandaError(f"OANDA partial-close request failed ({resp.status_code}): {resp.text}")
        return resp.json()

    def set_trade_stop(self, instrument: str, stop_loss: float) -> dict:
        """Move the stop-loss on the open trade(s) for an instrument (e.g. to breakeven)."""
        resp = self.session.get(
            self._url("/trades"), params={"instrument": instrument, "state": "OPEN"}, timeout=10
        )
        if resp.status_code >= 400:
            raise OandaError(f"OANDA open-trades lookup failed ({resp.status_code}): {resp.text}")
        trades = resp.json().get("trades", [])
        if not trades:
            raise OandaError(f"no open {instrument} trade to modify")
        results = []
        for trade in trades:
            body = {"stopLoss": {"price": format_price(stop_loss), "timeInForce": "GTC"}}
            resp = self.session.put(
                self._url(f"/trades/{trade['id']}/orders"), json=body, timeout=10
            )
            if resp.status_code >= 400:
                raise OandaError(
                    f"OANDA stop modification failed ({resp.status_code}): {resp.text}"
                )
            results.append(resp.json())
        return {"modified": results}
