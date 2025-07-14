"""
handle 程序中出现的异常
当视图函数执行出错时，会进入和异常匹配的 handler
"""
import traceback
from sanic import Request, NotFound, MethodNotAllowed, SanicException
from lib.app_core import app
from lib.app_core.global_context import global_context


@app.exception(NotFound, MethodNotAllowed)
async def handle_route_not_found_exception(request: Request, exception):
    """
    处理路由不存在、以及 HTTP 方法错误时的异常
    """
    method = request.method
    path = request.path
    global_context.response_data.set(
        code=404,
        data={},
        error_message=f"`{method} {path}` cannot be routed to any existing view",
        traceback=traceback.format_exc(),
    )
    return global_context.response_data.response


@app.exception(SanicException)
async def handler_sanic_exception(request: Request, exception: SanicException):
    """
    将已知的异常转成 SanicException
    """
    global_context.response_data.set(
        code=500,
        data={},
        error_message=exception.message,
        traceback=traceback.format_exc(),
    )
    return global_context.response_data.response


@app.exception(Exception)
async def handle_exception_exception_exception(request: Request, exception):
    """
    处理未知异常
    """
    global_context.response_data.set(
        code=500,
        data={},
        error_message="An error occurred while executing the service. Please contact the developer",
        traceback=traceback.format_exc(),
    )
    return global_context.response_data.response

