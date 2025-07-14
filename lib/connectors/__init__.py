from redis import Redis
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from lib.connectors.database import MYSQL_SESSION, POSTGRES_SESSION, BaseModelType
from lib.connectors.cache import redis_conn


class Connectors:
    REDIS: Redis = redis_conn
    MYSQL: async_sessionmaker[AsyncSession] = MYSQL_SESSION
    POSTGRES: async_sessionmaker[AsyncSession] = POSTGRES_SESSION


