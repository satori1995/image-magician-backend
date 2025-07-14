"""
定义请求数据结构、响应数据结构等
"""
from urllib.parse import parse_qs
from dataclasses import dataclass
import orjson
from sanic import Request, HTTPResponse
from sanic.request import File, RequestParameters


@dataclass
class RequestData:
    request: Request
    _query = None
    _form = None
    _json = None
    _files = None

    @property
    def query(self) -> dict[str, list[str]]:  # 查询参数
        if self._query is None:
            self._query = parse_qs(self.request.query_string)
        return self._query

    @property
    def form(self) -> RequestParameters:  # 请求体（表单）
        if self._form is None:
            self._form = self.request.form
        return self._form

    @property
    def json(self) -> dict:  # 请求体（JSON）
        if self._json is None:
            self._json = orjson.loads(self.request.body or b"{}")
        return self._json

    @property
    def files(self) -> dict[str, list[File]]:  # 文件
        if self._files is None:
            self._files = self.request.files
        return self._files


@dataclass
class ResponseData:
    code: int = None
    data: dict = None
    error_message: str = None
    traceback: str = None

    def set(self, code: int, data: dict, error_message: str = "", traceback: str = ""):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.traceback = traceback

    @property
    def response(self) -> HTTPResponse:
        return HTTPResponse(
            body=orjson.dumps(
                {"code": self.code,
                 "data": self.data,
                 "error_message": self.error_message,
                 "traceback": self.traceback}
            ),
            status=self.code,
            content_type="application/json",
        )


@dataclass
class MetricData:
    start_time: int = None
    end_time: int = None
    costs: int = None

