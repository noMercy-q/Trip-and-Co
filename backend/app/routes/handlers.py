from fastapi import Request
from app import db_service, TripCreate


async def cities_handler():
    return await db_service.parse_cities_data()

async def create_trip(trip: TripCreate):
    return await db_service.create_trip(trip)