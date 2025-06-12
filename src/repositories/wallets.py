import logging
from dataclasses import dataclass

from sqlalchemy import select, insert
from sqlalchemy.exc import SQLAlchemyError

from src.core.database import Session
from src.models.wallets import WalletInfo

logger = logging.getLogger("repositories.wallets")


@dataclass
class WalletsRepository:
    async def create_wallet_info(self, **data) -> str | None:
        async with Session() as session:
            try:
                insert_wallet = (
                    insert(WalletInfo)
                    .values(**data)
                    .returning(WalletInfo.wallet_address)
                )
                res = await session.execute(insert_wallet)
                await session.commit()

                return res.scalar()
            except SQLAlchemyError:
                logger.error(
                    "SQLAlchemyError while creating wallet record", exc_info=True
                )

    async def get_wallets_info(self, limit: int, offset: int) -> list[WalletInfo]:
        async with Session() as session:
            try:
                select_wallets = (
                    select(WalletInfo)
                    .offset(offset)
                    .limit(limit)
                    .order_by(WalletInfo.id.desc())
                )

                res = await session.execute(select_wallets)
                return res.scalars().all()
            except SQLAlchemyError:
                logger.error(
                    "SQLAlchemyError while getting wallets info", exc_info=True
                )
