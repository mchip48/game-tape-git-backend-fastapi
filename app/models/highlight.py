# app/models/highlight.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base

class Highlight(Base):
    __tablename__ = "highlights"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    line_number = Column(Integer, nullable=True) # <-- Line reference

    # Timestamps

    created_at = Column(DateTime(timezone=True), default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    commit_id = Column(Integer, ForeignKey("commits.id"), nullable=False)
    commit = relationship("Commit", back_populates="highlights")
