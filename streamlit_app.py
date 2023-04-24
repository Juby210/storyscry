import os

import ai21
import streamlit as st
from dotenv import load_dotenv
from streamlit_cookies_manager import CookieManager

from login import login, logout_button

st.set_page_config(page_title="Story/scry AI", initial_sidebar_state="collapsed")

load_dotenv()

st.session_state.cookies = CookieManager(prefix="ai21hackathon/")
if not st.session_state.cookies.ready():
    st.stop()

API_KEY = os.getenv("AI21_LABS_API_KEY")

ai21.api_key = API_KEY

st.title("Story/scry AI")

login()

if "user_email" in st.session_state:
    st.sidebar.write(f"Hello {st.session_state.user_email}")
    logout_button()
