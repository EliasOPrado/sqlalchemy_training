# from models import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# connect with database
engine = create_engine("postgresql://localhost")

NEW_DB_NAME = 'database_name'

with engine.connect() as conn:
    conn.execute("commit")
    # Do not substitute user-supplied database names here.
    conn.execute(f"CREATE DATABASE {NEW_DB_NAME}")

# begin of Base for models
Base = declarative_base()

# 
Session = sessionmaker(bind=engine)
session = Session()

# migrations ?
Base.metadata.create_all(engine)
# value = engine.table_names()