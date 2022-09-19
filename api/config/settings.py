from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_CONN_URL: str = ''

    # Auth
    SECRET_KEY: str = ''
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_HOURS: int = 24


    class Config:
        env_file = '.env'


settings = Settings()
