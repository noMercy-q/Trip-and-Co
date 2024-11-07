from datetime import datetime
from uuid import UUID
from pydantic import BaseModel


class TripCreate(BaseModel):
    name: str
    origin_city_id: str
    dest_city_id: str
    created_by: UUID
    start_date: datetime
    end_date: datetime
    description: str | None = None
