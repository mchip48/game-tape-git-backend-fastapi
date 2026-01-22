# app/api/github_routes.py
from fastapi import APIRouter, HTTPException
from app.core.github_services import get_user, get_repos

router = APIRouter(prefix="/github", tags=["GitHub"])

@router.get("/user")
async def github_user():
    try:
        return await get_user()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/repos")
async def github_repos():
    try:
        return await get_repos()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
