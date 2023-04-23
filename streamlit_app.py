import os

import ai21
import streamlit as st
from dotenv import load_dotenv

from login import login

load_dotenv()

API_KEY = os.getenv("AI21_LABS_API_KEY")

ai21.api_key = API_KEY

# Prompt for the model
PROMPT = "Based on the description given, name the sport.\nDescription: {description}\n Sport name: "

# Initialization of the output variable
if "output" not in st.session_state:
    st.session_state["output"] = "Output:"


def guess_sport(inp):
    if not len(inp):
        return None

    # overwrite the prompt with the description
    prompt = PROMPT.format(description=inp)

    response = ai21.Completion.execute(
        model="j2-grande-instruct",
        prompt=prompt,
        temperature=0.5,
        minTokens=1,
        maxTokens=15,
        numResults=1,
    )

    # return the name of the sport
    st.session_state["output"] = response.completions[0].data.text

    # a short celebration 😉
    st.balloons()


st.title("The Sports Guesser")

login()

if "user_email" in st.session_state:
    st.write(f"Hello {st.session_state.user_email}")

st.write(
    "This is a simple **Streamlit** app that generates Sport Name based on given description"
)

inp = st.text_area("Enter your description here", height=100)

st.button("Guess", on_click=guess_sport(inp))
st.write(f"Answer: {st.session_state.output}")
