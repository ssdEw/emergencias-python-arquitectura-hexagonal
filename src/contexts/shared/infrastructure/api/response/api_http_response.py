from abc import ABC
from http import HTTPStatus
from typing import Any, Dict


class ApiHttpResponse(ABC):
    def __init__(
        self,
        data: Any,
        status_code: int = HTTPStatus.OK,
        headers: Dict[str, str] | None = None,
    ):
        self._data = data or {}
        self._status_code = status_code
        self._headers = headers or {}

    @property
    def data(self):
        return self._data

    @property
    def status_code(self) -> int:
        return self._status_code

    @property
    def headers(self) -> Dict[str, str]:
        return self._headers
