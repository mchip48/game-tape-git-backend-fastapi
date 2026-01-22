import requests
from typing import List, Dict
from fastapi import HTTPException
import os

# Load GitHub token from environment variable for security
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    raise RuntimeError("Please set your GITHUB_TOKEN environment variable!")

HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

BASE_URL = "https://api.github.com"

def get_user_repos(username: str) -> List[Dict]:
    """Fetch public repos for a given GitHub username."""
    url = f"{BASE_URL}/users/{username}/repos"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail=f"Error fetching repos for user {username}: {response.text}"
        )
    return response.json()

def get_repo_commits(owner: str, repo: str) -> List[Dict]:
    """Fetch commits for a specific repository."""
    url = f"{BASE_URL}/repos/{owner}/{repo}/commits"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail=f"Error fetching commits for {owner}/{repo}: {response.text}"
        )
    return response.json()
