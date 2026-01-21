# app/models/commit.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base

class Commit(Base):
    __tablename__ = "commits"

    id = Column(Integer, primary_key=True, index=True)
    sha = Column(String, index=True, nullable=False)
    message = Column(String, nullable=False)
    author = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    url = Column(String, nullable=False)

    repo_id = Column(Integer, ForeignKey("repos.id"), nullable=False)
    repo = relationship("Repo", back_populates="commits")

    highlights = relationship("Highlight", back_populates="commit", cascade="all, delete-orphan")
