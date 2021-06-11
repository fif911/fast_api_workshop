"""
DB file
session config
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .settings import settings

engine = create_engine(
    settings.database_url,
    connect_args={'check_same_thread': False}  # Это безопасно только благодаря тому как мы построим дальше работу
    # сессиями. Чтобы подключение не переиспользовалось
)

Session = sessionmaker(
    engine,
    autocommit=False,
    autoflush=False,
)


# def greeting(name: str) -> str: typing hint
# using dependency injection
def get_session() -> Session:
    session = Session()
    try:
        yield session
    finally:
        session.close()
