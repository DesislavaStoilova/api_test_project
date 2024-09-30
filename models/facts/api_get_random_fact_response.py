from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, StrictInt, StrictStr, StrictBool, Field


class Status(BaseModel):
    verified: Optional[StrictBool]
    sentCount: StrictInt


class Facts(BaseModel):
    status: Status
    id: StrictStr= Field(alias='_id')
    text: StrictStr
    type: StrictStr
    user: StrictStr
    deleted: StrictBool
    created_at: datetime = Field(alias='createdAt')
    updated_at: datetime = Field(alias='updatedAt')
    __v: StrictInt
    source: Optional[StrictStr] = None
    used: Optional[StrictBool] = None


class ApiGetRandomFactResponse(BaseModel):
    data: Facts | List[Facts]
    status_code: StrictInt
