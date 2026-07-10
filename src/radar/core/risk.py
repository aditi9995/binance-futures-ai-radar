"""
Risk Management Engine
"""


class RiskManager:


    def calculate(
        self,
        price,
        atr=None
    ):


        if atr:

            stop_distance = atr * 1.5

        else:

            stop_distance = price * 0.015



        stop_loss = price - stop_distance


        target1 = price + (
            stop_distance * 2
        )


        target2 = price + (
            stop_distance * 3
        )


        risk_reward = round(
            (target1 - price)
            /
            (price - stop_loss),
            2
        )


        return {


            "Entry": round(
                price,
                8
            ),


            "Stop Loss": round(
                stop_loss,
                8
            ),


            "Target 1": round(
                target1,
                8
            ),


            "Target 2": round(
                target2,
                8
            ),


            "Risk Reward": risk_reward

        }