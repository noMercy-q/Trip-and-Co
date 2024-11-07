from pydantic import BaseModel


class Ticket(BaseModel):
    depart_date: str
    origin: str
    destination: str
    cost: str