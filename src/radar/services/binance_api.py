"""
Binance Futures REST API Client
"""

import requests

from src.radar.config.settings import settings
from src.radar.utils.logger import get_logger


logger = get_logger(__name__)


class BinanceAPI:

    def __init__(self):
        self.base_url = settings.BINANCE_FAPI_URL


    def _get(self, endpoint):

        response = requests.get(
            self.base_url + endpoint,
            timeout=settings.REQUEST_TIMEOUT
        )

        response.raise_for_status()

        return response.json()


    def get_exchange_info(self):

        return self._get(
            "/fapi/v1/exchangeInfo"
        )


    def get_market_tickers(self):

        return self._get(
            "/fapi/v1/ticker/24hr"
        )


    def get_open_interest(
        self,
        symbol
    ):

        return self._get(
            f"/fapi/v1/openInterest?symbol={symbol}"
        )


    def get_funding_rate(
        self,
        symbol
    ):

        data = self._get(
            f"/fapi/v1/premiumIndex?symbol={symbol}"
        )

        return {
            "fundingRate": float(
                data["lastFundingRate"]
            )
        }


    def get_klines(
        self,
        symbol,
        interval="5m",
        limit=100
    ):

        return self._get(
            f"/fapi/v1/klines?"
            f"symbol={symbol}"
            f"&interval={interval}"
            f"&limit={limit}"
        )


    def get_usdt_perpetual_symbols(self):

        exchange = self.get_exchange_info()

        symbols = []

        for s in exchange["symbols"]:

            if (
                s["quoteAsset"] == "USDT"
                and s["status"] == "TRADING"
                and s["contractType"] == "PERPETUAL"
            ):
                symbols.append(
                    s["symbol"]
                )

        logger.info(
            "Loaded %s USDT perpetual contracts",
            len(symbols)
        )

        return symbols