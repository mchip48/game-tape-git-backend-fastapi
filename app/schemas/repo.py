# app/schemas/repo.py

from pydantic import BaseModel, HttpUrl
from typing import Optional, List
from datetime import datetime

# Base schema shared by input and output
class RepoBase(BaseModel):
    name: str
    description: Optional[str] = None
    url: HttpUrl  # ensures it's a valid URL

# Schema for creating a new repo
class RepoCreate(RepoBase):
    pass  # inherits all fields from RepoBase

# Schema for returning repo info to the client
class RepoResponse(RepoBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # allows Pydantic to read from SQLAlchemy objects
