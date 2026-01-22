# app/core/github_services.py
import httpx
import os
from app.core.github import GITHUB_API_BASE, get_headers
from app.core.github_analysis import summarize_commits  # keep summarization logic

async def get_user():
    """Fetch authenticated GitHub user info"""
    url = f"{GITHUB_API_BASE}/user"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=get_headers())
        response.raise_for_status()
        return response.json()

async def get_repos():
    """Fetch authenticated user's repositories"""
    url = f"{GITHUB_API_BASE}/user/repos"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=get_headers())
        response.raise_for_status()
        return response.json()

async def get_commits(repo_name: str, per_page: int = 10):
    username = os.getenv("GITHUB_USERNAME")
    if not username:
        raise ValueError("GITHUB_USERNAME not set in .env")

    url = f"{GITHUB_API_BASE}/repos/{username}/{repo_name}/commits?per_page={per_page}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=get_headers())
        response.raise_for_status()
        commits = response.json()

    # ✅ THIS WAS THE BUG — now fixed
    summary = await summarize_commits(commits)

    return {
        "repo": repo_name,
        "raw_commit_count": len(commits),
        "analysis": summary,
    }