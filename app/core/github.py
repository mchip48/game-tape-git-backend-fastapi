# app/core/github.py
import os

GITHUB_API_BASE = "https://api.github.com"

def get_headers():
    """Return headers with the GitHub token."""
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise ValueError("GITHUB_TOKEN not set in environment")
    return {"Authorization": f"token {token}"}
