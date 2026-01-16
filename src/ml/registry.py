import joblib
from pathlib import Path

MODEL_PATH = Path("artifacts/model.joblib")

def save_model(model):
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)

def load_model():
    model = joblib.load(MODEL_PATH)
    return model