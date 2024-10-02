from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    """
    Placeholder for application settings.
    Find more information about pydantic settings
    like yaml/toml parameters, environmental variables at:
    https://docs.pydantic.dev/latest/concepts/pydantic_settings/
    """

    log_level: str = "INFO"
