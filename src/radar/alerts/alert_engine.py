"""
Alert Engine
"""

from datetime import datetime


class AlertEngine:


    def __init__(
        self,
        minimum_score=70
    ):

        self.minimum_score = minimum_score



    def check(
        self,
        results
    ):

        alerts = []


        for coin in results:


            if coin["AI Score"] >= self.minimum_score:


                alerts.append({

                    "Symbol": coin["Symbol"],

                    "Score": coin["AI Score"],

                    "Reason": coin["Reasons"],

                    "Time": datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )

                })


        return alerts