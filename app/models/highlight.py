# app/models/highlight.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Highlight(Base):
    __tablename__ = "highlights"

    id = Column(Integer, primary_key=True, index=True)
    note = Column(String, nullable=True)

    commit_id = Column(Integer, ForeignKey("commits.id"), nullable=False)
    commit = relationship("Commit", back_populates="highlights")
