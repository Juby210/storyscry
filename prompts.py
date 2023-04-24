import streamlit as st


def prompts():
    st.header("What story do you want to create?")
    st.text_area("(describe your theme e. g. the storey about: love, money, grief, dreams etc.)")
    st.header("Who is your main characters and what is his/her goal?")
    st.text_area("(describe your Protagonist character and his purpose, what he wants, what he needs)")
    st.header("Who is his/her antagonist? (optional)")
    st.text_area("(describe your main character's Antagonist and his goal, why he wants to stop our hero?)")
    st.button("Generate")
