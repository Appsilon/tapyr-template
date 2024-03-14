from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    log_level: str = "INFO"
