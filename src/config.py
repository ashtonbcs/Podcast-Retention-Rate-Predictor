import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = BASE_DIR / "data"

DATABASE_URL = "postgresql://podcast_retention_db_user:PUAe9EnFWNtjd42B9pmuDVtTlTgbtlgi@dpg-d5l96cm3jp1c739609mg-a/podcast_retention_db"


#if not DATABASE_URL:
 #   DATABASE_URL = "postgresql+psycopg2://poduser:poduser@localhost:5433/podcastdb"

#if DATABASE_URL.startswith("postgres://"):
 #   DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)



