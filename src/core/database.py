from typing import Annotated

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, declared_attr, mapped_column

from src.core.settings import base_config

DB_URL = base_config.DB_URL

if base_config.MODE == "TEST":
    DB_URL = base_config.TEST_DB_URL

engine = create_async_engine(
    url=DB_URL,
    echo=False,
)

Session = async_sessionmaker(engine, expire_on_commit=False)

int_pk = Annotated[int, mapped_column(primary_key=True)]


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"
