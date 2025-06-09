from typing import Annotated

from fastapi import Depends

from src.repositories.wallets import WalletsRepository
from src.services.wallets import WalletsServices


wallets_repository = WalletsRepository()
wallets_services = WalletsServices(wallets_repository)


def get_wallets_services() -> WalletsServices:
    return wallets_services


WalletsServicesDependency = Annotated[WalletsServices, Depends(get_wallets_services)]
