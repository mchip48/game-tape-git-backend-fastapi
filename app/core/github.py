# app/core/github.py
import os
import httpx

# Load token from environment
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Base headers for authenticated requests
HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

GITHUB_API_BASE = "https://api.github.com"
