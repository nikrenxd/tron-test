from sqlalchemy.orm import Mapped

from src.core.database import Base, int_pk

class WalletInfo(Base):
    __tablename__ = "wallet_info"

    id: Mapped[int_pk]
    balance_id: Mapped[str]
    bandwidth: Mapped[float]
    energy: Mapped[float]
    balance: Mapped[float]

    def __str__(self):
        return f"Balance with id - {self.balance_id}"
