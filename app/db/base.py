# from sqlalchemy.orm import declarative_base

# Base = declarative_base()

# app/db/base.py
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
