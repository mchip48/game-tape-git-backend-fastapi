from fastapi import FastAPI
from app.core.config import settings
from app.api import auth

print(settings.app_name)
print(settings.secret_key)


app = FastAPI(
    title="Game Tape API",
    version="0.1.0",
    description="Backend service for Game Tape analysis and security scanning"
)

# Inclusion of authorization routes
app.include_router(auth.router)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "env": settings.env
    }