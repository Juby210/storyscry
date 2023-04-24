import os

import ai21
import streamlit as st
from dotenv import load_dotenv
from streamlit_cookies_manager import CookieManager

from login import login
from prompts import prompts

st.set_page_config(page_title="Story/scry AI")

load_dotenv()

st.session_state.cookies = CookieManager(prefix="ai21hackathon/")
if not st.session_state.cookies.ready():
    st.stop()

API_KEY = os.getenv("AI21_LABS_API_KEY")

ai21.api_key = API_KEY

st.title("Story/scry AI")

login()

if "user_email" in st.session_state:
    if "prompts" in st.session_state:
        prompts()
    else:
        st.header("Choose your story structure to create your story by AI")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Square_1.svg/1200px-Square_1.svg.png")
            if st.button("Three-act structure", use_container_width=True):
                st.session_state.prompts = 0
                st.experimental_rerun()
        with col2:
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Square_1.svg/1200px-Square_1.svg.png")
            if st.button("Hero's Journey", use_container_width=True):
                st.session_state.prompts = 1
                st.experimental_rerun()
        with col3:
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Square_1.svg/1200px-Square_1.svg.png")
            if st.button("Save the cat", use_container_width=True):
                st.session_state.prompts = 2
                st.experimental_rerun()
