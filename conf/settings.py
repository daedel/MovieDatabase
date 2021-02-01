from pydantic import BaseSettings


class Settings(BaseSettings):
    access_token: str = "1d828458"

settings = Settings()