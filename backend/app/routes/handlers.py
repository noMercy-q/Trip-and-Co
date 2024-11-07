from fastapi import Request, Query
from app import db_service, schemas, aviasales_service, amadeus_service
from fastapi import Depends
import uuid
from app import db_service, schemas, aviasales_service
from app.routes.utils import get_current_user, generate_invite_token


async def get_cities():
    return await db_service.parse_cities_data()

# ??
# async def hotels_handler(trip: schemas.TripCreate):
#     return await db_service.create_trip(trip)

INVITE_TOKEN_LENGTH = 32

async def create_trip(trip: schemas.TripCreate, user: schemas.TokenPayloadData = Depends(get_current_user)):

    trip._invite_token = generate_invite_token(INVITE_TOKEN_LENGTH)
    trip._created_by = uuid.UUID(user.user_id)

    return await db_service.create_trip(trip)
#
# async def join_trip(invite_token: str = Query(), user: schemas.TokenPayloadData = Depends(get_current_user)):
#     get_trip_by_invite_token

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

async def get_votes(trip_item_id: int):
    return await db_service.get_votes(trip_item_id)

async def create_vote(vote: schemas.Vote, user: schemas.TokenPayloadData = Depends(get_current_user)):
    return await db_service.create_vote(vote, user.user_id)

async def get_comments(trip_item_id: int):
    return await db_service.get_comments(trip_item_id)

async def create_comment(trip_item_id: schemas.Comment,  user: schemas.TokenPayloadData = Depends(get_current_user)):
    return await db_service.create_comment(trip_item_id, user.user_id)