import pandas as pd

from src.radar.services.binance_api import BinanceAPI


class MarketDataService:


    def __init__(self):

        self.api = BinanceAPI()


    def get_exchange_info(self):

        return self.api.get_exchange_info()


    def get_tickers(self):

        return self.api.get_market_tickers()


    def get_open_interest(
        self,
        symbol
    ):

        data = self.api.get_open_interest(
            symbol
        )

        return float(
            data["openInterest"]
        )


    def get_funding_rate(
        self,
        symbol
    ):

        return self.api.get_funding_rate(
            symbol
        )["fundingRate"]


    def get_klines(
        self,
        symbol,
        interval="5m",
        limit=100
    ):

        data = self.api.get_klines(
            symbol,
            interval,
            limit
        )


        df = pd.DataFrame(
            data,
            columns=[
                "time",
                "open",
                "high",
                "low",
                "close",
                "volume",
                "close_time",
                "quote_volume",
                "trades",
                "buy_base",
                "buy_quote",
                "ignore"
            ]
        )


        for col in [
            "open",
            "high",
            "low",
            "close",
            "volume"
        ]:

            df[col] = pd.to_numeric(
                df[col]
            )


        return df