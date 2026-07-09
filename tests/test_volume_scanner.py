import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))


from src.radar.services.binance_api import BinanceAPI
from src.radar.core.volume_scanner import VolumeScanner


api = BinanceAPI()

symbols = api.get_usdt_perpetual_symbols()


scanner = VolumeScanner()


results = scanner.scan(
    symbols[:50]
)


for item in results[:10]:
    print(item)