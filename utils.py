import os
import re

import ai21
import streamlit as st
from dotenv import load_dotenv
from streamlit_cookies_manager import CookieManager

from login import login


def init_page():
    st.set_page_config(page_title="Story/scry AI", layout="wide")
    st.sidebar.write(
        '<style>div[data-testid="stSidebarNav"]{visibility:hidden;height:4rem}</style>', unsafe_allow_html=True)

    load_dotenv()

    st.session_state.cookies = CookieManager(prefix="ai21hackathon/")
    if not st.session_state.cookies.ready():
        st.stop()

    ai21.timeout_sec = 120
    if ai21.api_key is None:
        ai21.api_key = os.getenv("AI21_LABS_API_KEY")

    st.title("Story/scry AI")

    login()


def gen_scenes_areas(text, prompt):
    scenes = re.findall(r'\d?\d\. .+?:', text)
    for i in range(len(scenes)):
        with st.container():
            col1, col2, col3 = st.columns([1, 1, 2])
            scene = scenes[i]
            scene2 = scene[:-1]
            col1.markdown("#### " + scene2)

            val = text.split(scene)[1].strip()
            if i < len(scenes) - 1:
                val = val.split(scenes[i + 1])[0]
            if col2.button("Regenerate", "regen " + scene2, use_container_width=True):
                val = regen_scene(prompt, scene2, val)

            col2.button("Create scenes", "create " + scene2, use_container_width=True)
            col3.text_area(scene2, label_visibility="collapsed", height=150, value=val)


def regen_scene(prompt, scene, original):
    response = ai21.Completion.execute(
        model="j2-grande-instruct",
        prompt=prompt + st.session_state.output + "\n\nRegenerate \"" + scene + "\", create something new but connected with the whole story structure:",
        numResults=1,
        maxTokens=1000,
        minTokens=50,
    )
    st.session_state.output = st.session_state.output.replace(original, response.completions[0].data.text + "\n\n", 1)
    return response.completions[0].data.text.strip()
