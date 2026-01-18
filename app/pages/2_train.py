import streamlit as st
from src.ml.train import train_save
from src.postgres.health import db_health, table_count

st.title("Train The Model")

if st.button("Train Model"):
    st.write("DB:", db_health())
    st.write("podcast_data rows:", table_count("podcast_data"))
    result = train_save()
    st.success("Model Trained and saved")
    st.write("R2 mean", result["metric_r2_mean"])
    st.write("R2 std", result["metric_r2_std"])
    st.write("Scores:", result["metric_r2_scores"])