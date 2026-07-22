"""
====================================================
OrgoPredict - Reaction Predictor

This page allows users to:

1. Select a substrate category.
2. Select a substrate.
3. Select a reagent.
4. Predict the reaction product.

The prediction data is loaded from:
data/reactions.json

The prediction logic is handled by:
utils/predictor.py
====================================================
"""

import streamlit as st

from utils.helpers import (
    load_reactions,
    get_categories,
    get_substrates,
    get_reagents
)

from utils.predictor import (
    predict_reaction,
    format_prediction
)


# --------------------------------------------------
# Load reaction database
# --------------------------------------------------

reactions = load_reactions()


# --------------------------------------------------
# Page Title
# --------------------------------------------------

st.title("🧪 Reaction Predictor")

st.write(
    "Select a substrate and reagent, then click **Predict Product**."
)

st.divider()


# --------------------------------------------------
# User selections
# --------------------------------------------------

category = st.selectbox(
    "Substrate Category",
    get_categories(reactions)
)


substrate = st.selectbox(
    "Substrate",
    get_substrates(reactions, category)
)


reagent = st.selectbox(
    "Reagent",
    get_reagents(reactions)
)


st.divider()


# --------------------------------------------------
# Predict Button
# --------------------------------------------------

if st.button("🔬 Predict Product", use_container_width=True):

    reaction = predict_reaction(
        category,
        substrate,
        reagent
    )


    if reaction is None:

        st.error(
            "No matching reaction was found in the database."
        )


    else:

        result = format_prediction(reaction)

        st.success(
            "Reaction Found!"
        )


        st.divider()


        st.subheader("Prediction")


        st.write("### 🧪 Major Product")
        st.write(
            result["Major Product"]
        )


        st.write("### 📖 Reaction Name")
        st.write(
            result["Reaction Name"]
        )


        st.write("### ⚙️ Reaction Type")
        st.write(
            result["Reaction Type"]
        )


        st.write("### 🔬 Mechanism Summary")
        st.write(
            result["Mechanism Summary"]
        )


        st.write("### 📍 Regioselectivity")
        st.write(
            result["Regioselectivity"]
        )


        st.write("### 🧭 Stereochemistry")
        st.write(
            result["Stereochemistry"]
        )


        st.write("### 🔄 Rearrangement")
        st.write(
            result["Rearrangement"]
        )


        st.write("### 🎓 Common Exam Tips")

        st.info(
            result["Common Exam Tips"]
        )