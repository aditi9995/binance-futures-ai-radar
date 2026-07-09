"""
Final AI Radar Engine
"""

from concurrent.futures import ThreadPoolExecutor, as_completed

from src.radar.services.market_data import MarketDataService
from src.radar.core.volume import VolumeAnalyzer
from src.radar.core.scoring import AIScorer


class RadarEngine:

    def __init__(self):

        self.market = MarketDataService()
        self.volume = VolumeAnalyzer()
        self.scorer = AIScorer()


    def analyze_coin(self, symbol):

        try:

            candles = self.market.get_klines(
                symbol,
                "5m",
                100
            )

            candles = self.volume.calculate_rvol(
                candles
            )


            volume_signal = self.volume.volume_signal(
                candles
            )


            last = candles.iloc[-1]
            previous = candles.iloc[-2]


            price_change = (
                (last["close"] - previous["close"])
                /
                previous["close"]
            ) * 100



            open_interest = self.market.get_open_interest(
                symbol
            )


            funding = self.market.get_funding_rate(
                symbol
            )



            ai = self.scorer.calculate(
                rvol=volume_signal["rvol"],
                price_change=price_change,
                open_interest=open_interest,
                funding=funding
            )


            score = ai["score"]


            # Quality filter
            if score < 50:
                return None


            if volume_signal["rvol"] < 1.3:
                return None



            return {

                "Symbol": symbol,

                "AI Score": score,

                "RVOL": round(
                    volume_signal["rvol"],
                    2
                ),

                "Price %": round(
                    price_change,
                    2
                ),

                "Open Interest": round(
                    open_interest,
                    2
                ),

                "Funding": round(
                    funding,
                    6
                ),

                "Signal": volume_signal["signal"],

                "Reasons": ", ".join(
                    ai["reasons"]
                )

            }


        except Exception:

            return None



    def scan(
        self,
        symbols,
        workers=15
    ):

        results = []


        with ThreadPoolExecutor(
            max_workers=workers
        ) as executor:


            futures = [

                executor.submit(
                    self.analyze_coin,
                    symbol
                )

                for symbol in symbols

            ]


            for future in as_completed(futures):

                result = future.result()

                if result:
                    results.append(result)



        results.sort(
            key=lambda x: x["AI Score"],
            reverse=True
        )


        return results