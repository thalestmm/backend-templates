from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Base Configuration
    ENVIRONMENT: Literal["development", "testing", "staging", "production"] = Field(
        default="development", description="The current environment"
    )
    LOG_LEVEL: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = Field(
        default="DEBUG", description="Logging level"
    )

    class Config:
        env_file = ".env"
        case_sensitive = True
        ignore_extra = True

    @property
    def is_production(self) -> bool:
        return self.ENVIRONMENT == "production"


# Settings singleton
settings = Settings()

__all__ = ["settings"]
