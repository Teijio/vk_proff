from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = "Тестовое задание для лучшей социальной сети"
    database_url: str

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
