"""
====================================================
OrgoPredict - Search Page

This page allows users to search reactions by reagent.

The information is loaded from:
data/reactions.json

This keeps all pages connected to the same database.
====================================================
"""

import streamlit as st

from utils.helpers import (
    load_reactions,
    get_reagents
)


# --------------------------------------------------
# Load reaction database
# --------------------------------------------------

reactions = load_reactions()


# --------------------------------------------------
# Page Title
# --------------------------------------------------

st.title("🔍 Search Reactions")

st.write(
    "Search for reactions by reagent."
)

st.divider()


# --------------------------------------------------
# Select reagent
# --------------------------------------------------

reagent = st.selectbox(
    "Choose a reagent",
    get_reagents(reactions)
)


# --------------------------------------------------
# Search Results
# --------------------------------------------------

if st.button("🔎 Search", use_container_width=True):

    results = [
        reaction
        for reaction in reactions
        if reaction["reagent"] == reagent
    ]


    if results:

        st.success(
            f"{len(results)} reaction(s) found."
        )


        for reaction in results:

            st.divider()

            st.subheader(
                reaction["reaction_name"]
            )


            st.write(
                "**Substrate:**",
                reaction["substrate"]
            )


            st.write(
                "**Major Product:**",
                reaction["major_product"]
            )


            st.write(
                "**Reaction Type:**",
                reaction["reaction_type"]
            )


            st.write(
                "**Mechanism:**",
                reaction["mechanism_summary"]
            )


            st.write(
                "**Regioselectivity:**",
                reaction["regioselectivity"]
            )


            st.write(
                "**Stereochemistry:**",
                reaction["stereochemistry"]
            )


            st.write(
                "**Exam Tips:**",
                reaction["exam_tips"]
            )

    else:

        st.warning(
            "No reactions found for this reagent."
        )