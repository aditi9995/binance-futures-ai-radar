import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))


from src.radar.services.market_data import MarketDataService
from src.radar.core.volume import VolumeAnalyzer


service = MarketDataService()


candles = service.get_klines(
    "BTCUSDT",
    "5m",
    100
)


analyzer = VolumeAnalyzer()


result = analyzer.calculate_rvol(
    candles
)


signal = analyzer.volume_signal(
    result
)


print(signal)