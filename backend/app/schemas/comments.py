from pydantic import BaseModel


class Comment(BaseModel):
    trip_item_id: int
    content: str