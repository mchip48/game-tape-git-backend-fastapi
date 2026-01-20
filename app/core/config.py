from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Game Tape"
    env: str = "development"

    secret_key: str = "supersecretkey"
    access_token_expire_minutes: int 
    database_url: str = "sqlite:///./gametape.db"
    redis_url: str

    class Config:
        env_file = ".env"

settings = Settings()