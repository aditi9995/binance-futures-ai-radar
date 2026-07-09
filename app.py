import streamlit as st

from src.radar.config.settings import settings
from src.radar.ui.dashboard import run_dashboard

st.set_page_config(
    page_title=settings.APP_NAME,
    layout="wide",
)

run_dashboard()