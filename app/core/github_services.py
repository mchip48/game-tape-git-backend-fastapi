# # app/core/github_services.py
# import httpx
# from app.core.github import GITHUB_API_BASE, get_headers

# async def get_user():
#     """Fetch authenticated GitHub user info"""
#     url = f"{GITHUB_API_BASE}/user"
#     async with httpx.AsyncClient() as client:
#         response = await client.get(url, headers=get_headers())
#         response.raise_for_status()  # Raises error if status != 200
#         return response.json()

# async def get_repos():
#     """Fetch authenticated user's repositories"""
#     url = f"{GITHUB_API_BASE}/user/repos"
#     async with httpx.AsyncClient() as client:
#         response = await client.get(url, headers=get_headers())
#         response.raise_for_status()
#         return response.json()

# async def get_commits(repo_full_name: str):
#     """
#     Fetch commits for a given repository.
#     repo_full_name: 'owner/repo_name'
#     """
#     url = f"{GITHUB_API_BASE}/repos/{repo_full_name}/commits"
#     async with httpx.AsyncClient() as client:
#         response = await client.get(url, headers=get_headers())
#         response.raise_for_status()  # Raises error if status != 200
#         return response.json()

# app/core/github_services.py
# ---------------------------------------------------------------------
# import httpx
# from app.core.github import GITHUB_API_BASE, get_headers
# from typing import List, Dict

# async def get_user() -> Dict:
#     """Fetch authenticated GitHub user info"""
#     url = f"{GITHUB_API_BASE}/user"
#     async with httpx.AsyncClient() as client:
#         response = await client.get(url, headers=get_headers())
#         response.raise_for_status()
#         return response.json()

# async def get_repos() -> List[Dict]:
#     """Fetch authenticated user's repositories"""
#     url = f"{GITHUB_API_BASE}/user/repos"
#     async with httpx.AsyncClient() as client:
#         response = await client.get(url, headers=get_headers())
#         response.raise_for_status()
#         return response.json()

# async def get_commits(owner: str, repo: str) -> List[Dict]:
#     """Fetch commits for a given repository"""
#     url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/commits"
#     async with httpx.AsyncClient() as client:
#         response = await client.get(url, headers=get_headers())
#         response.raise_for_status()
#         return response.json()

# app/core/github_services.py
# import os
# import httpx
# from app.core.github import GITHUB_API_BASE, get_headers
# from typing import List, Dict, Optional

# async def get_user() -> Dict:
#     """Fetch authenticated GitHub user info"""
#     url = f"{GITHUB_API_BASE}/user"
#     async with httpx.AsyncClient() as client:
#         response = await client.get(url, headers=get_headers())
#         response.raise_for_status()
#         return response.json()

# async def get_repos() -> List[Dict]:
#     """Fetch authenticated user's repositories"""
#     url = f"{GITHUB_API_BASE}/user/repos"
#     async with httpx.AsyncClient() as client:
#         response = await client.get(url, headers=get_headers())
#         response.raise_for_status()
#         return response.json()

# async def get_commits(repo_full_name: str, per_page: Optional[int] = 10) -> List[Dict]:
#     """
#     Fetch commits for a given repository.
#     repo_full_name: 'owner/repo_name'
#     per_page: how many commits to fetch
#     """
#     url = f"{GITHUB_API_BASE}/repos/{repo_full_name}/commits?per_page={per_page}"
#     async with httpx.AsyncClient() as client:
#         response = await client.get(url, headers=get_headers())
#         response.raise_for_status()
#         return response.json()
# -------------------------------------------------------------------------------------------
# async def get_commits(repo_name: str, per_page: int = 10):
#     """
#     Fetch commits for a given repo (uses GITHUB_USERNAME from .env)
#     """
#     username = os.getenv("GITHUB_USERNAME")
#     if not username:
#         raise ValueError("GITHUB_USERNAME not set in .env")

#     url = f"{GITHUB_API_BASE}/repos/{username}/{repo_name}/commits?per_page={per_page}"
#     async with httpx.AsyncClient() as client:
#         response = await client.get(url, headers=get_headers())
#         response.raise_for_status()
#         return response.json()
# -------------------------------------------------------------------------------------------

# async def get_commits(repo_name: str, per_page: int = 10):
#     """
#     Fetch commits for a given repository.
#     Automatically uses GITHUB_USERNAME from .env.
#     """
#     username = os.getenv("GITHUB_USERNAME")
#     if not username:
#         raise ValueError("GITHUB_USERNAME not set in .env")

#     url = f"{GITHUB_API_BASE}/repos/{username}/{repo_name}/commits?per_page={per_page}"
#     async with httpx.AsyncClient() as client:
#         response = await client.get(url, headers=get_headers())
#         response.raise_for_status()
#         commits = response.json()
#         # Run your summarization
#         summary = summarize_commits(commits)
#         return summary

# app/core/github_services.py
import httpx
import os
from app.core.github import GITHUB_API_BASE, get_headers
from app.core.github_analysis import summarize_commits  # keep your summarization logic

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

# async def get_commits(repo_name: str, per_page: int = 10):
#     """
#     Fetch commits for a given repository.
#     Automatically uses GITHUB_USERNAME from .env.
#     """
#     username = os.getenv("GITHUB_USERNAME")
#     if not username:
#         raise ValueError("GITHUB_USERNAME not set in .env")

#     url = f"{GITHUB_API_BASE}/repos/{username}/{repo_name}/commits?per_page={per_page}"
#     async with httpx.AsyncClient() as client:
#         response = await client.get(url, headers=get_headers())
#         response.raise_for_status()
#         commits = response.json()
#         # Run your summarization
#         summary = summarize_commits(commits)
#         return summary

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