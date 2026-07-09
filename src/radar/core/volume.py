"""
Volume analysis engine.
Detects unusual volume activity.
"""

import pandas as pd


class VolumeAnalyzer:

    def __init__(
        self,
        lookback: int = 20
    ):
        self.lookback = lookback


    def calculate_rvol(
        self,
        df: pd.DataFrame
    ) -> pd.DataFrame:

        df = df.copy()

        df["avg_volume"] = (
            df["volume"]
            .rolling(self.lookback)
            .mean()
        )

        df["rvol"] = (
            df["volume"]
            /
            df["avg_volume"]
        )

        return df


    def volume_signal(
        self,
        df: pd.DataFrame
    ) -> dict:

        latest = df.iloc[-1]

        rvol = latest["rvol"]

        if rvol >= 3:
            signal = "EXTREME_VOLUME"

        elif rvol >= 2:
            signal = "HIGH_VOLUME"

        elif rvol >= 1.5:
            signal = "INCREASING_VOLUME"

        else:
            signal = "NORMAL"


        return {
            "rvol": round(float(rvol), 2),
            "signal": signal
        }