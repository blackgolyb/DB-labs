from functools import lru_cache
from pathlib import Path
from typing import Any, Unpack

from envparse import Env  # type: ignore
from pydantic import (
    Field,
    PostgresDsn,
    ValidationInfo,
    field_validator,
)
from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_FOLDER = Path(__file__).parent.parent
SQL_FOLDER = PROJECT_FOLDER / "sql"
MIGRATONS_FOLDER = SQL_FOLDER / "migratons"

ALL_TABLES = [
    "faculties",
    "groups",
    "teachers",
    "subjects",
    "students",
    "profiles",
    "grades",
]

_sentinel: Any = object()


def get_model_config(**kwargs: Unpack[SettingsConfigDict]) -> SettingsConfigDict:
    return SettingsConfigDict(
        env_nested_delimiter="__",
        case_sensitive=False,
        **kwargs,
    )


class PostgresSettings(BaseSettings):
    driver: str
    host: str
    port: int
    user: str
    password: str
    db: str
    url: PostgresDsn = Field(_sentinel, validate_default=True)

    model_config = get_model_config(env_prefix="POSTGRES_")

    @field_validator("url", mode="before")
    @classmethod
    def assemble_db_connection(
        cls, v: str | PostgresDsn, values: ValidationInfo
    ) -> PostgresDsn:
        if isinstance(v, str):
            return PostgresDsn(v)

        return PostgresDsn.build(
            scheme=f"postgresql+{values.data.get('driver')}",
            username=values.data.get("user"),
            password=values.data.get("password"),
            host=f"{values.data.get('host')}:{values.data.get('port')}",
            path=f"{values.data.get('db') or ''}",
        )

    @property
    def url_str(self) -> str:
        return self.url.unicode_string()


class Settings(BaseSettings):
    db: PostgresSettings = Field(default_factory=PostgresSettings)  # type: ignore

    model_config = get_model_config()


@lru_cache
def get_settings() -> Settings:
    env = Env()
    env.read_envfile(PROJECT_FOLDER / "env" / ".env")

    return Settings()
