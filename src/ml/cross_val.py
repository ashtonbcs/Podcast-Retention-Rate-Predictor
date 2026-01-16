from sklearn.model_selection import KFold, cross_val_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from src.ml.feature_build import build_features
from src.ml.data import load_train_data
data = load_train_data()

X, y, num_col, cat_col = build_features(data)
def make_pipeline(num_col, cat_col):
    preprocess = ColumnTransformer(
        transformers=[
            ("numeric", StandardScaler(), num_col),
            ("categorical", OneHotEncoder(handle_unknown="ignore"), cat_col),
        ]
    )

    pipe = Pipeline([
        ("preprocess", preprocess),
        ('regressor', LinearRegression())
    ])

    return pipe

def cross_val(pipe, X, y):
    kf = KFold(n_splits=5, shuffle=True, random_state=42)
    return cross_val_score(pipe, X, y, cv=kf, scoring='r2')


def metric(score):
    score_list = [score]
    return score_list