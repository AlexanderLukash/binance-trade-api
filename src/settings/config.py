from pydantic import Field
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    database_url: str = Field(
        alias="DATABASE_URL",
        default="postgres://my_user:my_password@localhost:5432/my_database",
    )
