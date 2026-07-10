import pandas as pd
import streamlit as st
from datetime import datetime

from src.radar.services.binance_api import BinanceAPI
from src.radar.core.radar import RadarEngine
from src.radar.alerts.alert_engine import AlertEngine
from src.radar.alerts.storage import AlertStorage


@st.cache_data(ttl=120)
def run_radar_scan():

    api = BinanceAPI()

    radar = RadarEngine()

    symbols = api.get_usdt_perpetual_symbols()


    results = radar.scan(
        symbols
    )


    return results



def show_radar():

    st.header(
        "🔥 AI Radar - High Probability Setups"
    )


    col1, col2 = st.columns(2)


    with col1:

        scan_button = st.button(
            "🔄 Scan Now"
        )


    with col2:

        st.write(
            "Cache: 2 minutes"
        )


    if scan_button:

        st.cache_data.clear()



    with st.spinner(
        "Loading radar..."
    ):

        results = run_radar_scan()



    if not results:

        st.warning(
            "No setups found"
        )

        return



    df = pd.DataFrame(
        results
    )


    st.success(
        f"Last update: {datetime.now().strftime('%H:%M:%S')}"
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



    alert_engine = AlertEngine()

    storage = AlertStorage()


    alerts = alert_engine.check(
        results
    )


    storage.save(
        alerts
    )


    st.subheader(
        "🚨 Active Alerts"
    )


    if alerts:

        st.dataframe(
            pd.DataFrame(alerts),
            width="stretch",
            hide_index=True
        )

    else:

        st.info(
            "No alerts"
        )