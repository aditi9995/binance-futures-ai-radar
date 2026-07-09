"""
Global application settings.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    APP_NAME: str = "Binance Futures AI Radar"

    BINANCE_FAPI_URL: str = "https://fapi.binance.com"

    REQUEST_TIMEOUT: int = 10

    REFRESH_SECONDS: int = 30


settings = Settings()