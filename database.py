from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Ensure the DATABASE_URL is correctly set or fallback to a default value
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://pieraly:pieraly@localhost:3306/items_db")

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class for declarative models
Base = declarative_base()