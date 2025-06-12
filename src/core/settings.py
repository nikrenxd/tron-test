from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    DB_URL: str
    BASE_URL: str
    TEST_DB_URL: str
    TRON_TEST_WALLET_ADDRESS: str
    MODE: Literal["TEST", "DEV"]

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


base_config = BaseConfig()
