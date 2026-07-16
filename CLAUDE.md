# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A TradingView → OANDA forex automation pipeline: a Pine Script strategy is backtested in
TradingView, then its alerts are routed through a small FastAPI webhook bridge that places
market orders against an OANDA account (practice or live). See README.md for the full
three-phase workflow (backtest → paper trade → live).

`remote-job-search-results.md` is unrelated content from a separate task; ignore it when
working on the trading pipeline.

## Commands

```bash
pip install -r requirements.txt        # install dependencies
python -m pytest                       # run all tests
python -m pytest tests/test_webhook.py                          # one file
python -m pytest tests/test_webhook.py::test_rejects_wrong_secret  # one test
uvicorn server.main:app --reload --port 8000                    # run the server locally
```

There is no linter, formatter, or build step configured.

## Architecture

Three components, connected only at runtime by the webhook contract:

- `pine_scripts/rsi2_mean_reversion_strategy.pine` — Pine Script v5 strategy pasted into
  TradingView. Its `alert()` calls emit the JSON payload the server expects. If you change
  the webhook contract in `server/main.py`, update the alert JSON here too (and vice versa).
- `server/` — the webhook bridge:
  - `main.py` — FastAPI app. `POST /webhook` validates the payload (`AlertPayload`),
    checks the shared secret with `hmac.compare_digest`, enforces the `MAX_ORDER_UNITS`
    cap, then dispatches to the OANDA client. `GET /health` reports the active environment.
    Orders are logged to `orders.log` in the working directory.
  - `oanda_client.py` — thin `requests` wrapper over the OANDA v20 REST API
    (`place_market_order`, `close_position`). Sign convention: positive units buy,
    negative units sell.
  - `config.py` — reads settings from environment variables (optionally an injected dict,
    which is how tests exercise it). Selects the practice vs. live API host and enforces
    the live-trading gate.
- `tests/` — pytest suite. `conftest.py` seeds dummy env vars **before** `server.main` is
  imported (module import instantiates `Settings()` and `OandaClient` at import time — this
  ordering matters). `test_webhook.py` uses FastAPI's `TestClient` with the OANDA client
  methods monkeypatched, so no test ever hits the real API.

## Webhook contract

`POST /webhook` takes `{"secret", "instrument", "action", "units"}` where `action` is
`buy`, `sell`, or `close_all`. `units` is ignored for `close_all` and rejected above
`MAX_ORDER_UNITS` for buy/sell. This contract is duplicated in the Pine script's `alert()`
strings — keep them in sync.

## Safety invariants — do not weaken

- Config is read from `.env` (copied from `.env.example`); `.env` is gitignored and must
  never be committed.
- `OANDA_ENVIRONMENT=live` refuses to start unless `LIVE_TRADING_CONFIRM` equals the exact
  phrase in `server/config.py` (`I_UNDERSTAND_THIS_TRADES_REAL_MONEY`). This speed bump is
  deliberate — preserve it in any config refactor.
- `MAX_ORDER_UNITS` is a hard per-order cap applied regardless of what an alert requests.
- The webhook secret is the only auth layer; secret comparison must stay constant-time
  (`hmac.compare_digest`).
- OANDA US enforces FIFO and disallows hedging; strategy logic assumes a single net
  position per instrument.

## Git note

The default branch (`master`) has no commits; all work lives on `claude/*` feature
branches. Check remote branches for the latest state before assuming the repo is empty.
