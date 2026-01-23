# main.py
from dotenv import load_dotenv
load_dotenv()

# FastAPI
from fastapi import FastAPI
import os

# SlowAPI
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from app.core.rate_limiter import limiter

# Project imports
from app.core.config import settings
from app.api import auth, users, repos, commits, highlights, github_routes

# Load .env
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")

print(f"App Name: {settings.app_name}")
print(f"Secret Key Loaded: {settings.secret_key is not None}")
print(f"GitHub Token Loaded: {GITHUB_TOKEN is not None}")
print(f"GitHub Username Loaded: {GITHUB_USERNAME is not None}")

# Create FastAPI app
app = FastAPI(
    title="Game Tape API",
    version="0.1.0",
    description="Backend service for Git Game Tape analysis and security scanning"
)

# Register rate limiting globally
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Include routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(repos.router)
app.include_router(commits.router)
app.include_router(highlights.router)
app.include_router(github_routes.router)

# Health check
@app.get("/health")
def health_check():
    return {"status": "ok", "env": settings.env}

# Test token endpoint
@app.get("/test-token")
def test_token():
    return {"status": "Token loaded successfully!" if GITHUB_TOKEN else "Token NOT loaded"}