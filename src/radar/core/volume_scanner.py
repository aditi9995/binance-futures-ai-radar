"""
Volume spike scanner.
Finds coins with unusual volume activity.
"""

from concurrent.futures import ThreadPoolExecutor, as_completed

from src.radar.services.market_data import MarketDataService
from src.radar.core.volume import VolumeAnalyzer


class VolumeScanner:

    def __init__(self):

        self.market = MarketDataService()
        self.analyzer = VolumeAnalyzer()

    
    def analyze_symbol(self, symbol):

        try:

            candles = self.market.get_klines(
                symbol,
                "5m",
                100
            )

            result = self.analyzer.calculate_rvol(
                candles
            )

            signal = self.analyzer.volume_signal(
                result
            )

            return {
                "Symbol": symbol,
                "RVOL": signal["rvol"],
                "Signal": signal["signal"]
            }


        except Exception:

            return None



    def scan(
        self,
        symbols,
        workers=10
    ):

        results = []


        with ThreadPoolExecutor(
            max_workers=workers
        ) as executor:


            tasks = [
                executor.submit(
                    self.analyze_symbol,
                    symbol
                )
                for symbol in symbols
            ]


            for task in as_completed(tasks):

                data = task.result()

                if data:
                    results.append(data)


        results.sort(
            key=lambda x: x["RVOL"],
            reverse=True
        )


        return results