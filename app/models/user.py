from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base # <-- imported Base fromn db/base.py

class User(Base):
    __tablename__ = "users"


    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    # Relationships
    repos = relationship("Repo", back_populates="owner", cascade="all, delete-orphan")