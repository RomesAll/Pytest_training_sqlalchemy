from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_HOST: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    DB_NAME: str
    DB_PORT: int
    DB_MODE: str

    @property
    def DATABASE_URL_sync(self):
        return f'postgresql+psycopg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    model_config = SettingsConfigDict(env_file='dev.env')

settings = Settings()