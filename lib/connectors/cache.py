import redis.asyncio as redis
from lib.settings import REDIS_CONFIG

connection_pool = redis.ConnectionPool(**REDIS_CONFIG)
redis_conn = redis.Redis(connection_pool=connection_pool)

