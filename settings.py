from pathlib import Path

from pydantic.v1 import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent


class AuthJWT(BaseSettings):
    private_key_path: Path = BASE_DIR / "expense_tracker" / "certs" / "private.pem"
    public_key_path: Path = BASE_DIR / "expense_tracker" / "certs" / "public.pem"
    algorithm: str = "RS256"
    access_token_exp_minutes: int = 15
    refresh_token_exp_minutes: int = 15


class Settings(BaseSettings):
    PROJECT_NAME: str = "Expense Tracker"

    DATABASE_URL: str | None = "sqlite:///./expense_tracker.sqlite3"
    ASYNC_DATABASE_URL: str | None = "sqlite+aiosqlite:///./expense_tracker.sqlite3"
    auth_jwt: AuthJWT = AuthJWT()

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
