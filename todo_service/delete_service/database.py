import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_USER = os.getenv("POSTGRES_USER", "user")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "pass")
DB_NAME = os.getenv("POSTGRES_DB", "todos")
DB_HOST = os.getenv("POSTGRES_HOST", "todo-db")

SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
