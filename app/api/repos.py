# app/api/repos.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.models.repo import Repo
from app.schemas.repo import RepoCreate, RepoResponse
from app.services.deps import get_db, get_current_user

router = APIRouter(
    prefix="/repos",
    tags=["repos"]
)

# Create a repo
@router.post("/", response_model=RepoResponse)
def create_repo(repo_in: RepoCreate, current_user = Depends(get_current_user), db: Session = Depends(get_db)):
    # Check if URL already exists
    existing_repo = db.query(Repo).filter(Repo.url == repo_in.url).first()
    if existing_repo:
        raise HTTPException(status_code=400, detail="Repo with this URL already exists")
    
    new_repo = Repo(
        name=repo_in.name,
        description=repo_in.description,
        url=repo_in.url,
        owner_id=current_user.id
    )
    db.add(new_repo)
    db.commit()
    db.refresh(new_repo)
    return new_repo

# Get all repos
@router.get("/", response_model=List[RepoResponse])
def get_repos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    repos = db.query(Repo).offset(skip).limit(limit).all()
    return repos

# Get one repo by ID
@router.get("/{repo_id}", response_model=RepoResponse)
def get_repo(repo_id: int, db: Session = Depends(get_db)):
    repo = db.query(Repo).filter(Repo.id == repo_id).first()
    if not repo:
        raise HTTPException(status_code=404, detail="Repo not found")
    return repo
