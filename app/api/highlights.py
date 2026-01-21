from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.models.highlight import Highlight
from app.schemas.highlight import HighlightCreate, HighlightResponse

router = APIRouter(prefix="/highlights", tags=["highlights"])

@router.post("/", response_model=HighlightResponse)
def create_highlight(highlight_in: HighlightCreate, db: Session = Depends(get_db)):
    new_highlight = Highlight(
        content=highlight_in.content,
        line_number=highlight_in.line_number,
        commit_id=highlight_in.commit_id
    )
    db.add(new_highlight)
    db.commit()
    db.refresh(new_highlight)
    return new_highlight

@router.get("/commit/{commit_id}", response_model=List[HighlightResponse])
def get_highlights(commit_id: int, db: Session = Depends(get_db)):
    highlights = db.query(Highlight).filter(Highlight.commit_id == commit_id).all()
    return highlights
