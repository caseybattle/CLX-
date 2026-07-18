import hmac
import logging

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, field_validator

from server.config import Settings
from server.oanda_client import OandaClient, OandaError

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.FileHandler("orders.log"), logging.StreamHandler()],
)
logger = logging.getLogger("webhook")

ALLOWED_ACTIONS = {"buy", "sell", "close_all", "close_partial", "modify_stop"}

app = FastAPI(title="TradingView -> OANDA webhook bridge")
settings = Settings()
oanda = OandaClient(settings)


class AlertPayload(BaseModel):
    secret: str
    instrument: str
    action: str
    units: int = 0
    stop_loss: float | None = None
    take_profit: float | None = None

    @field_validator("action")
    @classmethod
    def action_must_be_known(cls, v: str) -> str:
        if v not in ALLOWED_ACTIONS:
            raise ValueError(f"action must be one of {sorted(ALLOWED_ACTIONS)}")
        return v

    @field_validator("stop_loss", "take_profit")
    @classmethod
    def price_levels_must_be_positive(cls, v: float | None) -> float | None:
        if v is not None and v <= 0:
            raise ValueError("price levels must be positive")
        return v


@app.get("/health")
def health():
    return {"status": "ok", "environment": settings.oanda_environment}


@app.post("/webhook")
async def webhook(request: Request):
    raw_body = await request.body()
    try:
        payload = AlertPayload.model_validate_json(raw_body)
    except Exception as exc:
        logger.warning("Rejected malformed alert payload: %s", exc)
        raise HTTPException(status_code=400, detail="invalid alert payload") from exc

    if not hmac.compare_digest(payload.secret, settings.webhook_secret):
        logger.warning("Rejected alert with invalid secret for instrument=%s", payload.instrument)
        raise HTTPException(status_code=401, detail="invalid secret")

    if payload.action == "modify_stop" and payload.stop_loss is None:
        logger.warning("Rejected modify_stop without stop_loss for instrument=%s", payload.instrument)
        raise HTTPException(status_code=400, detail="modify_stop requires stop_loss")

    units = abs(payload.units)
    if payload.action == "close_partial" and units == 0:
        logger.warning("Rejected close_partial without units for instrument=%s", payload.instrument)
        raise HTTPException(status_code=400, detail="close_partial requires units > 0")
    if units > settings.max_order_units:
        logger.warning(
            "Rejected order exceeding MAX_ORDER_UNITS: requested=%s cap=%s",
            units,
            settings.max_order_units,
        )
        raise HTTPException(status_code=400, detail="units exceeds MAX_ORDER_UNITS")

    logger.info(
        "Accepted alert: instrument=%s action=%s units=%s environment=%s",
        payload.instrument,
        payload.action,
        units,
        settings.oanda_environment,
    )

    try:
        if payload.action == "buy":
            result = oanda.place_market_order(
                payload.instrument, units,
                stop_loss=payload.stop_loss, take_profit=payload.take_profit,
            )
        elif payload.action == "sell":
            result = oanda.place_market_order(
                payload.instrument, -units,
                stop_loss=payload.stop_loss, take_profit=payload.take_profit,
            )
        elif payload.action == "close_partial":
            result = oanda.close_position_partial(payload.instrument, units)
        elif payload.action == "modify_stop":
            result = oanda.set_trade_stop(payload.instrument, payload.stop_loss)
        else:  # close_all
            result = oanda.close_position(payload.instrument)
    except OandaError as exc:
        logger.error("OANDA request failed: %s", exc)
        raise HTTPException(status_code=502, detail=str(exc)) from exc

    logger.info("OANDA response for %s %s: %s", payload.instrument, payload.action, result)
    return {"status": "ok", "oanda_response": result}
