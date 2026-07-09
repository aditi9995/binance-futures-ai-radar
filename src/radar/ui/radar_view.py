import pandas as pd
import streamlit as st

from src.radar.services.binance_api import BinanceAPI
from src.radar.core.radar import RadarEngine



def show_radar():

    st.header(
        "🔥 AI Radar - High Probability Setups"
    )


    api = BinanceAPI()

    radar = RadarEngine()


    symbols = api.get_usdt_perpetual_symbols()


    with st.spinner(
        "Scanning futures market..."
    ):

        results = radar.scan(
            symbols
        )


    if not results:

        st.warning(
            "No strong setups found"
        )

        return



    df = pd.DataFrame(
        results
    )


    st.metric(
        "Signals Found",
        len(df)
    )


    st.dataframe(
        df.head(50),
        width="stretch",
        hide_index=True
    )