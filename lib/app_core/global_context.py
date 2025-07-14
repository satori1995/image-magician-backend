"""
创建全局 Context，协程隔离
"""
from contextvars import ContextVar
from lib.app_core.request_response_data import RequestData, ResponseData, MetricData
from lib.settings import SERVICE_NAME


class GlobalContext:

    def __init__(self):
        self._ctx = ContextVar(SERVICE_NAME)

    def set_storage_dict(self):
        self._ctx.set({})

    def set(self, key, value):
        self._ctx.get()[key] = value

    def get(self, key):
        return self._ctx.get()[key]

    def __contains__(self, key):
        return key in self._ctx.get({})

    @property
    def request_data(self) -> RequestData:
        return self._ctx.get()["request_data"]

    @property
    def response_data(self) -> ResponseData:
        return self._ctx.get()["response_data"]

    @property
    def metric_data(self) -> MetricData:
        return self._ctx.get()["metric_data"]


global_context = GlobalContext()

