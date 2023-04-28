import streamlit as st
from streamlit_extras.switch_page_button import switch_page

import utils


def prompts():
    if "select" in st.session_state:
        select_structure()
    else:
        empty = st.empty()
        c = empty.container()
        c1, c2 = c.columns([1, 4])
        c1.title("Story/scry AI")
        c1.image("static/bg.jpeg")
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
        if c2.button("Select structure"):
            empty.empty()
            st.session_state.select = True
            select_structure()


def select_structure():
    empty = st.empty()
    c = empty.container()
    c.title("Story/scry AI")
    c.header("Choose your story structure to create your story by AI")
    col1, col2, col3 = c.columns(3)
    with col1:
        st.image("static/three-act.jpeg")
        if st.button("Three-Act Structure", use_container_width=True):
            st.session_state.structure = True
            switch_page("Three-Act Structure")
        st.write(utils.THREE_ACT_STRUCTURE_DESCRIPTION)
    with col2:
        st.image("static/heros-journey.jpeg")
        if st.button("Hero's Journey", use_container_width=True):
            st.session_state.structure = True
            switch_page("Heros Journey")
        st.write(utils.HEROS_JOURNEY_DESCRIPTION)
    with col3:
        st.image("static/save-the-cat.jpeg")
        if st.button("Save the cat", use_container_width=True):
            st.session_state.structure = True
            switch_page("Save the cat")
        st.write(utils.SAVE_THE_CAT_DESCRIPTION)
    c.write(
        "<style>img{border-radius:25%;height:17vw;max-width:20vw;}div[data-testid=stImage]{margin:0 auto}</style>",
        unsafe_allow_html=True
    )
    if c.button("Go back"):
        empty.empty()
        del st.session_state["select"]
        prompts()
