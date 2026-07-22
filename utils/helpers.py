"""
====================================================
OrgoPredict - Helper Functions

This module contains reusable helper functions that
can be used throughout the application.

Keeping these functions in a separate file makes the
project easier to maintain and avoids repeating code.
====================================================
"""

import json
from pathlib import Path


# --------------------------------------------------
# Get the path to reactions.json
# --------------------------------------------------
def get_database_path():
    """
    Returns the full path to data/reactions.json.

    Using pathlib keeps the code portable across
    Windows, macOS, and Linux.
    """

    project_root = Path(__file__).resolve().parent.parent
    return project_root / "data" / "reactions.json"


# --------------------------------------------------
# Load the reaction database
# --------------------------------------------------
def load_reactions():
    """
    Reads reactions.json and returns a list of
    reaction dictionaries.

    Returns:
        list: All reactions in the database.

    Raises:
        FileNotFoundError:
            If reactions.json does not exist.

        json.JSONDecodeError:
            If the JSON file is not valid.
    """

    database_path = get_database_path()

    with open(database_path, "r", encoding="utf-8") as file:
        reactions = json.load(file)

    return reactions


# --------------------------------------------------
# Find all unique substrate categories
# --------------------------------------------------
def get_categories(reactions):
    """
    Returns a sorted list of substrate categories.

    Example:
        Alkane
        Alkene
        Alcohol
    """

    categories = {
        reaction["substrate_category"]
        for reaction in reactions
    }

    return sorted(categories)


# --------------------------------------------------
# Find substrates in one category
# --------------------------------------------------
def get_substrates(reactions, category):
    """
    Returns all substrates belonging to a selected
    substrate category.
    """

    substrates = {
        reaction["substrate"]
        for reaction in reactions
        if reaction["substrate_category"] == category
    }

    return sorted(substrates)


# --------------------------------------------------
# Find available reagents
# --------------------------------------------------
def get_reagents(reactions):
    """
    Returns a sorted list of all reagents stored in
    the reaction database.
    """

    reagents = {
        reaction["reagent"]
        for reaction in reactions
    }

    return sorted(reagents)


# --------------------------------------------------
# Search reactions by reagent
# --------------------------------------------------
def search_by_reagent(reactions, reagent):
    """
    Returns every reaction that uses the selected
    reagent.
    """

    return [
        reaction
        for reaction in reactions
        if reaction["reagent"].lower() == reagent.lower()
    ]