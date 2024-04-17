from pydantic import BaseSettings, Field, Optional


class Settings(BaseSettings):
    # database_hostname: str = "ABC"
    # <- also default values allowed if original env var not present
    # inthat case error will not be raised
    database_hostname: str
    database_port: int
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    refresh_token_expire_minutes: int
    title: str
    version: str
    host: Optional[str] = Field(default="0.0.0.0")
    port: Optonal[int] = Field(default=5000)

    class Config:
        env_file = ".env"


settings = Settings()
