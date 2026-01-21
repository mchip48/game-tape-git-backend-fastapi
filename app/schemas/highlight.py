# app/schemas/highlight.py
from pydantic import BaseModel

class HighlightCreate(BaseModel):
    note: str

class HighlightResponse(HighlightCreate):
    id: int
    commit_id: int

    class Config:
        from_attributes = True
