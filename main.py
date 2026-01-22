# from fastapi import FastAPI
# import os
# from dotenv import load_dotenv

# # Import your project modules
# from app.core.config import settings
# from app.api import auth, users, repos, commits, highlights, github_routes

# # -----------------------------
# # Load .env and GitHub token
# # -----------------------------
# load_dotenv()
# GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# # Optional debug prints (remove later)
# print(f"App Name: {settings.app_name}")
# print(f"Secret Key Loaded: {settings.secret_key is not None}")
# print(f"GitHub Token Loaded: {GITHUB_TOKEN is not None}")

# # -----------------------------
# # Create FastAPI app
# # -----------------------------
# app = FastAPI(
#     title="Game Tape API",
#     version="0.1.0",
#     description="Backend service for Game Tape analysis and security scanning"
# )

# # -----------------------------
# # Include your routers
# # -----------------------------
# app.include_router(auth.router)
# app.include_router(users.router)
# app.include_router(repos.router)
# app.include_router(commits.router)
# app.include_router(highlights.router)
# app.include_router(github_routes.router)

# # -----------------------------
# # Health check endpoint
# # -----------------------------
# @app.get("/health")
# def health_check():
#     return {
#         "status": "ok",
#         "env": settings.env
#     }

# # -----------------------------
# # Test token endpoint
# # -----------------------------
# @app.get("/test-token")
# def test_token():
#     # Don't return the actual token! Just confirm it's loaded
#     if GITHUB_TOKEN:
#         return {"status": "Token loaded successfully!"}
#     return {"status": "Token NOT loaded"}

# main.py
# from fastapi import FastAPI
# from dotenv import load_dotenv
# import os

# # -----------------------------
# # Load environment variables
# # -----------------------------
# load_dotenv()
# GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
# GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")  # used in commits if needed

# # -----------------------------
# # Import project modules
# # -----------------------------
# from app.core.config import settings
# from app.api import auth, users, repos, commits, highlights, github_routes

# # -----------------------------
# # Create FastAPI app
# # -----------------------------
# app = FastAPI(
#     title=settings.app_name,
#     version="0.1.0",
#     description="Backend service for Game Tape analysis and GitHub integration"
# )

# # -----------------------------
# # Include routers
# # -----------------------------
# app.include_router(auth.router)
# app.include_router(users.router)
# app.include_router(repos.router)
# app.include_router(commits.router)
# app.include_router(highlights.router)
# app.include_router(github_routes.router)

# # -----------------------------
# # Health check endpoint
# # -----------------------------
# @app.get("/health", tags=["System"])
# def health_check():
#     """
#     Simple health check endpoint
#     """
#     return {
#         "status": "ok",
#         "environment": settings.env
#     }

# # -----------------------------
# # Test token endpoint
# # -----------------------------
# @app.get("/test-token", tags=["System"])
# def test_token():
#     """
#     Confirm that the GitHub token is loaded (without revealing it)
#     """
#     if GITHUB_TOKEN:
#         return {"status": "GitHub token loaded successfully!"}
#     return {"status": "GitHub token NOT loaded"}

# main.py
from fastapi import FastAPI
import os
from dotenv import load_dotenv

# Project imports
from app.core.config import settings
from app.api import auth, users, repos, commits, highlights, github_routes

# Load .env
load_dotenv()
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
    description="Backend service for Game Tape analysis and security scanning"
)

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
