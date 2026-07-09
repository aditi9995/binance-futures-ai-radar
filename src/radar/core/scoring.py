"""
AI scoring model
"""


class AIScorer:


    def calculate(
        self,
        rvol,
        price_change,
        open_interest,
        funding
    ):


        score = 0

        reasons = []


        if rvol >= 4:

            score += 35

            reasons.append(
                "Extreme volume"
            )


        elif rvol >= 2:

            score += 25

            reasons.append(
                "High volume"
            )


        elif rvol >= 1.5:

            score += 15

            reasons.append(
                "Volume increase"
            )



        if price_change >= 3:

            score += 25

            reasons.append(
                "Strong momentum"
            )


        elif price_change >= 1:

            score += 15

            reasons.append(
                "Positive momentum"
            )



        if open_interest >= 500000:

            score += 25

            reasons.append(
                "High participation"
            )


        elif open_interest >= 100000:

            score += 15

            reasons.append(
                "Growing OI"
            )



        if abs(funding) < 0.0005:

            score += 15

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