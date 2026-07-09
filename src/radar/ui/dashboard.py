import pandas as pd
import streamlit as st
from streamlit_autorefresh import st_autorefresh

from src.radar.core.scanner import Scanner
from src.radar.ui.radar_view import show_radar


scanner = Scanner()


def run_dashboard():

    st_autorefresh(
        interval=60000,
        key="refresh"
    )


    st.title("🚀 Binance Futures AI Radar")


    tab1, tab2 = st.tabs(
        [
            "Market",
            "🔥 AI Radar"
        ]
    )


    with tab1:

        data = scanner.get_market()

        df = pd.DataFrame(data)

        st.dataframe(
            df,
            width="stretch",
            hide_index=True
        )


    with tab2:

        show_radar()