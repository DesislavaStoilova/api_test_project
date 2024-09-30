from enum import IntEnum


class StatusCodeEnum(IntEnum):
    SUCCESS = 200
    CREATED = 201
    UNAUTHORIZED = 401
    FAIL = 500
