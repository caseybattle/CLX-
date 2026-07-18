import pytest
from fastapi.testclient import TestClient

from server import main


@pytest.fixture
def client():
    return TestClient(main.app)


@pytest.fixture(autouse=True)
def stub_oanda(monkeypatch):
    calls = {}

    def fake_place_market_order(self, instrument, units, stop_loss=None, take_profit=None):
        calls["place_market_order"] = (instrument, units, stop_loss, take_profit)
        return {"orderFillTransaction": {"id": "1"}}

    def fake_close_position(self, instrument):
        calls["close_position"] = (instrument,)
        return {"longOrderFillTransaction": {"id": "2"}}

    def fake_close_position_partial(self, instrument, units):
        calls["close_position_partial"] = (instrument, units)
        return {"longOrderFillTransaction": {"id": "3"}}

    def fake_set_trade_stop(self, instrument, stop_loss):
        calls["set_trade_stop"] = (instrument, stop_loss)
        return {"modified": [{"id": "4"}]}

    def fake_has_open_position(self, instrument):
        return calls.get("open_position", False)

    monkeypatch.setattr(main.OandaClient, "place_market_order", fake_place_market_order)
    monkeypatch.setattr(main.OandaClient, "close_position", fake_close_position)
    monkeypatch.setattr(main.OandaClient, "close_position_partial", fake_close_position_partial)
    monkeypatch.setattr(main.OandaClient, "set_trade_stop", fake_set_trade_stop)
    monkeypatch.setattr(main.OandaClient, "has_open_position", fake_has_open_position)
    return calls


def test_health_check(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"


def test_rejects_wrong_secret(client):
    resp = client.post(
        "/webhook",
        json={"secret": "wrong", "instrument": "EUR_USD", "action": "buy", "units": 1000},
    )
    assert resp.status_code == 401


def test_rejects_unknown_action(client):
    resp = client.post(
        "/webhook",
        json={"secret": "test-secret", "instrument": "EUR_USD", "action": "yolo", "units": 1000},
    )
    assert resp.status_code == 400


def test_rejects_units_over_cap(client):
    resp = client.post(
        "/webhook",
        json={"secret": "test-secret", "instrument": "EUR_USD", "action": "buy", "units": 999999},
    )
    assert resp.status_code == 400


def test_buy_places_positive_units_order(client, stub_oanda):
    resp = client.post(
        "/webhook",
        json={"secret": "test-secret", "instrument": "EUR_USD", "action": "buy", "units": 1000},
    )
    assert resp.status_code == 200
    assert stub_oanda["place_market_order"] == ("EUR_USD", 1000, None, None)


def test_sell_places_negative_units_order(client, stub_oanda):
    resp = client.post(
        "/webhook",
        json={"secret": "test-secret", "instrument": "EUR_USD", "action": "sell", "units": 1000},
    )
    assert resp.status_code == 200
    assert stub_oanda["place_market_order"] == ("EUR_USD", -1000, None, None)


def test_buy_passes_stop_loss_and_take_profit(client, stub_oanda):
    resp = client.post(
        "/webhook",
        json={
            "secret": "test-secret",
            "instrument": "EUR_USD",
            "action": "buy",
            "units": 1000,
            "stop_loss": 1.1210,
            "take_profit": 1.1590,
        },
    )
    assert resp.status_code == 200
    assert stub_oanda["place_market_order"] == ("EUR_USD", 1000, 1.1210, 1.1590)


def test_rejects_entry_when_position_already_open(client, stub_oanda):
    stub_oanda["open_position"] = True
    resp = client.post(
        "/webhook",
        json={"secret": "test-secret", "instrument": "EUR_USD", "action": "buy", "units": 1000},
    )
    assert resp.status_code == 409
    assert "place_market_order" not in stub_oanda


def test_close_partial_routes_units(client, stub_oanda):
    resp = client.post(
        "/webhook",
        json={"secret": "test-secret", "instrument": "EUR_USD", "action": "close_partial", "units": 500},
    )
    assert resp.status_code == 200
    assert stub_oanda["close_position_partial"] == ("EUR_USD", 500)


def test_close_partial_requires_units(client):
    resp = client.post(
        "/webhook",
        json={"secret": "test-secret", "instrument": "EUR_USD", "action": "close_partial", "units": 0},
    )
    assert resp.status_code == 400


def test_modify_stop_routes_price(client, stub_oanda):
    resp = client.post(
        "/webhook",
        json={
            "secret": "test-secret",
            "instrument": "EUR_USD",
            "action": "modify_stop",
            "units": 0,
            "stop_loss": 1.14268,
        },
    )
    assert resp.status_code == 200
    assert stub_oanda["set_trade_stop"] == ("EUR_USD", 1.14268)


def test_modify_stop_requires_stop_loss(client):
    resp = client.post(
        "/webhook",
        json={"secret": "test-secret", "instrument": "EUR_USD", "action": "modify_stop", "units": 0},
    )
    assert resp.status_code == 400


def test_rejects_non_positive_price_levels(client):
    resp = client.post(
        "/webhook",
        json={
            "secret": "test-secret",
            "instrument": "EUR_USD",
            "action": "buy",
            "units": 1000,
            "stop_loss": -1.5,
        },
    )
    assert resp.status_code == 400


def test_close_all_closes_position(client, stub_oanda):
    resp = client.post(
        "/webhook",
        json={"secret": "test-secret", "instrument": "EUR_USD", "action": "close_all", "units": 0},
    )
    assert resp.status_code == 200
    assert stub_oanda["close_position"] == ("EUR_USD",)
