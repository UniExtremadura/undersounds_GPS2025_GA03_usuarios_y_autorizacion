from __future__ import annotations

import os
from dataclasses import dataclass
from functools import lru_cache

try:
    from dotenv import load_dotenv
except ModuleNotFoundError:  # pragma: no cover - fallback when dependency missing
    def load_dotenv(*_args, **_kwargs):
        return False

load_dotenv()


@dataclass
class Settings:
    db_url: str
    jwt_secret: str
    access_ttl: int
    refresh_ttl: int


@lru_cache()
def get_settings() -> Settings:
    """Return application settings loaded from environment variables."""
    return Settings(
        db_url=os.getenv("DB_URL", "sqlite:///./undersounds.db"),
        jwt_secret=os.getenv("JWT_SECRET", "change-me"),
        access_ttl=int(os.getenv("ACCESS_TTL", "2592000")),
        refresh_ttl=int(os.getenv("REFRESH_TTL", "2592000")),
    )
