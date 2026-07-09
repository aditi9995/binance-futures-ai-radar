"""
Binance Futures REST API Client
"""

from __future__ import annotations

from typing import List

import requests

from src.radar.config.settings import settings
from src.radar.utils.logger import get_logger


logger = get_logger(__name__)


class BinanceAPI:

    def __init__(self) -> None:
        self.base_url = settings.BINANCE_FAPI_URL

    def get_exchange_info(self) -> dict:

        url = f"{self.base_url}/fapi/v1/exchangeInfo"

        response = requests.get(
            url,
            timeout=settings.REQUEST_TIMEOUT,
        )

        response.raise_for_status()

        return response.json()

    def get_usdt_perpetual_symbols(self) -> List[str]:

        exchange = self.get_exchange_info()

        symbols = []

        for symbol in exchange["symbols"]:

            if (
                symbol["quoteAsset"] == "USDT"
                and symbol["status"] == "TRADING"
                and symbol["contractType"] == "PERPETUAL"
            ):

                symbols.append(symbol["symbol"])

        symbols.sort()

        logger.info(
            "Loaded %s USDT perpetual contracts",
            len(symbols),
        )

        return symbols