from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_HOST: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_PORT: int

    @property
    def DATABASE_URL_sync(self):
        return f'postgresql+psycopg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    model_config = SettingsConfigDict(env_file='dev.env')

settings = Settings()