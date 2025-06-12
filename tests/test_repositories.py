import pytest


@pytest.mark.anyio
async def test_create_wallet_info(wallets_repository, tron_test_wallet_data):
    res = await wallets_repository.create_wallet_info(**tron_test_wallet_data)

    assert res == tron_test_wallet_data["wallet_address"]


@pytest.mark.anyio
async def test_get_wallet_info(wallets_repository, tron_test_wallet):
    res = await wallets_repository.get_wallets_info(limit=1, offset=0)

    assert res[0].wallet_address == tron_test_wallet
