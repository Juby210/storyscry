import ai21
import streamlit as st

import utils

utils.init_page("Save the cat", utils.SAVE_THE_CAT_DESCRIPTION, "save-the-cat")
utils.ensure_main_page_was_displayed()

PROMPT = "Please help me create a screenplay full length treatment using the Save the Cat structure. \n\nThe story is about: \n\nMain Character: " + st.session_state.character + "\nTheme: " + st.session_state.theme + "\nAntagonist: " + st.session_state.antagonist + "\n\nConsider the following elements while creating the outline:\n\nAct 1 / The Beginning\n1. Opening Image – A single scene beat that shows a “before” snapshot of the protagonist and the flawed world that he or she lives in.\n2. Theme Stated – A single scene beat in which a statement is made by someone (other than the protagonist) that hints at what the protagonist will learn before the end of the story.\n3. Setup – A multi-scene beat in which the reader gets to see what the protagonist’s life and the world are like–flaws and all. It’s also where important supporting characters and the protagonist’s initial goal (or the thing the protagonist thinks will fix his or her life) is introduced.\n4. Catalyst – A single scene beat in which a life-changing event happens to the protagonist and catapults him or her into a new world or a new way of thinking. In other words, after this moment, there’s no going back to the “normal world” introduced in the setup.\n5. Debate – A multi-scene beat where the protagonist debates what he or she will do next. Usually, there is some kind of question haunting them like, “should I do this?” or “should I do that?” The purpose of this beat is to show that the protagonist is reluctant to change for one reason or another.\n6. Break Into Two – A single scene beat in which the protagonist decides to accept the call to adventure, leave their comfort zone, try something new, or to venture into a new world or way of thinking. It’s the bridge between the beginning (Act 1) and middle (Act 2) of the story. Act 2A / The Middle (Part 1)\n7. B Story – A single scene beat that introduces a new character or characters who will ultimately serve to help the hero learn the theme (or lesson) of the story. This character could be a love interest, a nemesis, a mentor, a family member, a friend, etc.\n8. Fun and Games – A multi-scene beat where the reader gets to see the protagonist either shinning or floundering in their new world. In other words, they are either loving their new world or hating it.\n9. Midpoint – A single scene beat where the fun and games section either culminates in a “false victory” (if your protagonist has been succeeding thus far) or a “false defeat” (if your protagonist has been floundering thus far) or a. In romance novels, this could be a kiss (or more), a declaration of love, or a marriage proposal. In a mystery or thriller, this could be a game-changing plot twist or a sudden ticking clock that ups the ante. This could even be a celebration or the first big public outing where the protagonist officially declares themselves a part of their new world. Whatever happens during this beat, it should raise the stakes and push the protagonist toward making a real change before moving forward.\n\nAct 2B / The Middle (Part 2)\n10. Bad Guys Close In – If the protagonist had a “false victory” at the Midpoint, this multi-scene beat would be a downward path where things get worse and worse for him or her. On the other hand, if the Midpoint was a “false defeat,” this section will be an upward path where things get better and better. Regardless of the path your protagonist takes during this multi-scene beat, his or her deep-rooted fear or false belief (their internal bad guys) and the antagonist (external bad guys) are closing in.\n11. All is Lost – A single scene beat where something happens, that when combined with the threat of the bad guys closing in, pushes your protagonist to their lowest point.\n12. Dark Night of the Soul – A multi-scene beat in which the protagonist takes time to process everything that’s happened so far. This is his or her darkest hour—the moment right before he or she figures out the solution to their big problem and learns the theme or life lesson of the story.\n13. Break Into Three – A single scene beat where the protagonist realizes what he or she must do to fix not only the external story problems but more importantly, their internal problems as well.\n\nAct 3 / The End\n14. Finale – A multi-scene beat where the protagonist proves they have learned the story’s theme and acts on the plan he or she made in the Break Into Three scene. A great finale has five parts:\nA. Gathering the Team – The protagonist rounds up his or her friends, and gathers the tools, weapons, and supplies needed to execute the plan.\nB. Executing the Plan – The protagonist (and his or her crew) execute the plan. Sometimes secondary characters are sacrificed here in order to force the protagonist to continue forward on their own.\nC. The High Tower Surprise – The protagonist faces a twist or a surprise that forces him or her to prove their worth.\nD. Dig Deep Down – With no backup plan, the protagonist has to dig deep inside themselves to find the most important weapon of them all—the strength and courage to overcome their fear or false belief (internal antagonist) and face the antagonist or antagonistic force (external antagonist).\nE. Execution of New Plan – After the protagonist overcomes their fear or false belief (internal antagonist), he or she takes action against the antagonist or antagonistic force (external antagonist) and is successful. (If you’re writing a story where the protagonist isn’t successful, make sure there’s a point to their failure.)\n15. Final Image – A single scene beat that shows the reader an “after” snapshot of your protagonist’s life and how much he or she has changed since the beginning of the story.\n\n\nPlease ensure that the outline is detailed, engaging, and adheres to the Save the Cat structure. Create a unique story using the Save the Cat structure, ensuring that each act is detailed and engaging. In your response, provide the title of the story and outline the plot for each act. Remember to be creative, specific, and prompt in crafting the narrative to maintain the same structure throughout:\nAct 1 / The Beginning:\n1. Opening Image:"

if "output" not in st.session_state:
    with st.spinner("Generating..."):
        response = ai21.Completion.execute(
            model="j2-jumbo-instruct",
            prompt=PROMPT,
            numResults=1,
            maxTokens=2000,
            minTokens=400,
        )
        st.session_state.output = "Act 1 / The Beginning:\n1. Opening Image:" + response.completions[0].data.text

st.columns(3)[1].markdown("### Act 1 - The Beginning")
split_by_act = st.session_state.output.split("Act 2A / The Middle")
utils.gen_scenes_areas(split_by_act[0], PROMPT)

st.columns(3)[1].markdown("### Act 2A - The Middle (Part 1)")
split_by_act = split_by_act[1].split("Act 2B / The Middle")
utils.gen_scenes_areas(split_by_act[0], PROMPT)

st.columns(3)[1].markdown("### Act 2B - The Middle (Part 2)")
split_by_act = split_by_act[1].split("Act 3 / The End")
utils.gen_scenes_areas(split_by_act[0], PROMPT)

st.columns(3)[1].markdown("### Act 3 - The End")
utils.gen_scenes_areas(split_by_act[1], PROMPT)

utils.export_button()
