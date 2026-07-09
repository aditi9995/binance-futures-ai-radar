import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))


from src.radar.services.binance_api import BinanceAPI
from src.radar.core.radar import RadarEngine


api = BinanceAPI()

symbols = api.get_usdt_perpetual_symbols()


radar = RadarEngine()


results = radar.scan(
    symbols[:50]
)


for r in results[:10]:
    print(r)