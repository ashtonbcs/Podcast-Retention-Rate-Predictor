import streamlit as st
import pandas as pd
from typing import Tuple
from sqlalchemy import text
from src.postgres.session import engine

REQ_COL =  [
    "length_minutes",
    "intro_length_seconds",
    "adsNumber",
    "previous_ep_retention",
    "host_energy",
    "completion_percentage",
    "category"
]

NUM_COL = [
    "length_minutes",
    "intro_length_seconds",
    "adsNumber",
    "previous_ep_retention",
    "host_energy",
    "completion_percentage"
]

TABLE_NAME = "podcast_data"


st.title("Import Training Data (CSV)")
st.write("Upload a CSV file to ingest rows")
uploaded = st.file_uploader("Upload a CSV file", type=["csv"])

def validate_data(data: pd.DataFrame) -> Tuple[pd.DataFrame, int]:
    data.columns = [c.strip() for c in data.columns]

    missing = [c for c in REQ_COL if c not in data.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    data = data[REQ_COL].copy()

    for col in NUM_COL:
        data[col] = pd.to_numeric(data[col], errors="coerce")

    data["category"] = data["category"].astype(str)

    before = len(data)
    data = data.dropna(subset=REQ_COL)

    dropped = before - len(data)

    return data, dropped

def insert_df(data: pd.DataFrame) -> int:
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
        data.to_sql(TABLE_NAME, conn, if_exists="append", index=False, method="multi")
    return len(data)

if uploaded:
    try:
        data_raw = pd.read_csv(uploaded)
        st.subheader("Preview (raw)")
        st.dataframe(data_raw.head(20), use_container_width=True)

        data_clean, dropped = validate_data(data_raw)

        st.subheader("Preview (clean)")
        st.dataframe(data_clean.head(20), use_container_width=True)
        st.info(f"Rows to insert: {len(data_clean)} | Rows dropped: {dropped}")

        if st.button("Ingest Data"):
            inserted = insert_df(data_clean)
            st.success(f"Inserted {inserted} rows into {TABLE_NAME} table.")

    except Exception as e:
        st.error(str(e))



