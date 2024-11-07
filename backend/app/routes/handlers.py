from fastapi import Request
from app import db_service, schemas, aviasales_service, amadeus_service
from fastapi import Depends
from app import db_service, schemas, aviasales_service
from app.routes.utils import get_current_user


async def get_cities():
    return await db_service.parse_cities_data()

# ??
# async def hotels_handler(trip: schemas.TripCreate):
#     return await db_service.create_trip(trip)

async def create_trip(trip: schemas.TripCreate):
    return await db_service.create_trip(trip)

async def create_trip_item(trip_item: schemas.TripItemCreate):
    created_trip = db_service.create_trip_item(trip_item)
    # await amadeus_service.send_trip_item(trip_item["id"], trip_item["dest_city_id"])
    return created_trip
async def trip_items_handler(trip_id: int):
    return await db_service.get_trip_items("view", trip_id)

async def hotel_handler(trip_id: int):
    return await db_service.get_trip_items("hotel",trip_id)
async def get_tickets(trip_id: int):
    return await aviasales_service.parse_tickets(trip_id)

async def create_vote(vote: schemas.Vote, user: schemas.TokenPayloadData = Depends(get_current_user)):
    return await db_service.create_vote(vote, user.user_id)
