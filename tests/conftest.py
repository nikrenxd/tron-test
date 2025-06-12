from decimal import Decimal

import pytest
from httpx import ASGITransport, AsyncClient

from src.core.database import engine, Base, Session
from src.core.settings import base_config
from src.main import create_app
from src.models.wallets import WalletInfo
from src.repositories.wallets import WalletsRepository
from src.services.wallets import WalletsServices


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture(autouse=True)
async def prepare_db():
    if base_config.MODE == "TEST":
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

        async with Session() as session:
            async with session.begin():
                session.add_all(
                    [
                        WalletInfo(
                            wallet_address=base_config.TRON_TEST_WALLET_ADDRESS,
                            balance=Decimal("1000.9234"),
                            bandwidth_limit=600,
                            bandwidth_left=73,
                            energy_limit=73,
                            energy_left=73,
                        ),
                        WalletInfo(
                            wallet_address=base_config.TRON_TEST_WALLET_ADDRESS,
                            balance=Decimal("1200.9234"),
                            bandwidth_limit=600,
                            bandwidth_left=73,
                            energy_limit=73,
                            energy_left=73,
                        ),
                    ]
                )


@pytest.fixture(scope="session")
def base_url():
    return base_config.BASE_URL


@pytest.fixture(scope="session")
def tron_test_wallet():
    return base_config.TRON_TEST_WALLET_ADDRESS


@pytest.fixture(scope="session")
def tron_test_wallet_data(tron_test_wallet):
    return {
        "wallet_address": tron_test_wallet,
        "balance": Decimal("1000.9234"),
        "bandwidth_limit": 600,
        "bandwidth_left": 73,
        "energy_limit": 73,
        "energy_left": 73,
    }


@pytest.fixture(scope="session")
def app():
    return create_app()


@pytest.fixture(scope="session")
def wallets_repository():
    return WalletsRepository()


@pytest.fixture(scope="session")
def wallets_services(wallets_repository):
    return WalletsServices(wallets_repository)


@pytest.fixture(scope="session")
async def client(app, base_url):
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url=base_url) as client:
        yield client
