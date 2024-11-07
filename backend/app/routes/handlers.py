from fastapi import Request
from backend.app import db_service, schemas, aviasales_service, amadeus_sevice


async def get_cities():
    return await db_service.parse_cities_data()

async def hotels_handler(trip: schemas.TripCreate):
    return await db_service.create_trip(trip)

async def create_trip(trip: schemas.TripCreate):
    amadeus_sevice.
    return await db_service.create_trip(trip)

async def create_trip_item(trip_item: schemas.TripItemCreate):
    return await db_service.create_trip_item(trip_item)

async def trip_items_handler(trip_id: int):
    return await db_service.get_trip_items("view", trip_id)

async def hotel_handler(trip_id: int):
    return await db_service.get_trip_items("hotel",trip_id)
async def get_tickets(trip_id: int):
    return await aviasales_service.parse_tickets(trip_id)