from decimal import Decimal

from pydantic import BaseModel


class WalletsBodySchema(BaseModel):
    wallet_address: str


class WalletsInfoSchema(WalletsBodySchema):
    balance: Decimal
    bandwidth_limit: int
    bandwidth_left: int
    energy_limit: int
    energy_left: int
