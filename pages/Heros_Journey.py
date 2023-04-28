import ai21
import streamlit as st

import utils

utils.init_page("Hero's Journey", utils.HEROS_JOURNEY_DESCRIPTION, "heros-journey")
utils.ensure_main_page_was_displayed()

PROMPT = "Here is the Hero's Journey structure\n\n1. The Ordinary World: The story starts with the hero's normal life before they go on an adventure.\n\nIntroduce {character} homeland\n\n>Make parallels from {character} world to today’s modern society\n\n>Give me more details about {character} home life and community \n\n>Who is {character} really? \n\n>What are {character} capabilities? \n\n>What are {character} flaws? \n\n>What are their outlooks on life?\n\n>What does {character} stand for?\n\n>What does {character} stand against?\n\n>What does {character} desire?\n\n***\n\n2. Call to Adventure: The hero is confronted with an occurrence, conflict, problem, or tension that compels them to embark on their journey.\n\n>What was {character} call to action? \n\n>What was {character} pain?\n\n>What elements of {character} world were disrupted and presented a challenge or quest?\n\n***\n\n3. Refusal of the Call: The hero initially refuses the adventure because of hesitation, fears, insecurity, or any other number of issues.\n\n>What fears and personal doubts held {character} back that needed to be overcome?\n\n>What event happens to {character} that pushes them over the edge and allows them to bet on themself and realize that not acting will cause further harm to their world?\n\n***\n\n4. Meeting the Mentor: A mentor, often an individual who has previously completed the trek or a legendary figure, may assist the protagonist in this manner.\n\n>Who is {character} mentor? \n\n>What is the mentor's motivation to train {character}? \n\n>What does their mentor represent? \n\n>What did the mentor give {character} to help on their journey?\n\n***\n\n5. Crossing the Threshold: The protagonist departs from their regular existence for the first time and enters into a new realm of danger.\n\n>Does {character} start willingly or are they pushed by an outside force?\n\n>What does the threshold represent? \n\n>What is it like when {character} crosses over to the other side?\n\n>What is this new world like? \n\n***\n\n6. Tests, Allies, and Enemies: The hero learns the rules of the new world and faces trials, encounters friends, and meets foes.\n\n>What is {character} first challenge? \n\n>What are some new challenges {character} is faced with?\n\n>What new skills did {character} learn because of the challenges? \n\n>What does this new adventure mean for {character}? \n\n>What new tools did {character} learn to use? \n\n>What new allies does {character} meet?\n\n>What new enemies do they meet?\n\n>How has {character} training and sense of purpose helped {character} overcome them? \n\n>How does this give {character} a deeper understanding into who they truly are and what they are capable of?\n\n7. Approach To The Inmost Cave:The hero's initial plan to tackle the main conflict begins, but difficulties crop up that cause him to try a new strategy or embrace new concepts.\n\n>What attempt does {character} make to prove themself and fail?\n\n>What does {character} struggle with internally?\n\n>What does {character} struggle with externally? \n\n>What does {character} struggle with philosophically? \n\n***\n\n8. The Ordeal: Things begin to go wrong and new friction is introduced. The hero faces greater challenges and barriers, some of which may be life-changing.\n\n>What is {character} supreme ordeal?\n\n>What skill does {character} need to draw on to overcome this challenge?\n\n>What happens if {character} fails?\n\n***\n\n9. The Reward: The hero receives a reward after surviving The Ordeal that allows them to take on the most difficult challenge. It might be a tangible item, piece of knowledge, or wisdom that will aid them in their efforts.\n\n>What reward does {character} receive after overcoming their greatest challenge?\n\n>Who does {character} transform into after overcoming their greatest challenge?\n\n***\n\n10. The Road Back: The protagonist is at the verge of achieving his or her goal, but they are about to face even more tests and obstacles.\n\n>What does {character} return home look like?\n\n>What is {character} road back like? \n\n>How does {character} journey continue?\n\n>What is {character} final commitment?\n\n>What is {character} higher cause?\n\n***\n\n11. The Resurrection: The final event. The hero is put to the ultimate test, using everything they've learned to conquer the struggle once and for all.\n\n>What is {character} final and most dangerous battle?\n\n>What happens if {character} fails?\n\n>What are the far-reaching consequences to {character} ordinary world?\n\n***\n\n12. The Return: The hero is returned to the regular world with their knowledge or \"elixir.\"\n\n>What is {character} return with the elixir?\n\n>Who has {character} changed into?\n\n>What is {character} cause for celebration, self-realization, or an end to strife?\n\n>What is {character} resolution?\n\nThe hero returns with the elixir of knowledge, understanding, and the power to make a difference in their world. They have become more confident, compassionate, and wise from their journey. The return is cause for celebration among their peers as they can now use this newfound wisdom to help others and work towards lasting solutions to problems that have plagued them. The resolution is that the hero has found their true purpose and can use their knowledge to make a real difference in the world. They have achieved clarity, understanding, and an inner peace that will stay with them forever. They are now able to embrace the beauty of life and understand that despite any obstacles, there is always a chance to create something better for themselves and for others. The hero has become an inspiration for all who seek knowledge and truth. \n\nThey have solved the mystery, passed their tests, and found the power within them to make a lasting difference. The journey has not been easy, but it was worth every risky step taken. This hero is an example of the strength and courage that lies within us all and a reminder to never give up, no matter how difficult the task may seem. They have shown us that we can make a difference if we choose to take action, find our true purpose, and commit to achieving our goals. We can all be heroes in our own way if we have the courage to pursue our dreams and never stop believing in ourselves. With dedication, hard work, and a little bit of luck, anything is possible. So take your first steps towards greatness and become the hero you always wanted to be! \n\nBe daring and courageous. Be strong-willed and determined. You may not know where the journey will lead you, but with faith in yourself, you’ll make it through whatever obstacles come your way. Take a chance on new opportunities that arise; it may just be the start of something special for you. Live adventurously; find purpose in life’s challenges; \n\nWrite a story in above structure, about:\n\n{Character}: " + st.session_state.character + "\n{Character}'s goal: " + st.session_state.goal + "\nTheme: " + st.session_state.theme + "\nAntagonist: " + st.session_state.antagonist + "\n\n"

if "output" not in st.session_state:
    with st.spinner("Generating..."):
        response = ai21.Completion.execute(
            model="j2-grande-instruct",
            prompt=PROMPT + "1. The Ordinary World:\n",
            numResults=1,
            maxTokens=5000,
            minTokens=200,
        )
        st.session_state.output = "1. The Ordinary World:\n" + response.completions[0].data.text

# sometimes ai21 doesn't generate full story, if happens generate missing parts
if "12. The Return:" not in st.session_state.output:
    with st.spinner("Generating..."):
        response = ai21.Completion.execute(
            model="j2-grande-instruct",
            prompt=PROMPT + st.session_state.output,
            numResults=1,
            maxTokens=5000,
            minTokens=200,
        )
        st.session_state.output += response.completions[0].data.text


utils.gen_scenes_areas(st.session_state.output, PROMPT)
utils.export_button()
