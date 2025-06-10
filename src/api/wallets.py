from fastapi import APIRouter

from src.api.dependencies import WalletsServicesDependency
from src.api.schemas.wallets import WalletsBodySchema, WalletsInfoSchema

router = APIRouter(prefix="/wallets", tags=["wallets"])


@router.post("/", response_model=WalletsInfoSchema)
async def create_wallet_record(
    data: WalletsBodySchema,
    wallets_services: WalletsServicesDependency,
):
    wallet_info = await wallets_services.get_account_info(data.wallet_address)
    await wallets_services.save_account_info(**wallet_info)
    return wallet_info
