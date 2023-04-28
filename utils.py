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
SAVE_THE_CAT_DESCRIPTION = "A 15-beat structure focusing on character arcs, emotional connection, and key moments for" \
                           " compelling stories."


def init_page(subpage=None, desc=None, img=None):
    st.set_page_config(page_title="Story/scry AI", layout="wide", initial_sidebar_state="collapsed")
    # Hack, hides default navbar from the sidebar
    st.sidebar.write(
        '<style>div[data-testid="stSidebarNav"]{visibility:hidden;height:4rem}</style>', unsafe_allow_html=True)

    load_dotenv()

    st.session_state.cookies = CookieManager(prefix="storyscry/")
    if not st.session_state.cookies.ready():
        st.stop()

    ai21.timeout_sec = 120
    if ai21.api_key is None:
        ai21.api_key = os.getenv("AI21_LABS_API_KEY")

    if subpage is not None:
        col1, col2, col3 = st.columns([1, 2, 1])
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
            if col2.button("Create scenes", "create " + scene2, use_container_width=True):
                val = create_scenes(scene2, val)

            col3.text_area(scene2, label_visibility="collapsed", height=150, value=val)


def regen_scene(prompt, scene, original):
    response = ai21.Completion.execute(
        model="j2-grande-instruct",
        prompt=prompt + st.session_state.output + "\n\nRegenerate \"" + scene + "\", create something new but connected with the whole story structure:",
        numResults=1,
        maxTokens=1000,
        minTokens=50,
    )
    new = response.completions[0].data.text
    st.session_state.output = st.session_state.output.replace(original, new + "\n\n", 1)
    return new.strip()


def create_scenes(name, original):
    response = ai21.Completion.execute(
        model="j2-grande-instruct",
        prompt="Here is our story:\n\n" + st.session_state.output + "\n\nAnd now a description of the Fountain format: The Fountain format is a plain text markup language that uses specific syntax to indicate elements of a screenplay, such as scene headings, dialogue, and action. Here's an example of how you can prompt a scene in the Fountain format:\n\nINT. COFFEE SHOP - DAY\n\nJACK, a disheveled writer, sits at a table, staring at his laptop. He takes a sip of coffee and sighs.\n\nJACK\n(to himself)\nI can't do this. I'm never going to finish this screenplay.\n\nSuddenly, a beautiful woman, JILL, walks into the coffee shop. Jack's eyes light up.\n\nJILL\n(smiling)\nMind if I join you?\n\nJack nods, speechless.\n\nAs Jill sits down, Jack's laptop screen glows with inspiration. In this example, the scene heading \"INT. COFFEE SHOP - DAY\" indicates the location and time of the scene. The action lines describe Jack's behavior and thoughts, while the dialogue lines show his conversation with Jill. This scene in the fountain format was only the example of the format, don't remember the story only a format, our story is above that scene fragment.\n\n\nNow generate in the Fountain format three film scenes with dialogues, for \"" + name + "\" part:",
        numResults=1,
        maxTokens=1000,
        minTokens=50,
    )
    new = original + response.completions[0].data.text
    st.session_state.output = st.session_state.output.replace(original, new + "\n\n", 1)
    return new.strip()


# ensures that the user already provided data in main page prompts, if no goes back to main page
def ensure_main_page_was_displayed():
    if "structure" not in st.session_state:
        switch_page("streamlit_app")


def footer(export_prefix=""):
    col1, col2, _ = st.columns(3)
    col2.download_button("Export", export_prefix + st.session_state.output, "export.txt", use_container_width=True)
    if col1.button("Go back"):
        del st.session_state["output"]
        switch_page("Prompts")
