import os
import re

import ai21
import streamlit as st
from dotenv import load_dotenv
from streamlit_cookies_manager import CookieManager
from streamlit_extras.switch_page_button import switch_page

from login import login


THREE_ACT_STRUCTURE_DESCRIPTION = "A story framework with beginning (Setup), middle (Confrontation), and end " \
                                  "(Resolution) for character development and plot growth."
HEROS_JOURNEY_DESCRIPTION = "A 17-stage monomyth with a protagonist's transformative adventure, challenges, " \
                            "and return with wisdom."
SAVE_THE_CAT_DESCRIPTION = "A 15-beat structure focusing on character arcs, emotional connection, and key moments for " \
                           "compelling stories."

def init_page(subpage=None, desc=None, img=None):
    st.set_page_config(page_title="Story/scry AI", layout="wide")
    # Hack, hides default navbar from the sidebar
    st.sidebar.write(
        '<style>div[data-testid="stSidebarNav"]{visibility:hidden;height:4rem}</style>', unsafe_allow_html=True)

    load_dotenv()

    st.session_state.cookies = CookieManager(prefix="ai21hackathon/")
    if not st.session_state.cookies.ready():
        st.stop()

    ai21.timeout_sec = 120
    if ai21.api_key is None:
        ai21.api_key = os.getenv("AI21_LABS_API_KEY")

    if subpage is None:
        st.title("Story/scry AI")
    else:
        col1, col2, col3 = st.columns([2, 2, 1])
        col1.title("Story/scry AI")
        col1.write("<style>img{border-radius:22%}</style>", unsafe_allow_html=True)
        col2.title(subpage)
        col2.write(desc)
        col3.image("static/"+img+".jpeg")

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


# ensures that the user already provided data in main page prompts, if no goes back to main page
def ensure_main_page_was_displayed():
    if "structure" not in st.session_state:
        switch_page("streamlit_app")


def export_button(prefix=""):
    st.columns(3)[1].download_button("Export", prefix + st.session_state.output, "export.txt", use_container_width=True)
