import sqlalchemy
import pandas as pd
from src.postgres.session import engine
import numpy as np
from sklearn.preprocessing import OneHotEncoder
def load_train_data():

    query = """
    SELECT
        podcast_data.length_minutes,
        podcast_data.intro_length_seconds,
        podcast_data."adsNumber",
        podcast_data.previous_ep_retention,
        podcast_data.host_energy,
        podcast_data.completion_percentage,
        podcast_data.category
    FROM podcast_data
    """
    data = pd.read_sql(query, engine)
    return data

