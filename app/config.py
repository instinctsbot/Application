from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME : str
    DEBUG : bool = False

    DATABASE_URL : str

    OPENAI_API_KEY : str

    TELEGRAM_BOT_TOKEN : str
    TELEGRAM_CHAT_ID : str

    SECRET_KEY : str
    ALGORITHM : str
    ACCESS_TOKEN_EXPIRE_MINUTES : int

    REDIS_URL : str

    class Config:
        env_file = ".env"

@lru_cache
def get_settings():
    return Settings()

settings = Settings()

OPENAI_MODEL : str = "gpt-4.1-mini"

REPORT_HOUR: int = 9
REPORT_MINUTE: int = 0