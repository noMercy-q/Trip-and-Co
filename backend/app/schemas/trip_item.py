from datetime import datetime
from db.models import TripItemsTypes
from pydantic import BaseModel


class Trip(BaseModel):
    id:str
    name: str
    type: TripItemsTypes
    description: str | None = None
    details: dict | None = None
    cost: int =0
    link_url: str | None = None
    image_url: str | None = None
class TripItemCreate(BaseModel):
    name: str
    type: TripItemsTypes
    description: str | None = None
    details: dict | None = None
    cost: int =0
    link_url: str | None = None
    image_url: str | None = None




