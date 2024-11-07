from fastapi import Request, Query
from starlette.status import HTTP_404_NOT_FOUND

from app import db_service, schemas, aviasales_service, amadeus_service
from fastapi import Depends, HTTPException
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
    user_id = uuid.UUID(user.user_id)

    trip._invite_token = generate_invite_token(INVITE_TOKEN_LENGTH)
    trip._created_by = user_id
    created_trip = await db_service.create_trip(trip)

    await db_service.add_participant(user_id, created_trip.id)

    await amadeus_service.get_hotels(created_trip.id, created_trip.dest_city_id)
    return created_trip
#
async def join_trip(invite_token: str = Query(), user: schemas.TokenPayloadData = Depends(get_current_user)):
    trips = await db_service.get_trips(invite_token=invite_token)

    if len(trips) < 1:
        return HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail="Trip not found",
        )

    current_trip = trips[0]

    user_id = uuid.UUID(user.user_id)

    await db_service.add_participant(user_id, current_trip.id)

    return {
        "status": "success"
    }

async def get_trips(
        trip_id: int = Query(None),
        invite_token: str = Query(None),
        participant: bool = Query(None),
        user: schemas.TokenPayloadData = Depends(get_current_user)):

    filters = dict()

    if trip_id:
        filters['id'] = trip_id

    if invite_token:
        filters['invite_token'] = invite_token

    trips = await db_service.get_trips(**filters)

    if participant:
        user_participants = await db_service.get_user_participants(uuid.UUID(user.user_id))
        print("user_part in ", user_participants)
        print("all trips", trips)
        trips = [trip for trip in trips if trip.id in user_participants]

    return trips

async def create_trip_item(trip_item: schemas.TripItemCreate):
    return await  db_service.create_trip_item(trip_item)


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

async def top_options(trip_id: int):
    best_tickets_data = await aviasales_service.get_best_tickets_data(trip_id)
    return await db_service.top_options(trip_id, best_tickets_data)