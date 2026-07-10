import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))


from src.radar.alerts.alert_engine import AlertEngine


data = [

    {
        "Symbol":"BTCUSDT",
        "AI Score":85,
        "Reasons":"High volume"
    },

    {
        "Symbol":"ETHUSDT",
        "AI Score":40,
        "Reasons":"Weak"
    }

]


engine = AlertEngine()


alerts = engine.check(data)


for alert in alerts:
    print(alert)