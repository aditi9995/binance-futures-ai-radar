from src.radar.services.market_data import MarketDataService


class Scanner:

    def __init__(self):
        self.market = MarketDataService()

    def get_market(self):

        exchange = self.market.get_exchange_info()
        tickers = self.market.get_tickers()

        usdt_symbols = {
            s["symbol"]
            for s in exchange["symbols"]
            if s["quoteAsset"] == "USDT"
            and s["status"] == "TRADING"
            and s["contractType"] == "PERPETUAL"
        }

        rows = []

        for coin in tickers:

            if coin["symbol"] not in usdt_symbols:
                continue

            rows.append(
                {
                    "Symbol": coin["symbol"],
                    "Price": float(coin["lastPrice"]),
                    "24h %": float(coin["priceChangePercent"]),
                    "Volume": float(coin["quoteVolume"]),
                    "Trades": int(coin["count"]),
                }
            )

        rows.sort(
            key=lambda x: x["Volume"],
            reverse=True,
        )

        return rows