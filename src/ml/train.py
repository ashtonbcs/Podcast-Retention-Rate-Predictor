from src.ml.data import load_train_data
from src.ml.feature_build import build_features
from src.ml.cross_val import cross_val, make_pipeline, metric
from pathlib import Path
import joblib

ARTIFACT_DIR = Path("artifact")
MODEL_PATH = ARTIFACT_DIR / "model.joblib"
ARTIFACT_DIR.mkdir(exist_ok=True)

def train_save():
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    data = load_train_data()
    X, y, num_col, cat_col = build_features(data)
    pipe = make_pipeline(num_col, cat_col)
    scores = cross_val(pipe, X, y, n_splits=5)


    pipe.fit(X, y)

    joblib.dump(pipe, MODEL_PATH)

    return{
        "metric_r2_scores": scores.tolist(),
        "metric_r2_mean": float(scores.mean()),
        "metric_r2_std": float(scores.std()),
        "model_path": str(MODEL_PATH),
    }