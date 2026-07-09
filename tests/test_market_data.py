import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))


from src.radar.services.market_data import MarketDataService


service = MarketDataService()


data = service.get_klines(
    "BTCUSDT",
    "5m",
    100
)


print(data.tail())