from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path



class Settings(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASW: int
    DB_HOST: str
    DB_PORT: int
    
    @property
    def db_url(self):
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASW}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
    
    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent.parent / '.env',
        extra='ignore' # Будет игнорировать все переменные из .env - если их не указать в классе настроек
        )
    
settings = Settings()