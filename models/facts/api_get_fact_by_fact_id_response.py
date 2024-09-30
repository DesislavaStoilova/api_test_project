from datetime import datetime
from typing import Optional

from pydantic import BaseModel, StrictInt, StrictStr, StrictBool, Field


class Name(BaseModel):
    first: StrictStr
    last: StrictStr


class User(BaseModel):
    _id: StrictStr
    name: Name
    photo: StrictStr


class Status(BaseModel):
    verified: Optional[StrictBool]
    sentCount: StrictInt


class Facts(BaseModel):
    status: Status
    id: StrictStr = Field(alias='_id')
    text: StrictStr
    type: StrictStr
    user: User
    deleted: StrictBool
    created_at: datetime = Field(alias='createdAt')
    updated_at: datetime = Field(alias='updatedAt')
    __v: StrictInt


class ApiGetFactByFactIDResponse(BaseModel):
    data: Facts
    status_code: StrictInt
