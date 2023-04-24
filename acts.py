from enum import Enum

import streamlit as st


class Structure(Enum):
    ThreeAct = "Three-act structure"
    HeroJourney = "Hero's Journey"
    SaveTheCat = "Save the cat"


def acts():
    empty = st.empty()
    c = empty.container()
    structure = st.session_state.structure
    c.header(structure.value)

    if structure == Structure.ThreeAct:
        with c.container():
            col1, col2 = st.columns(2)
            col1.markdown("#### ACT I")
            col2.text_area("Act I", label_visibility="collapsed", height=200)
            col1.markdown("#### Turning point 1")
            col2.columns(3)[1].button("Regenerate", "regen1", use_container_width=True)

        with c.container():
            col1, col2 = st.columns(2)
            col1.markdown("#### ACT II")
            col2.text_area("Act II", label_visibility="collapsed", height=250)
            col1.markdown("#### Mid-point")
            col1.markdown("#### Turning point 2")
            col2.columns(3)[1].button("Regenerate", "regen2", use_container_width=True)

        with c.container():
            col1, col2 = st.columns(2)
            col1.markdown("#### ACT III")
            col2.text_area("Act III", label_visibility="collapsed", height=200)
            col1.markdown("#### Climax")
            col2.columns(3)[1].button("Regenerate", "regen3", use_container_width=True)
    else:
        with c.container():
            col1, col2 = st.columns(2)
            col1.markdown("#### 1. The Ordinary World")
            col2.text_area("1", label_visibility="collapsed", height=100)
        with c.container():
            col1, col2 = st.columns(2)
            col1.markdown("#### 2. Call To Adventure")
            col2.text_area("2", label_visibility="collapsed", height=100)
