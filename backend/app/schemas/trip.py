from datetime import datetime

from pydantic import BaseModel


class TripCreate(BaseModel):
    name: str
    origin_city_id: str
    dest_city_id: str
    created_by: int
    start_date: datetime
    end_date: datetime
    description: str | None = None
