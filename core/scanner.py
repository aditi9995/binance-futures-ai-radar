"""
Scanner.
"""

from services.binance_api import BinanceAPI


class Scanner:

    def __init__(self):

        self.api = BinanceAPI()

    def scan(self):

        return self.api.get_usdt_symbols()