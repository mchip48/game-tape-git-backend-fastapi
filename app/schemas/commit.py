# app/schemas/commit.py
from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import Optional

class CommitCreate(BaseModel):
    sha: str
    message: str
    author: str
    date: Optional[datetime] = None
    url: HttpUrl
    repo_id: int

class CommitResponse(BaseModel):
    id: int
    sha: str
    message: str
    author: str
    date: datetime
    url: str
    repo_id: int

    class Config:
        from_attributes = True
