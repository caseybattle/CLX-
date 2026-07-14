# TradingView -> OANDA Automation

A three-phase pipeline for turning a TradingView strategy idea into automated forex trading,
built around Claude Code writing/backtesting Pine Script and a small webhook bridge that
routes TradingView alerts to an OANDA account.

Broker: **OANDA US**. It's the only TradingView-integrated broker that both accepts US
clients and ships a documented, free REST API (v20) with a no-cost practice account, which
made it the practical choice for going from "backtest in TradingView" to "place real orders"
without switching platforms mid-project.

## Phase 1 — Backtest in TradingView (no credentials needed)

1. Open TradingView Desktop (or use it with Claude Code + a TradingView MCP bridge, as
   described in `pine_scripts/`), and load the chart for the instrument you want to test.
2. Pine Editor -> Create new -> **Strategy** -> paste in
   `pine_scripts/rsi2_mean_reversion_strategy.pine`.
3. Add it to the chart, open the **Strategy Tester** tab, and review the metrics (net profit,
   win rate, drawdown, trade count) vs. buy-and-hold.
4. Iterate on the inputs (RSI length/level, SMA lengths, instrument) until you're happy with
   the backtest. This step never touches a broker — it's pure historical simulation.

## Phase 2 — Paper trade against OANDA's practice account

1. Open a free account at https://www.oanda.com/us-en/trading/ and switch to (or create) a
   **practice** sub-account — no funding required.
2. Generate a personal API token: account settings -> "Manage API Access" (or
   https://www.oanda.com/demo-account/tpa/personal_token for practice tokens).
3. Copy `.env.example` to `.env` and fill in `OANDA_API_TOKEN` and `OANDA_ACCOUNT_ID`. Leave
   `OANDA_ENVIRONMENT=practice`. Set `WEBHOOK_SECRET` to a long random string
   (`openssl rand -hex 32`).
4. Install dependencies and start the server:
   ```
   pip install -r requirements.txt
   uvicorn server.main:app --reload --port 8000
   ```
5. For TradingView (cloud) to reach your local machine, tunnel it, e.g. with ngrok:
   `ngrok http 8000`, then use the resulting HTTPS URL + `/webhook` as your alert's webhook URL.
6. In TradingView, add an alert on the strategy with condition **"Any alert() function call"**,
   and set the webhook URL to `https://<your-tunnel>/webhook`. The Pine script already emits
   the correct JSON body (see the `alert(...)` calls at the bottom of the `.pine` file) — just
   replace the placeholder `WEBHOOK_SECRET` string in the script with the value from your `.env`.
7. Watch `orders.log` (created next to wherever you run uvicorn) and the OANDA practice
   account's transaction history to confirm alerts are producing the trades you expect.

Run the test suite any time with:
```
python -m pytest
```

## Phase 3 — Live trading (only after Phase 2 has run cleanly for a while)

This is a deliberate, multi-step switch — don't flip it casually:

1. Fund a **live** OANDA account and generate a live API token (different from the practice
   token).
2. In `.env`, set `OANDA_ACCOUNT_ID` and `OANDA_API_TOKEN` to the live values, and set
   `OANDA_ENVIRONMENT=live`.
3. The server refuses to start with `OANDA_ENVIRONMENT=live` unless
   `LIVE_TRADING_CONFIRM=I_UNDERSTAND_THIS_TRADES_REAL_MONEY` is also set — this is a deliberate
   speed bump so live trading can't be enabled by an accidental config change.
4. Set `MAX_ORDER_UNITS` to a conservative cap while you build confidence — every order the
   webhook receives is rejected if it exceeds this, regardless of what the alert requests.
5. Consider running the live server on a machine that stays on (a small VPS) rather than your
   laptop, since a dropped connection means missed alerts.

## Webhook contract

`POST /webhook` expects a JSON body:
```json
{
  "secret": "must match WEBHOOK_SECRET",
  "instrument": "EUR_USD",
  "action": "buy | sell | close_all",
  "units": 1000
}
```
`units` is ignored for `close_all` (it closes the entire position, long or short) and is
capped at `MAX_ORDER_UNITS` for `buy`/`sell`.

## Repo layout

- `pine_scripts/` — Pine Script v5 strategies to paste into TradingView's Pine Editor.
- `server/` — FastAPI webhook bridge (`main.py`), OANDA v20 client (`oanda_client.py`), and
  config/env handling (`config.py`).
- `tests/` — unit tests covering auth rejection, unit caps, order routing, and the
  practice/live confirmation gate.

## Safety notes

- Never commit `.env` — it's already in `.gitignore`.
- The webhook secret is your only auth layer; use a long random value and keep the tunnel URL
  private.
- `MAX_ORDER_UNITS` is a blunt safety net, not a risk-management system — it caps order size,
  it does not manage overall account exposure across multiple open positions.
- OANDA US enforces FIFO and disallows hedging by regulation; the strategy logic here assumes
  a single net position per instrument.
