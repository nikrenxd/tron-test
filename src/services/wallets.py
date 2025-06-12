from dataclasses import dataclass

from tronpy import AsyncTron

from src.models.wallets import WalletInfo
from src.repositories.wallets import WalletsRepository


@dataclass
class WalletsServices:
    repository: WalletsRepository

    async def get_account_info(self, wallet_address: str) -> dict:
        async with AsyncTron(network="shasta") as client:
            account_balance = await client.get_account_balance(wallet_address)
            resources = await client.get_account_resource(wallet_address)

            bandwidth_limit = resources.get("freeNetLimit", 0)
            bandwidth_left = bandwidth_limit - resources.get("freeNetUsed", 0)

            energy_limit = resources.get("EnergyLimit", 0)
            energy_left = energy_limit - resources.get("EnergyUsed", 0)

            account_data = {
                "wallet_address": wallet_address,
                "balance": account_balance,
                "bandwidth_limit": bandwidth_limit,
                "bandwidth_left": bandwidth_left,
                "energy_limit": energy_limit,
                "energy_left": energy_left,
            }

            return account_data

    async def get_last_accounts_info(self, limit: int, offset: int) -> list[WalletInfo]:
        return await self.repository.get_wallets_info(limit, offset)

    async def save_account_info(self, **data) -> str | None:
        return await self.repository.create_wallet_info(**data)
