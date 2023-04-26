import streamlit as st
from streamlit_extras.switch_page_button import switch_page

from enums import Structure


def prompts():
    if "select" in st.session_state:
        select_structure()
    else:
        empty = st.empty()
        c = empty.container()
        c.header("What story do you want to create?")
        st.session_state.theme = c.text_area(
            "(describe your theme e. g. the storey about: love, money, grief, dreams etc.)",
            st.session_state.theme if "theme" in st.session_state else ""
        )
        c.header("Who is your main characters and what is his/her goal?")
        st.session_state.character = c.text_area(
            "(describe your Protagonist character and his purpose, what he wants, what he needs)",
            st.session_state.character if "character" in st.session_state else ""
        )
        c.header("Who is his/her antagonist? (optional)")
        st.session_state.antagonist = c.text_area(
            "(describe your main character's Antagonist and his goal, why he wants to stop our hero?)",
            st.session_state.antagonist if "antagonist" in st.session_state else ""
        )
        if c.button("Select structure"):
            empty.empty()
            st.session_state.select = True
            select_structure()


def select_structure():
    empty = st.empty()
    c = empty.container()
    c.header("Choose your story structure to create your story by AI")
    col1, col2, col3 = c.columns(3)
    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Square_1.svg/1200px-Square_1.svg.png")
        if st.button("Three-Act Structure", use_container_width=True):
            st.session_state.structure = True
            switch_page("Three-Act Structure")
    with col2:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Square_1.svg/1200px-Square_1.svg.png")
        if st.button("Hero's Journey", use_container_width=True):
            st.session_state.structure = True
            switch_page("Heros Journey")
    with col3:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Square_1.svg/1200px-Square_1.svg.png")
        if st.button("Save the cat", use_container_width=True):
            st.session_state.structure = True
            switch_page("Save the cat")
    c.markdown("###")
    if c.button("Go back"):
        empty.empty()
        del st.session_state["select"]
        prompts()
