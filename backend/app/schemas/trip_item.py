from datetime import datetime
from db.models import TripItemsTypes
from pydantic import BaseModel


class TripItem(BaseModel):
    id:int
    trip_id: int
    name: str
    type: TripItemsTypes
    description: str | None = None
    details: dict | None = None
    cost: int =0
    link_url: str | None = None
    image_url: str | None = None
class TripItemCreate(BaseModel):
    name: str
    trip_id: int
    type: TripItemsTypes
    description: str | None = None
    details: dict | None = None
    cost: int =0
    link_url: str | None = None
    image_url: str | None = None




