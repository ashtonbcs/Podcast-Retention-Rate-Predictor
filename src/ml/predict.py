import pandas as pd
from pathlib import Path
import joblib

from src.postgres.session import SessionLocal
from src.postgres.table import PodcastPrediction

MODEL_PATH = Path("artifacts/model.joblib")

FEATURE_COLUMNS = [
    "length_minutes",
    "intro_length_seconds",
    "adsNumber",
    "previous_ep_retention",
    "host_energy",
    "category",
]


def load_model():
    return joblib.load(MODEL_PATH)


def predict_log(
    length_minutes: float,
    intro_length_seconds: float,
    adsNumber: int,
    previous_ep_retention: float,
    host_energy: float,
    category: str,
) -> float:

    # Build 1-row input DataFrame
    X_new = pd.DataFrame(
        [{
            "length_minutes": length_minutes,
            "intro_length_seconds": intro_length_seconds,
            "adsNumber": adsNumber,
            "previous_ep_retention": previous_ep_retention,
            "host_energy": host_energy,
            "category": category,
        }],
        columns=FEATURE_COLUMNS
    )

    model = load_model()
    pred = float(model.predict(X_new)[0])

    # Save prediction to DB
    db = SessionLocal()
    try:
        row = PodcastPrediction(
            length_minutes=length_minutes,
            intro_length_seconds=intro_length_seconds,
            adsNumber=adsNumber,
            previous_ep_retention=previous_ep_retention,
            host_energy=host_energy,
            category=category,
            predicted_completion_percentage=pred,
        )
        db.add(row)
        db.commit()
    finally:
        db.close()

    return pred
