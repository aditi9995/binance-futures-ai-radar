"""
Final AI Radar Engine
"""

from concurrent.futures import ThreadPoolExecutor, as_completed

from src.radar.services.market_data import MarketDataService
from src.radar.core.volume import VolumeAnalyzer
from src.radar.core.scoring import AIScorer
from src.radar.core.indicators import IndicatorEngine
from src.radar.core.risk import RiskManager



class RadarEngine:


    def __init__(self):

        self.market = MarketDataService()

        self.volume = VolumeAnalyzer()

        self.scorer = AIScorer()

        self.indicators = IndicatorEngine()

        self.risk = RiskManager()



    def analyze_coin(
        self,
        symbol
    ):

        try:


            candles = self.market.get_klines(
                symbol,
                "5m",
                250
            )



            candles = self.indicators.add_ema(
                candles
            )



            trend = self.indicators.trend(
                candles
            )



            breakout = self.indicators.breakout(
                candles
            )



            candles = self.volume.calculate_rvol(
                candles
            )



            volume_signal = self.volume.volume_signal(
                candles
            )



            current_price = candles.iloc[-1]["close"]



            price_change = (

                (
                    candles.iloc[-1]["close"]
                    -
                    candles.iloc[-2]["close"]
                )

                /

                candles.iloc[-2]["close"]

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

                funding=funding,

                trend=trend,

                breakout=breakout

            )



            # Minimum quality filter

            if ai["score"] < 50:

                return None



            trade = self.risk.calculate(

                price=current_price

            )



            return {


                "Symbol": symbol,


                "AI Score": ai["score"],


                "RVOL": round(
                    volume_signal["rvol"],
                    2
                ),


                "Price %": round(
                    price_change,
                    2
                ),


                "Trend": trend,


                "Breakout": breakout,


                "OI": round(
                    open_interest,
                    2
                ),


                "Funding": round(
                    funding,
                    6
                ),


                "Entry": trade["Entry"],


                "Stop Loss": trade["Stop Loss"],


                "Target 1": trade["Target 1"],


                "Target 2": trade["Target 2"],


                "Risk Reward": trade["Risk Reward"],


                "Signal": volume_signal["signal"],


                "Reasons": ", ".join(
                    ai["reasons"]
                )

            }



        except Exception as e:


            print(
                f"{symbol} ERROR:",
                e
            )


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


            futures = [

                executor.submit(
                    self.analyze_coin,
                    symbol
                )

                for symbol in symbols

            ]



            for future in as_completed(
                futures
            ):


                result = future.result()



                if result:

                    results.append(
                        result
                    )



        results.sort(

            key=lambda x: x["AI Score"],

            reverse=True

        )



        return results