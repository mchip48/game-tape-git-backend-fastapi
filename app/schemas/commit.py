# app/schemas/commit.py
from pydantic import BaseModel, HttpUrl
from datetime import datetime

class CommitCreate(BaseModel):
    sha: str
    message: str
    author: str
    url: HttpUrl

class CommitResponse(CommitCreate):
    id: int
    date: datetime
    repo_id: int

    class Config:
        from_attributes = True
