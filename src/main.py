from fastapi import FastAPI

from src.core.log import logging_init_config, LOGGING_CONFIG
from src.api.wallets import router as wallets_router


def create_app() -> FastAPI:
    _app = FastAPI()

    logging_init_config(LOGGING_CONFIG)

    _app.include_router(wallets_router)

    return _app


app = create_app()
