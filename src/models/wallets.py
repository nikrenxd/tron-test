from decimal import Decimal

from sqlalchemy import Numeric
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from src.core.database import Base, int_pk


class WalletInfo(Base):
    __tablename__ = "wallet_info"

    id: Mapped[int_pk]
    wallet_address: Mapped[str]
    balance: Mapped[Decimal] = mapped_column(Numeric(12, 4))
    bandwidth_limit: Mapped[int]
    bandwidth_left: Mapped[int]
    energy_limit: Mapped[int]
    energy_left: Mapped[int]

    def __str__(self):
        return f"Balance with id - {self.balance_id}"
