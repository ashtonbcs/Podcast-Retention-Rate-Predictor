import streamlit as st
from src.ml.train import train_save

st.title("Train The Model")

if st.button("Train Model"):
    result = train_save()
    st.success("Model Trained and saved")
    st.write("R2 mean", result["metric_r2_mean"])
    st.write("R2 std", result["metric_r2_std"])
    st.write("Scores:", result["metric_r2_scores"])