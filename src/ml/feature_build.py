from src.ml.data import load_train_data
import numpy as np
from sklearn.preprocessing import OneHotEncoder

data = load_train_data()

X_col = ['length_minutes', 'intro_length_seconds', 'adsNumber','previous_ep_retention','host_energy']
y_col = ['completion_percentage']
x_cat = ['category']


def build_features(data):
    X = data[X_col + x_cat]
    y = data[y_col]
    return X, y, X_col, x_cat
