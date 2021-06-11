from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    перечисляем набор параметром которыми хотим управлять
    """
    # defaults but will be overridden by .env
    server_host: str = "127.0.0.1"
    server_port: int = 8000
    database_url: str = 'sqlite:///./database.sqlite3'

    jwt_secret: str
    """
    from secrets import token_urlsafe
    token_urlsafe(32)
    """
    jwt_algorithm: str = 'HS256'
    jwt_expiration: int = 3600


settings = Settings(_env_file='.env', _env_file_encoding='utf-8')
