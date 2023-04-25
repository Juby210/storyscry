import streamlit as st

from prompts import prompts
from utils import init_page

init_page()

if "user_email" in st.session_state:
    prompts()
