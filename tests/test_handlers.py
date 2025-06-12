import pytest


@pytest.mark.anyio
async def test_get_wallets(client):
    res = await client.get("/wallets/", params={"limit": 1, "offset": 0})
    assert res.status_code == 200


@pytest.mark.anyio
async def test_create_wallet_record(client, tron_test_wallet):
    res = await client.post("/wallets/", json={"wallet_address": tron_test_wallet})

    assert res.status_code == 201
    assert res.json()["wallet_address"] == tron_test_wallet
