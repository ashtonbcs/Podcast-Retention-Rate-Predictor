import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = BASE_DIR / "data"

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://poduser:poduser@localhost:5433/podcastdb"
)