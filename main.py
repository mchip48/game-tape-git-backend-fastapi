from fastapi import FastAPI
import os
from dotenv import load_dotenv

# Import your project modules
from app.core.config import settings
from app.api import auth, users, repos, commits, highlights

# -----------------------------
# Load .env and GitHub token
# -----------------------------
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Optional debug prints (remove later)
print(f"App Name: {settings.app_name}")
print(f"Secret Key Loaded: {settings.secret_key is not None}")
print(f"GitHub Token Loaded: {GITHUB_TOKEN is not None}")

# -----------------------------
# Create FastAPI app
# -----------------------------
app = FastAPI(
    title="Game Tape API",
    version="0.1.0",
    description="Backend service for Game Tape analysis and security scanning"
)

# -----------------------------
# Include your routers
# -----------------------------
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(repos.router)
app.include_router(commits.router)
app.include_router(highlights.router)

# -----------------------------
# Health check endpoint
# -----------------------------
@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "env": settings.env
    }

# -----------------------------
# Test token endpoint
# -----------------------------
@app.get("/test-token")
def test_token():
    # Don't return the actual token! Just confirm it's loaded
    if GITHUB_TOKEN:
        return {"status": "Token loaded successfully!"}
    return {"status": "Token NOT loaded"}
