from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Example DB URL — use SQLite for testing
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./railway_ivr.db")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ This is the "Base" that other models import
Base = declarative_base()
