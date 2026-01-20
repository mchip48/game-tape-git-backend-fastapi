from fastapi import FastAPI

app = FastAPI(
    title="Game Tape API",
    version="0.1.0",
    description="Backend service for Game Tape analysis and security scanning"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}