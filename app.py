import pandas as pd
import streamlit as st

from src.radar.config.settings import settings
from src.radar.services.binance_api import BinanceAPI

st.set_page_config(
    page_title=settings.APP_NAME,
    layout="wide",
)

st.title("🚀 Binance Futures AI Radar")

api = BinanceAPI()

try:
    symbols = api.get_usdt_perpetual_symbols()

    st.success("Connected to Binance Futures")

    st.metric(
        "USDT Perpetual Contracts",
        len(symbols),
    )

    df = pd.DataFrame(
        {
            "Symbol": symbols,
        }
    )

    st.dataframe(
        df,
        width="stretch",
        height=600,
    )

except Exception as e:
    st.error(str(e))