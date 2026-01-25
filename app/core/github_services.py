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
        commits_data = response.json() # must be a list of dicts

        # DEBUG: ensure all commits are dicts
        commits = []
        for c in commits_data:
            if isinstance(c, dict) and "commit" in c:
                commits.append(c)
            elif isinstance(c, str):
                # sometimes API may return SHA string only; fetch full commit
                commit_url = f"{GITHUB_API_BASE}/repos/{username}/{repo_name}/commits/{c}"
                r = await client.get(commit_url, headers=get_headers())
                r.raise_for_status()
                commits.append(r.json())
            else:
                raise ValueError(f"Unexpected commit format: {c}")

    # ✅ THIS WAS THE BUG— now fixed
    # summarize_commits expects list[dict]
    summary = await summarize_commits(commits)

    return {
        "repo": repo_name,
        "raw_commit_count": len(commits),
        "analysis": summary,
    }

# Helper function to turn raw commit data from a dict into a list[dict]

async def get_commits_raw(repo_name: str, per_page: int = 100): # updated int = 10 to be int = 100, fix the rest of this function for pagination later 
    """Fetch raw commits list only (no summary)."""
    username = os.getenv("GITHUB_USERNAME")
    if not username:
        raise ValueError("GITHUB_USERNAME not set in .env")

    url = f"{GITHUB_API_BASE}/repos/{username}/{repo_name}/commits?per_page={per_page}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=get_headers())
        response.raise_for_status()
        commits_data = response.json()

        # filter just the valid commits
        commits = [c for c in commits_data if isinstance(c, dict) and "commit" in c]

    return commits
