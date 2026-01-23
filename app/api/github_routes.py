# # app/api/github_routes.py

from fastapi import APIRouter, HTTPException
from app.core.github_services import get_user, get_repos, get_commits, get_commits_raw
from app.core.github_analysis import summarize_commits
from app.core.github_scoring import score_repo
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

@router.get("/score/{repo_name}")
async def score_repository(repo_name: str):
    
    commits = await get_commits_raw(repo_name)
    analysis = await summarize_commits(commits)

    score = score_repo(analysis)

    return {
        "repo": repo_name,
        "score": score
    }