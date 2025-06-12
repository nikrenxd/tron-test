import pytest


@pytest.mark.anyio
async def test_save_account_info(wallets_services, tron_test_wallet_data):
    res = await wallets_services.save_account_info(**tron_test_wallet_data)

    assert res == tron_test_wallet_data["wallet_address"]


@pytest.mark.anyio
async def test_get_last_accounts_info(wallets_services, tron_test_wallet):
    res = await wallets_services.get_last_accounts_info(limit=1, offset=0)

    assert res[0].wallet_address == tron_test_wallet

@pytest.mark.anyio
async def test_get_account_info(wallets_services, tron_test_wallet):
    res = await wallets_services.get_account_info(tron_test_wallet)

    assert res["wallet_address"] == tron_test_wallet