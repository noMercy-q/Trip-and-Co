from fastapi import Request
from app import db_service, schemas


async def cities_handler():
    return await db_service.parse_cities_data()

async def create_trip(trip: schemas.TripCreate):
    return await db_service.create_trip(trip)