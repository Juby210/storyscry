import streamlit as st
from streamlit_extras.switch_page_button import switch_page

from utils import init_page

init_page()

if "structure" not in st.session_state:
    switch_page("streamlit_app")

st.header("Save the cat")
