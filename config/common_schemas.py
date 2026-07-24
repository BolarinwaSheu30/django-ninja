from ninja import Schema
from typing import Any


class SuccessResponseSchema(Schema):
    status: str
    message: str
    data: Any = None


class ErrorResponseSchema(Schema):
    status: str
    message: str
    data: Any = None


