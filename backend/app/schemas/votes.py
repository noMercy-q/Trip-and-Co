from pydantic import BaseModel


class Vote(BaseModel):
    trip_item_id: int
