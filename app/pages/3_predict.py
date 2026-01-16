import streamlit as st
from src.ml.predict import predict_log

st.title("Podcast Retention Prediction")

with st.form("predict_form"):
    length_minutes = st.number_input("Episode length (minutes)", min_value=0.0, max_value=130.0, value=62)
    intro_length_seconds = st.number_input("Intro length (seconds)", min_value=0.0, max_value=230.0, value=113)
    adsNumber = st.number_input("Number of ads", min_value=0, max_value=7,value=5, step=1)
    previous_ep_retention = st.number_input("Previous episode retention", min_value=0.0, max_value=80.0, value=41.0)
    host_energy = st.number_input("Host energy", min_value=0.0, max_value=10.0, value=5.0)
    category = st.selectbox("Category", ["News & Politics", "Education", "Self-Improvement", "Comedy",
                                         "Business", "Arts", "Science", "Technology", "True Crime", "Sports", "Health & Fitness", "History"])

    submitted = st.form_submit_button("Predict")

if submitted:
    pred = predict_log(
        length_minutes=length_minutes,
        intro_length_seconds=intro_length_seconds,
        adsNumber=int(adsNumber),
        previous_ep_retention=previous_ep_retention,
        host_energy=host_energy,
        category=category,
    )
    st.success(f"Predicted completion percentage: {pred:.3f}")
