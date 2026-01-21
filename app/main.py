from fastapi import FastAPI
from app.core.config import settings
from app.api import auth, users, repos, commits, highlights

print(settings.app_name)
print(settings.secret_key)


app = FastAPI(
    title="Game Tape API",
    version="0.1.0",
    description="Backend service for Game Tape analysis and security scanning"
)

# Inclusion of authorization routes
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(repos.router)
app.include_router(commits.router)
app.include_router(highlights.router)

# Health check

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "env": settings.env
    }