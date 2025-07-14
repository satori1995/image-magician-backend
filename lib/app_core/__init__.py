"""
创建 Sanic APP
"""
import sys
import asyncio
from sanic import Sanic
from lib.app_core.global_context import global_context
from lib.settings import SERVICE_NAME

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = Sanic(SERVICE_NAME)


# 心跳检测，用于验证服务是否正常
@app.get("/state/healthcheck")
async def healthcheck(_):
    global_context.response_data.set(
        code=200,
        data={},
        error_message="",
        traceback=""
    )
    return global_context.response_data.response
