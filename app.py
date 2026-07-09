import streamlit as st

from core.scanner import Scanner

st.set_page_config(
    page_title="Binance Futures AI Radar",
    layout="wide"
)

st.title("🚀 Binance Futures AI Radar")

scanner = Scanner()

try:

    symbols = scanner.scan()

    st.success(f"Connected to Binance Futures")

    st.metric(
        "USDT Perpetual Contracts",
        len(symbols)
    )

    import pandas as pd

df = pd.DataFrame({"Symbol": symbols})

st.dataframe(
    df,
    width="stretch",
    height=600,
)

except Exception as ex:

    st.error(str(ex))