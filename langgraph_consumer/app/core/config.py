from typing import Literal, Optional

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Environment Configuration
    ENVIRONMENT: Literal["development", "testing", "staging", "production"] = Field(
        default="development"
    )
    LOG_LEVEL: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = Field(
        default="INFO"
    )

    # Broker Configuration
    BROKER_URL: Optional[str] = Field(default="amqp://guest:guest@localhost:5672//")

    # Backend Configuration
    BACKEND_URL: Optional[str] = Field(default="redis://localhost:6379")

    # Langsmith Configuration
    LANGSMITH_PROJECT: Optional[str] = Field(default=None)
    LANGSMITH_API_KEY: Optional[str] = Field(default=None)
    LANGSMITH_TRACING: Optional[bool] = Field(default=True)

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
