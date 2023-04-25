import os

import ai21
import streamlit as st
from dotenv import load_dotenv
from streamlit_cookies_manager import CookieManager

from login import login


def init_page():
    st.set_page_config(page_title="Story/scry AI", layout="wide")
    st.sidebar.write(
        '<style>div[data-testid="stSidebarNav"]{visibility:hidden;height:4rem}</style>', unsafe_allow_html=True)

    load_dotenv()

    st.session_state.cookies = CookieManager(prefix="ai21hackathon/")
    if not st.session_state.cookies.ready():
        st.stop()

    if ai21.api_key is None:
        ai21.api_key = os.getenv("AI21_LABS_API_KEY")

    st.title("Story/scry AI")

    login()
