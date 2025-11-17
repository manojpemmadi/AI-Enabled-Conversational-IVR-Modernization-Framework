from app.db.database import initialize_all_tables
from pathlib import Path

def test_database_created():
    initialize_all_tables()
    assert Path("app/db/railway_ivr.db").exists()
