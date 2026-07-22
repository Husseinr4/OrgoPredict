"""
====================================================
OrgoPredict - Quiz Mode

This page quizzes the user on organic chemistry
reactions.

For now, the questions are stored in a Python list.

Later, they will be loaded automatically from
data/reactions.json.
====================================================
"""

import random
import streamlit as st

st.title("📝 Quiz Mode")
st.write("Test your Organic Chemistry knowledge!")

st.divider()

# --------------------------------------------------
# Temporary quiz questions
# These will later come from reactions.json
# --------------------------------------------------
quiz_questions = [
    {
        "substrate": "Propene",
        "reagent": "HBr",
        "answer": "2-Bromopropane",
        "reaction": "Hydrohalogenation"
    },
    {
        "substrate": "Propene",
        "reagent": "HBr / ROOR",
        "answer": "1-Bromopropane",
        "reaction": "Radical Addition"
    },
    {
        "substrate": "Cyclohexene",
        "reagent": "Br₂",
        "answer": "trans-1,2-Dibromocyclohexane",
        "reaction": "Halogenation"
    },
    {
        "substrate": "Cyclohexene",
        "reagent": "Br₂ / H₂O",
        "answer": "Bromohydrin",
        "reaction": "Halohydrin Formation"
    },
    {
        "substrate": "Cyclohexene",
        "reagent": "OsO₄",
        "answer": "cis-1,2-Cyclohexanediol",
        "reaction": "Syn Dihydroxylation"
    }
]

# --------------------------------------------------
# Store current question
# --------------------------------------------------
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(quiz_questions)

question = st.session_state.current_question

# --------------------------------------------------
# Display question
# --------------------------------------------------
st.subheader("Predict the Product")

st.write(f"**Substrate:** {question['substrate']}")
st.write(f"**Reagent:** {question['reagent']}")

user_answer = st.text_input(
    "Enter the major product:"
)

col1, col2 = st.columns(2)

# --------------------------------------------------
# Show Answer
# --------------------------------------------------
with col1:

    if st.button("Show Answer"):

        st.success("Correct Answer")

        st.write(
            f"**Major Product:** {question['answer']}"
        )

        st.write(
            f"**Reaction:** {question['reaction']}"
        )

# --------------------------------------------------
# Next Question
# --------------------------------------------------
with col2:

    if st.button("Next Question"):

        st.session_state.current_question = random.choice(
            quiz_questions
        )

        st.rerun()

st.divider()

st.info(
    "Later versions will automatically generate quiz "
    "questions from the reaction database."
)