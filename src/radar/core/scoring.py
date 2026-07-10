"""
Advanced AI Scoring Engine
"""


class AIScorer:


    def calculate(
        self,
        rvol,
        price_change,
        open_interest,
        funding,
        trend,
        breakout
    ):


        score = 0

        reasons = []



        # Volume

        if rvol >= 4:

            score += 30

            reasons.append(
                "Extreme volume spike"
            )


        elif rvol >= 2:

            score += 20

            reasons.append(
                "High volume"
            )


        elif rvol >= 1.5:

            score += 10

            reasons.append(
                "Increasing volume"
            )



        # Momentum

        if price_change >= 3:

            score += 20

            reasons.append(
                "Strong momentum"
            )


        elif price_change >= 1:

            score += 10

            reasons.append(
                "Positive momentum"
            )



        # Trend

        if trend == "BULLISH":

            score += 20

            reasons.append(
                "EMA trend bullish"
            )



        # Breakout

        if breakout:

            score += 20

            reasons.append(
                "Resistance breakout"
            )



        # Open interest

        if open_interest >= 500000:

            score += 10

            reasons.append(
                "High participation"
            )



        # Funding

        if abs(funding) < 0.0005:

            score += 5

            reasons.append(
                "Healthy funding"
            )



        return {

            "score": min(
                score,
                100
            ),

            "reasons": reasons

        }