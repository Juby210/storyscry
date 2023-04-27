import ai21
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

from utils import init_page, gen_scenes_areas

init_page()

if "structure" not in st.session_state:
    switch_page("streamlit_app")

st.header("Save the cat")

# PROMPT = "Create a story using the structure below about:\n\n\n\nMain Character: " + st.session_state.character + "\n\nTheme: " + st.session_state.theme + "\n\nAntagonist: " + st.session_state.antagonist + "\n\n\n\nAct 1 / The Beginning\n\n\n\n1. Opening Image – A single scene beat that shows a “before” snapshot of the protagonist and the flawed world that he or she lives in.\n\n\n\n2. Theme Stated – A single scene beat in which a statement is made by someone (other than the protagonist) that hints at what the protagonist will learn before the end of the story.\n\n\n\n3. Setup – A multi-scene beat in which the reader gets to see what the protagonist’s life and the world are like–flaws and all. It’s also where important supporting characters and the protagonist’s initial goal (or the thing the protagonist thinks will fix his or her life) is introduced.\n\n\n\n4. Catalyst – A single scene beat in which a life-changing event happens to the protagonist and catapults him or her into a new world or a new way of thinking. In other words, after this moment, there’s no going back to the “normal world” introduced in the setup.\n\n\n\n5. Debate – A multi-scene beat where the protagonist debates what he or she will do next. Usually, there is some kind of question haunting them like, “should I do this?” or “should I do that?” The purpose of this beat is to show that the protagonist is reluctant to change for one reason or another.\n\n\n\n6. Break Into Two – A single scene beat in which the protagonist decides to accept the call to adventure, leave their comfort zone, try something new, or to venture into a new world or way of thinking. It’s the bridge between the beginning (Act 1) and middle (Act 2) of the story.\n\n\n\nWrite a treatment of Act 1 (use minimum 1000 characters) as in the structure above:\n\n\n\n###\n\n\n\nAct 2A / The Middle\n\n\n\n7. B Story – A single scene beat that introduces a new character or characters who will ultimately serve to help the hero learn the theme (or lesson) of the story. This character could be a love interest, a nemesis, a mentor, a family member, a friend, etc.\n\n\n\n8. Fun and Games – A multi-scene beat where the reader gets to see the protagonist either shinning or floundering in their new world. In other words, they are either loving their new world or hating it.\n\n\n\n9. Midpoint – A single scene beat where the fun and games section either culminates in a “false victory” (if your protagonist has been succeeding thus far) or a “false defeat” (if your protagonist has been floundering thus far) or a. In romance novels, this could be a kiss (or more), a declaration of love, or a marriage proposal. In a mystery or thriller, this could be a game-changing plot twist or a sudden ticking clock that ups the ante. This could even be a celebration or the first big public outing where the protagonist officially declares themselves a part of their new world. Whatever happens during this beat, it should raise the stakes and push the protagonist toward making a real change before moving forward.\n\n\n\nAct 2B / The Middle\n\n\n\n10. Bad Guys Close In – If the protagonist had a “false victory” at the Midpoint, this multi-scene beat would be a downward path where things get worse and worse for him or her. On the other hand, if the Midpoint was a “false defeat,” this section will be an upward path where things get better and better. Regardless of the path your protagonist takes during this multi-scene beat, his or her deep-rooted fear or false belief (their internal bad guys) and the antagonist (external bad guys) are closing in.\n\n\n\n11. All is Lost – A single scene beat where something happens, that when combined with the threat of the bad guys closing in, pushes your protagonist to their lowest point.\n\n\n\n12. Dark Night of the Soul – A multi-scene beat in which the protagonist takes time to process everything that’s happened so far. This is his or her darkest hour—the moment right before he or she figures out the solution to their big problem and learns the theme or life lesson of the story.\n\n\n\n13. Break Into Three (80%) – A single scene beat where the protagonist realizes what he or she must do to fix not only the external story problems but more importantly, their internal problems as well.\n\n\n\n###\n\n\n\nAct 3 / The End\n\n\n\n14. Finale – A multi-scene beat where the protagonist proves they have learned the story’s theme and acts on the plan he or she made in the Break Into Three scene. A great finale has five parts:\n\n\n\nA. Gathering the Team – The protagonist rounds up his or her friends, and gathers the tools, weapons, and supplies needed to execute the plan.\n\n\n\nB. Executing the Plan – The protagonist (and his or her crew) execute the plan. Sometimes secondary characters are sacrificed here in order to force the protagonist to continue forward on their own.\n\n\n\nC. The High Tower Surprise – The protagonist faces a twist or a surprise that forces him or her to prove their worth.\n\n\n\nD. Dig Deep Down – With no backup plan, the protagonist has to dig deep inside themselves to find the most important weapon of them all—the strength and courage to overcome their fear or false belief (internal antagonist) and face the antagonist or antagonistic force (external antagonist).\n\n\n\nE. Execution of New Plan – After the protagonist overcomes their fear or false belief (internal antagonist), he or she takes action against the antagonist or antagonistic force (external antagonist) and is successful. (If you’re writing a story where the protagonist isn’t successful, make sure there’s a point to their failure.)\n\n\n\n15. Final Image (99% to 100%) – A single scene beat that shows the reader an “after” snapshot of your protagonist’s life and how much he or she has changed since the beginning of the story.\n\n###\n\nAct 1 / The Beginning\n1. Opening Image:"
# if "output" not in st.session_state:
#     with st.spinner("Generating..."):
#         response = ai21.Completion.execute(
#             model="j2-jumbo-instruct",
#             prompt=PROMPT,
#             numResults=1,
#             maxTokens=1900,
#             minTokens=400,
#             stopSequences=["###"],
#             logitBias={"<|endoftext|>": -100.0}
#         )
#         st.session_state.output = "1. Opening Image: " + response.completions[0].data.text
#
# st.columns(3)[1].markdown("### Act 1 - The Beginning")
# split_by_act = st.session_state.output.split("Act 2A / The Middle")
# gen_scenes_areas(split_by_act[0], PROMPT)
#
# st.columns(3)[1].markdown("### Act 2A - The Middle (Part 1)")
# split_by_act = split_by_act[1].split("Act 2B / The Middle")
# gen_scenes_areas(split_by_act[0], PROMPT)
#
# st.columns(3)[1].markdown("### Act 2B - The Middle (Part 2)")
# split_by_act = split_by_act[1].split("Act 3 / The End")
# gen_scenes_areas(split_by_act[0], PROMPT)
#
# st.columns(3)[1].markdown("### Act 3 - The End")
# gen_scenes_areas(split_by_act[1], PROMPT)
#
# st.columns(3)[1].download_button("Export", "Act 1 / The Beginning:\n" + st.session_state.output, "export.txt", use_container_width=True)
