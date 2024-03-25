from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    log_level: str = "INFO"
