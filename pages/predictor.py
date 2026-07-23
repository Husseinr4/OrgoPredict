"""
====================================================
OrgoPredict - Reaction Predictor
====================================================
"""

import streamlit as st

from utils.helpers import (
    load_reactions,
    get_categories,
    get_substrates,
    get_reagents,
)

from utils.predictor import (
    predict_reaction,
    format_prediction,
)

# ----------------------------------------
# Load database
# ----------------------------------------

reactions = load_reactions()

# ----------------------------------------
# Page
# ----------------------------------------

st.title("🧪 Reaction Predictor")

st.write(
    "Select a substrate and reagent, then click **Predict Product**."
)

st.divider()

# ----------------------------------------
# Category
# ----------------------------------------

category = st.selectbox(
    "Substrate Category",
    get_categories(reactions),
)

# ----------------------------------------
# Substrate
# ----------------------------------------

substrate = st.selectbox(
    "Substrate",
    get_substrates(reactions, category),
)

# ----------------------------------------
# Reagent
# ----------------------------------------

reagent = st.selectbox(
    "Reagent",
    get_reagents(reactions, category),
)

st.divider()

# ----------------------------------------
# Predict
# ----------------------------------------

if st.button("🔬 Predict Product", use_container_width=True):

    reaction = predict_reaction(
        category,
        substrate,
        reagent,
    )

    if reaction is None:

        st.error("No matching reaction found.")

    else:

        result = format_prediction(reaction)

        st.success("Prediction Complete")

        st.markdown("---")

        st.subheader("🧪 Major Product")
        st.write(result["Major Product"])

        st.subheader("📖 Reaction Name")
        st.write(result["Reaction Name"])

        st.subheader("⚙️ Reaction Type")
        st.write(result["Reaction Type"])

        st.subheader("🔬 Mechanism Summary")
        st.write(result["Mechanism Summary"])

        st.subheader("📍 Regioselectivity")
        st.write(result["Regioselectivity"])

        st.subheader("🧬 Stereochemistry")
        st.write(result["Stereochemistry"])

        st.subheader("🔄 Rearrangement")
        st.write(result["Rearrangement"])

        st.subheader("🎓 Common Exam Tips")
        st.info(result["Common Exam Tips"])