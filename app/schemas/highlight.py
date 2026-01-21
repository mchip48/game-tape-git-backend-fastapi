# app/schemas/highlight.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Schema for creating a highlight

class HighlightCreate(BaseModel):
    content: str
    line_number: Optional[int]
    commit_id: int

# Schema for updating a highlight

class HighlightUpdate(BaseModel):
    content: Optional[str]
    line_number: Optional[int]

# Schema for response (includes timestamps)

class HighlightResponse(HighlightCreate):
    id: int
    content: str
    line_number: Optional[int]
    commit_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
