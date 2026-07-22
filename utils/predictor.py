
"""
====================================================
OrgoPredict - Prediction Engine

This module searches the reaction database and
returns the matching reaction.

All prediction logic is kept here so the Streamlit
pages only handle the user interface.
====================================================
"""

from utils.helpers import load_reactions


# --------------------------------------------------
# Predict a reaction
# --------------------------------------------------
def predict_reaction(substrate_category, substrate, reagent):
    """
    Search the reaction database for a matching reaction.

    Parameters
    ----------
    substrate_category : str
    substrate : str
    reagent : str

    Returns
    -------
    dict or None
        Returns the matching reaction dictionary.
        Returns None if no match exists.
    """

    reactions = load_reactions()

    for reaction in reactions:

        if (
            reaction["substrate_category"].lower() == substrate_category.lower()
            and reaction["substrate"].lower() == substrate.lower()
            and reaction["reagent"].lower() == reagent.lower()
        ):
            return reaction

    return None


# --------------------------------------------------
# Format prediction results
# --------------------------------------------------
def format_prediction(reaction):
    """
    Convert a reaction dictionary into a format that
    is easy for Streamlit to display.
    """

    if reaction is None:
        return None

    return {
        "Major Product": reaction["major_product"],
        "Reaction Name": reaction["reaction_name"],
        "Reaction Type": reaction["reaction_type"],
        "Mechanism Summary": reaction["mechanism_summary"],
        "Regioselectivity": reaction["regioselectivity"],
        "Stereochemistry": reaction["stereochemistry"],
        "Rearrangement": reaction["rearrangement"],
        "Common Exam Tips": reaction["exam_tips"],
    }


# --------------------------------------------------
# Check whether a reaction exists
# --------------------------------------------------
def reaction_exists(substrate_category, substrate, reagent):
    """
    Returns True if the reaction exists in the database.
    """

    return (
        predict_reaction(
            substrate_category,
            substrate,
            reagent
        )
        is not None
    )

