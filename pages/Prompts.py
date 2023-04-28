import streamlit as st
from streamlit_extras.switch_page_button import switch_page

import utils

utils.init_page()
utils.ensure_main_page_was_displayed()

c1, c2 = st.columns([1, 4])
c1.title("Story/scry AI")
c1.image("static/bg.jpeg")
if c1.button("Go back"):
    switch_page("streamlit_app")

c2.header("What story do you want to create? About what?")
st.session_state.theme = c2.text_area(
    "(describe your theme e. g. the storey about: love, money, grief, dreams etc2.)",
    st.session_state.theme if "theme" in st.session_state else ""
)
c2.header("Who is your main character?")
st.session_state.character = c2.text_area(
    "(describe your Protagonist character and his purpose, what he wants, what he needs)",
    st.session_state.character if "character" in st.session_state else ""
)
c2.header("What is his/her goal? (optional)")
st.session_state.goal = c2.text_area(
    "goal", st.session_state.goal if "goal" in st.session_state else "", label_visibility="collapsed"
)
c2.header("Who is his/her antagonist? (optional)")
st.session_state.antagonist = c2.text_area(
    "(describe your main character's Antagonist and his goal, why he wants to stop our hero?)",
    st.session_state.antagonist if "antagonist" in st.session_state else ""
)
if c2.button("Continue"):
    switch_page(st.session_state.structure)
