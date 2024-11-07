from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, PrivateAttr


class TripCreate(BaseModel):
    name: str
    origin_city_id: str
    dest_city_id: str
    _created_by: UUID = PrivateAttr()
    start_date: datetime
    end_date: datetime
    description: str | None = None
    _invite_token: str = PrivateAttr()

class Trip(BaseModel):
    id: int
    name: str
    origin_city_id: str
    dest_city_id: str
    created_by: UUID
    start_date: datetime
    end_date: datetime
    description: str | None = None
    invite_token: str
