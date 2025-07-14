"""
数据库驱动
"""
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncEngine,
    async_sessionmaker,
)
from sqlalchemy.orm import declarative_base
from sqlalchemy.engine.url import URL
from lib.settings import MYSQL_CONFIG, POSTGRES_CONFIG

BaseModelType = declarative_base()

# MySQL
MYSQL_ENGINE: AsyncEngine = create_async_engine(
    URL.create(**MYSQL_CONFIG)
)
MYSQL_SESSION = async_sessionmaker(bind=MYSQL_ENGINE, expire_on_commit=False)

# Postgres
POSTGRES_ENGINE: AsyncEngine = create_async_engine(
    URL.create(**POSTGRES_CONFIG)
)
POSTGRES_SESSION = async_sessionmaker(bind=POSTGRES_ENGINE, expire_on_commit=False)

