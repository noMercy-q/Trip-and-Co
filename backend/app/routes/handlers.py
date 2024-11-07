from fastapi import Request
from app import db_service, schemas


async def cities_handler():
    return await db_service.parse_cities_data()

async def hotels_handler(trip: schemas.TripCreate):
    return await db_service.create_trip(trip)
async def create_trip(trip: schemas.TripCreate):
    return await db_service.create_trip(trip)
async def create_trip_item(trip_item: schemas.TripItemCreate):
    return await db_service.create_trip_item(trip_item)
async def trip_items_handler():
    return await db_service.get_trip_items()
