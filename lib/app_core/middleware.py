"""
定义一些中间件
"""
import time
from sanic import Request, HTTPResponse
from sanic_cors import CORS
from lib.app_core import app
from lib.app_core.global_context import global_context
from lib.app_core.request_response_data import (
    RequestData, ResponseData, MetricData
)


@app.middleware("request")
async def parse_request_data(request: Request):
    """
    解析请求数据，注入到全局上下文中
    """
    # 设置存储字典
    global_context.set_storage_dict()
    request_data = RequestData(request)
    response_data = ResponseData()
    metric_data = MetricData(start_time=int(time.time() * 1000))
    # 注入到全局上下文中
    global_context.set("request_data", request_data)
    global_context.set("response_data", response_data)
    global_context.set("metric_data", metric_data)


@app.middleware("response")
async def log_request(request: Request, response: HTTPResponse):
    """
    将整个请求的生命周期记录下来
    """
    request_data = global_context.request_data
    response_data = global_context.response_data
    metric_data = global_context.metric_data
    # 统计结束时间以及耗时
    end_time = int(time.time() * 1000)
    costs = end_time - metric_data.start_time
    metric_data.end_time = end_time
    metric_data.costs = costs
    # todo：记录请求信息


CORS(
    app,
    origins=["*"],
    methods=["*"],
    allow_headers=["*"]
)

