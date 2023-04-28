import ai21
import streamlit as st

import utils

utils.init_page()
utils.ensure_main_page_was_displayed()

st.header("Three-Act Structure")

PROMPT = "The first act, or opening narration, is usually used for exposition, to establish the main characters, their relationships, and the world they live in. Later in the first act, a dynamic incident occurs, known as the inciting incident, or catalyst, that confronts the main character (the protagonist). The protagonist's attempts to deal with this incident lead to a second and more dramatic situation, known as the first plot point, which (a) signals the end of the first act, (b) ensures life will never be the same again for the protagonist and raises a dramatic question that will be answered in the climax of the film. The dramatic question should be framed in terms of the protagonist's call to action, (Will X recover the diamond? Will Y get the girl? Will Z capture the killer?).\n\nThe second act, also referred to as rising action, typically depicts the protagonist's attempt to resolve the problem initiated by the first turning point, only to find themselves in ever worsening situations. Part of the reason protagonists seem unable to resolve their problems is because they do not yet have the skills to deal with the forces of antagonism that confront them. They must not only learn new skills but arrive at a higher sense of awareness of who they are and what they are capable of, in order to deal with their predicament, which in turn changes who they are. This is referred to as character development or a character arc. This cannot be achieved alone and they are usually aided and abetted by mentors and co-protagonists.\n\nThe third act features the resolution of the story and its subplots. The climax is the scene or sequence in which the main tensions of the story are brought to their most intense point and the dramatic question answered, leaving the protagonist and other characters with a new sense of who they really are.\n\nWrite a story in the \"Three act structure\" described above about:\n\nMain Character: [" + st.session_state.character + "]\nTheme: [" + st.session_state.theme + "]\nAntagonist: [" + st.session_state.antagonist + "]\n\nProvide turning points in the end of ACT 1 and ACT 2. Create the middle point in the middle of the ACT 2. Create Climax point in the end of ACT 3. \nName every of this point above in the bracket in it's Act.\n\nMark all points of the story. \nWrite a full story treatment using this structure above, use minimum 500 words per Act:\nAct 1:\n"


def act_container(act_number, val):
    col1, col2 = st.columns(2)
    col1.markdown("#### ACT " + act_number)
    text_area_cont = col2.container()
    _, c2, c3 = col2.columns(3)
    if c2.button("Regenerate", "regen " + act_number, use_container_width=True):
        val = utils.regen_scene(PROMPT, "Act " + act_number, val)
    c3.button("Create scenes", "create " + act_number, use_container_width=True)
    text_area_cont.text_area("Act " + act_number, label_visibility="collapsed", height=200, value=val)


if "output" not in st.session_state:
    with st.spinner("Generating..."):
        response = ai21.Completion.execute(
            model="j2-jumbo-instruct",
            prompt=PROMPT,
            numResults=1,
            maxTokens=5000,
            minTokens=200,
        )
        st.session_state.output = response.completions[0].data.text

split_by_act = st.session_state.output.split("Act 2:")
act_container("I", split_by_act[0].strip())
split_by_act = split_by_act[1].split("Act 3:")
act_container("II", split_by_act[0].strip())
act_container("III", split_by_act[1].strip())

utils.export_button("Act 1:\n")
