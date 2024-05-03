from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = "Тестовое задание для лучшей социальной сети"
    database_url: str
    secret_key: str = "very_stronk_key"

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
