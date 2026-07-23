"""
===========================================================
OrgoPredict

Main application entry point.

Developed by:
Hussein Rizk
Chemical Engineering Student
American University of Beirut

===========================================================
"""

import streamlit as st

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="OrgoPredict",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------

st.sidebar.title("🧪 OrgoPredict")

st.sidebar.success(
    "Use the pages in the sidebar to explore the application."
)

st.sidebar.markdown("---")

st.sidebar.write("Version 1.0")

st.sidebar.write("Developed by")

st.sidebar.markdown(
    """
**Hussein Rizk**

Chemical Engineering Student

American University of Beirut
"""
)

# ---------------------------------------------------------
# Hero Section
# ---------------------------------------------------------

st.title("🧪 OrgoPredict")

st.subheader(
    "Organic Chemistry Reaction Prediction Platform"
)

st.markdown("---")

left, right = st.columns([2, 1])

with left:

    st.markdown(
        """
### Predict. Understand. Master Organic Chemistry.

OrgoPredict is an educational platform designed for undergraduate
Organic Chemistry students.

Using a structured reaction database, the application helps users
predict products, understand reaction mechanisms, and prepare
for exams.
"""
    )

# --------------------------------------------------
# Features Navigation
# --------------------------------------------------

st.subheader("✨ Features")

col1, col2, col3 = st.columns(3)


with col1:

    if st.button(
        "🔬 Predict reaction products",
        use_container_width=True
    ):
        st.switch_page(
            "pages/predictor.py"
        )


with col2:

    if st.button(
        "📚 Reaction library",
        use_container_width=True
    ):
        st.switch_page(
            "pages/reaction_library.py"
        )


with col3:

    if st.button(
        "🔍 Search by reagent",
        use_container_width=True
    ):
        st.switch_page(
            "pages/search.py"
        )


col4, col5, col6 = st.columns(3)


with col4:

    if st.button(
        "🧠 Quiz mode",
        use_container_width=True
    ):
        st.switch_page(
            "pages/quiz.py"
        )


with col5:

    st.button(
        "⚡ Fast JSON prediction engine",
        use_container_width=True,
        disabled=True
    )


with col6:

    st.button(
        "📈 Continuously expanding reaction database",
        use_container_width=True,
        disabled=True
    )


with right:

    st.info(
        """
### Developer

**Hussein Rizk**

Chemical Engineering Student

American University of Beirut
"""
    )

# ---------------------------------------------------------
# Platform Overview
# ---------------------------------------------------------

st.markdown("---")

st.header("Platform Modules")

col1, col2 = st.columns(2)

with col1:

    st.subheader("🧪 Reaction Predictor")

    st.write(
        """
Choose a substrate and reagent.

Instantly predict:

- Major product
- Reaction type
- Mechanism
- Regioselectivity
- Stereochemistry
- Rearrangements
"""
    )

    st.subheader("📚 Reaction Library")

    st.write(
        """
Browse reactions chapter by chapter.

Review mechanisms and important notes.
"""
    )

with col2:

    st.subheader("🔍 Search")

    st.write(
        """
Search reactions by reagent.

Quickly locate reaction information for studying.
"""
    )

    st.subheader("🎯 Quiz Mode")

    st.write(
        """
Practice predicting products.

Reveal the correct answer after making your prediction.
"""
    )

# ---------------------------------------------------------
# Vision
# ---------------------------------------------------------

st.markdown("---")

st.header("Project Vision")

st.write(
"""
OrgoPredict aims to become a comprehensive learning platform for
undergraduate Organic Chemistry.

Future updates include:

• 300+ reaction database

• RDKit molecular structures

• Reaction equations

• Multi-step synthesis prediction

• Functional group recognition

• AI-assisted reaction explanations

• Progress tracking

• Exam mode
"""
)

# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

st.markdown("---")

st.caption(
    "© 2026 Hussein Rizk • OrgoPredict • Version 1.0"
)
# streamlit run app.py
