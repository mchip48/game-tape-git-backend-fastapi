from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Game Tape"
    env: str = "development"

    secret_key: str = "supersecretkey"
    access_token_expire_minutes: int = 60 # default 60 minutes 
    database_url: str = "sqlite:///./gametape.db"
    redis_url: str = "redis://localhost:6379/0"  # default local Redis

    class Config:
        env_file = ".env"
        extra = "ignore"
        
settings = Settings()