import streamlit as st
from streamlit_extras.switch_page_button import switch_page

import utils

utils.init_page()

if "user_email" in st.session_state:
    st.title("Story/scry AI")
    st.header("Choose your story structure to create your story by AI")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("static/three-act.jpeg")
        if st.button("Three-Act Structure", use_container_width=True):
            st.session_state.structure = "Three-Act Structure"
            switch_page("Prompts")
        st.write(utils.THREE_ACT_STRUCTURE_DESCRIPTION)
    with col2:
        st.image("static/heros-journey.jpeg")
        if st.button("Hero's Journey", use_container_width=True):
            st.session_state.structure = "Heros Journey"
            switch_page("Prompts")
        st.write(utils.HEROS_JOURNEY_DESCRIPTION)
    with col3:
        st.image("static/save-the-cat.jpeg")
        if st.button("Save the cat", use_container_width=True):
            st.session_state.structure = "Save the cat"
            switch_page("Prompts")
        st.write(utils.SAVE_THE_CAT_DESCRIPTION)
    st.write(
        "<style>img{border-radius:25%;height:17vw;max-width:20vw;}div[data-testid=stImage]{margin:0 auto}</style>",
        unsafe_allow_html=True
    )
