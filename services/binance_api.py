"""
Binance Futures REST API.
"""

from typing import List

import requests

from config.settings import BINANCE_FAPI_URL, REQUEST_TIMEOUT
from utils.logger import get_logger

logger = get_logger(__name__)


class BinanceAPI:

    def __init__(self):
        self.base_url = BINANCE_FAPI_URL

    def get_exchange_info(self) -> dict:

        url = f"{self.base_url}/fapi/v1/exchangeInfo"

        response = requests.get(
            url,
            timeout=REQUEST_TIMEOUT
        )

        response.raise_for_status()

        return response.json()

    def get_usdt_symbols(self) -> List[str]:

        data = self.get_exchange_info()

        symbols = []

        for item in data["symbols"]:

            if (
                item["quoteAsset"] == "USDT"
                and item["status"] == "TRADING"
                and item["contractType"] == "PERPETUAL"
            ):

                symbols.append(item["symbol"])

        logger.info("Found %s USDT perpetual contracts", len(symbols))

        return sorted(symbols)