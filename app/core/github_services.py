# app/core/github_services.py
import httpx
from app.core.github import GITHUB_API_BASE, get_headers

async def get_user():
    """Fetch authenticated GitHub user info"""
    url = f"{GITHUB_API_BASE}/user"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=get_headers())
        response.raise_for_status()  # Raises error if status != 200
        return response.json()

async def get_repos():
    """Fetch authenticated user's repositories"""
    url = f"{GITHUB_API_BASE}/user/repos"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=get_headers())
        response.raise_for_status()
        return response.json()

async def get_commits(username: str, repo_name: str, per_page: int = 10):
    """Fetch recent commits for a given repository"""
    url = f"{GITHUB_API_BASE}/repos/{username}/{repo_name}/commits"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=get_headers(), params={"per_page": per_page})
        response.raise_for_status()
        return response.json()
