from sqlalchemy import text
from src.postgres.session import engine

def db_health():
    with engine.connect() as conn:
        db = conn.execute(text("select current_database()")).scalar()
        user = conn.execute(text("select current_user")).scalar()
        schema = conn.execute(text("select current_schema()")).scalar()
        return {"db": db, "user": user, "schema": schema}

def table_count(table_name: str):
    with engine.connect() as conn:
        return conn.execute(text(f"SELECT COUNT(*) FROM {table_name}")).scalar()
