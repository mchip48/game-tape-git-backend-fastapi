from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str
    env: str

    secret_key: str
    access_token_expire_minutes: int
    database_url: str
    redis_url: str

    class Config:
        env_file = ".env"

settings = Settings()