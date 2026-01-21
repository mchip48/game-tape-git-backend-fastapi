# app/schemas/repo.py
from pydantic import BaseModel, HttpUrl
from typing import Optional

class RepoCreate(BaseModel):
    name: str
    description: Optional[str]
    url: HttpUrl

class RepoResponse(RepoCreate):
    id: int
    owner_id: int

    class Config:
        from_attributes = True
