"""
====================================================
OrgoPredict - Reaction Library

This page contains explanations for common organic
chemistry reactions.

Currently, the reaction information is stored in a
Python list.

Later, this page will automatically read the data
from data/reactions.json.
====================================================
"""

import streamlit as st

st.title("📚 Reaction Library")
st.write("Browse common Organic Chemistry reactions.")

st.divider()

# --------------------------------------------------
# Temporary reaction library
# --------------------------------------------------

reaction_library = [

    {
        "name": "Hydrohalogenation",
        "reagent": "HBr",
        "mechanism": "Electrophilic addition through a carbocation intermediate.",
        "why": "The alkene π bond attacks H⁺, followed by Br⁻ attack.",
        "notes": "Usually follows Markovnikov's rule.",
        "memory": "H first, Br second."
    },

    {
        "name": "Radical Hydrohalogenation",
        "reagent": "HBr / ROOR",
        "mechanism": "Free radical chain mechanism.",
        "why": "Peroxides generate radicals that reverse regioselectivity.",
        "notes": "Anti-Markovnikov addition.",
        "memory": "Peroxide = opposite orientation."
    },

    {
        "name": "Halogenation",
        "reagent": "Br₂ or Cl₂",
        "mechanism": "Formation of a halonium ion followed by nucleophilic attack.",
        "why": "The double bond attacks the halogen molecule.",
        "notes": "Produces anti addition products.",
        "memory": "Halonium = Anti addition."
    },

    {
        "name": "Halohydrin Formation",
        "reagent": "Br₂ / H₂O",
        "mechanism": "Bromonium ion followed by water attack.",
        "why": "Water opens the bromonium ion.",
        "notes": "OH goes to the more substituted carbon.",
        "memory": "Water attacks the most stable carbon."
    },

    {
        "name": "Hydroboration-Oxidation",
        "reagent": "BH₃·THF then H₂O₂ / OH⁻",
        "mechanism": "Concerted addition followed by oxidation.",
        "why": "Boron adds first, then is replaced by OH.",
        "notes": "Anti-Markovnikov and syn addition.",
        "memory": "BH₃ = Anti-Mark + Syn."
    },

    {
        "name": "Ozonolysis",
        "reagent": "O₃",
        "mechanism": "Cleavage of the carbon-carbon double bond.",
        "why": "Ozone breaks the alkene into carbonyl compounds.",
        "notes": "Products depend on workup conditions.",
        "memory": "O₃ cuts double bonds."
    },

    {
        "name": "Dihydroxylation",
        "reagent": "OsO₄",
        "mechanism": "Concerted syn addition.",
        "why": "Both OH groups add simultaneously.",
        "notes": "Forms cis diols.",
        "memory": "OsO₄ = Syn OH addition."
    },

    {
        "name": "Epoxidation",
        "reagent": "mCPBA",
        "mechanism": "Concerted oxygen transfer.",
        "why": "Peracid transfers oxygen to the alkene.",
        "notes": "Produces an epoxide.",
        "memory": "mCPBA makes epoxides."
    },

    {
        "name": "Oxidation of Alcohols",
        "reagent": "PCC",
        "mechanism": "Selective oxidation.",
        "why": "Primary alcohols become aldehydes.",
        "notes": "Stops before carboxylic acid.",
        "memory": "PCC is a mild oxidizing agent."
    }
]

# --------------------------------------------------
# Display reactions
# --------------------------------------------------

for reaction in reaction_library:

    with st.expander(
        f"{reaction['name']} ({reaction['reagent']})"
    ):

        st.write("### Mechanism")
        st.write(reaction["mechanism"])

        st.write("### Why it Happens")
        st.write(reaction["why"])

        st.write("### Important Notes")
        st.write(reaction["notes"])

        st.write("### Memory Trick")
        st.success(reaction["memory"])