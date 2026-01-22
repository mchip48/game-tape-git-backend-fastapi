# app/api/github_routes.py
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

@router.get("/repos")
async def github_repos():
    try:
        return await get_repos()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/commits/{repo_name}")
async def github_commits(repo_name: str, per_page: int = 10):
    """Fetch recent commits for a given repo"""
    username = os.getenv("GITHUB_USERNAME")  # store your GitHub username in .env

    try:
        commits = await get_commits(username=username, repo_name=repo_name, per_page=per_page)
        return {"repo": repo_name, "commits": commits}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))