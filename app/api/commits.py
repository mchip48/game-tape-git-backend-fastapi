# app/api/commits.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models.commit import Commit
from app.schemas.commit import CommitCreate, CommitResponse
from app.api.auth import get_db
from app.services.deps import get_current_user

router = APIRouter(
    prefix="/commits",
    tags=["commits"]
)

@router.post("/", response_model=CommitResponse)
def create_commit(
    commit_in: CommitCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    # Optional: verify that current_user owns the repo here
    existing_commit = db.query(Commit).filter(Commit.sha == commit_in.sha).first()
    if existing_commit:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Commit already exists")
    
    commit = Commit(
        sha=commit_in.sha,
        message=commit_in.message,
        author=commit_in.author,
        date=commit_in.date or datetime.utcnow(),
        url=str(commit_in.url),
        repo_id=commit_in.repo_id
    )
    db.add(commit)
    db.commit()
    db.refresh(commit)
    return commit

@router.get("/{commit_id}", response_model=CommitResponse)
def read_commit(commit_id: int, db: Session = Depends(get_db)):
    commit = db.query(Commit).filter(Commit.id == commit_id).first()
    if not commit:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Commit not found")
    return commit
