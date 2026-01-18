import streamlit as st

st.set_page_config(
    page_title="Podcast Retention Predictor",
    layout="wide"
)

st.title("Podcast Retention Predictor")
st.write("""
    Please use the sidebar to navigate.
    - **Import** to import training data
    - **Train** to retain the model and save it.
    - **Predict** to enter features and log predictions.
""")