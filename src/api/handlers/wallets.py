from fastapi import APIRouter, status, HTTPException

from src.api.dependencies import WalletsServicesDependency
from src.api.schemas.wallets import WalletsBodySchema, WalletsInfoSchema

router = APIRouter(prefix="/wallets", tags=["wallets"])


@router.post(
    "/",
    response_model=WalletsInfoSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_wallet_record(
    data: WalletsBodySchema,
    wallets_services: WalletsServicesDependency,
):
    wallet_info = await wallets_services.get_account_info(data.wallet_address)
    res = await wallets_services.save_account_info(**wallet_info)
    if not res:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    return wallet_info


@router.get("/", response_model=list[WalletsInfoSchema])
async def get_wallets(
    limit: int,
    offset: int,
    wallets_services: WalletsServicesDependency,
):
    wallets = await wallets_services.get_last_accounts_info(limit, offset)
    return wallets
