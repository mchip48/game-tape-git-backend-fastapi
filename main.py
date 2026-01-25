# main.py
from app.api import auth, users, repos, commits, highlights, github_routes
from app.core.config import settings
from app.core.rate_limiter import limiter

from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

# Load .env
load_dotenv()
API_KEY = os.getenv("API_KEY")
FRONTEND_ORIGINS = os.getenv("FRONTEND_ORIGINS", "")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")

# print(f"App Name: {settings.app_name}")
# print(f"Secret Key Loaded: {settings.secret_key is not None}")
# print(f"GitHub Token Loaded: {GITHUB_TOKEN is not None}")
# print(f"GitHub Username Loaded: {GITHUB_USERNAME is not None}")

def get_allowed_origins():
    return [o.strip() for o in FRONTEND_ORIGINS.split(",") if o.strip()]

# Create FastAPI app
app = FastAPI(
    title="Game Tape API",
    version="0.1.0",
    description="Backend service for Git Game Tape analysis and security scanning"
)

# Add CORS middleware before rate limiter

app.add_middleware(
    CORSMiddleware,
    allow_origins=get_allowed_origins(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
    # allow_headers=["Authorization", "Content-Type", "X-API-Key"],
)

# Register rate limiting globally
limiter = Limiter(key_func=lambda request: request.client.host)
app.state.limiter = limiter
app.add_exception_handler(429, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

# app.state.limiter = limiter
# app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

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