# # app/api/github_routes.py

from fastapi import APIRouter, HTTPException
from app.core.github_services import get_user, get_repos, get_commits
import os

router = APIRouter(prefix="/github", tags=["GitHub"])

@router.get("/user")
async def github_user():
    try:
        return await get_user()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/my-repos")
async def my_repos():
    try:
        repos = await get_repos()
        # Return only repo names (to pass to commits route)
        return [r["name"] for r in repos]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/commits/{repo_name}")
async def github_commits(repo_name: str, per_page: int = 10):
    try:
        return await get_commits(repo_name=repo_name, per_page=per_page)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))