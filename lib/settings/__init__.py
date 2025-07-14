"""
配置项目
"""
SERVICE_NAME = "sanic-service-template"

# Postgres
POSTGRES_CONFIG = {
    "drivername": "postgresql+asyncpg",
    "host": "58.87.66.219",
    "port": 5432,
    "username": "postgres",
    "password": "zgghyYs123",
    "database": "postgres",
}

# MySQL
MYSQL_CONFIG = {
    "drivername": "mysql+asyncmy",
    "host": "58.87.66.219",
    "port": 3306,
    "username": "root",
    "password": "zgghyYs123",
    "database": "temp",
}

# Redis
REDIS_CONFIG = {
    "host": "r-rj9z0semb98rk3qb59.redis.rds.aliyuncs.com",
    "port": 6379,
    "password": "redis_rw:X6v8TGiqyS5VvL",
    "db": 2,
    "decode_responses": True,
}





