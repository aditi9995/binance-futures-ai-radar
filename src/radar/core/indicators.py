"""
Technical Indicators Engine
"""

import pandas as pd


class IndicatorEngine:


    def add_ema(
        self,
        df: pd.DataFrame
    ):

        df = df.copy()

        df["EMA20"] = (
            df["close"]
            .ewm(span=20)
            .mean()
        )

        df["EMA50"] = (
            df["close"]
            .ewm(span=50)
            .mean()
        )

        df["EMA200"] = (
            df["close"]
            .ewm(span=200)
            .mean()
        )

        return df



    def trend(
        self,
        df
    ):

        last = df.iloc[-1]


        if (
            last["EMA20"] >
            last["EMA50"] >
            last["EMA200"]
        ):

            return "BULLISH"


        elif (
            last["EMA20"] <
            last["EMA50"] <
            last["EMA200"]
        ):

            return "BEARISH"


        return "NEUTRAL"



    def breakout(
        self,
        df,
        lookback=20
    ):

        previous_high = (
            df["high"]
            .iloc[-lookback:-1]
            .max()
        )


        current_price = (
            df["close"]
            .iloc[-1]
        )


        if current_price > previous_high:

            return True


        return False