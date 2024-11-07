from datetime import datetime
from pydantic import BaseModel
from typing import Optional

from app import schemas

from db.client import PostgresClient
from db.models import Trip, City, TripItem


class PostgresService:
    def __init__(self, db_client: PostgresClient):
        self.client = db_client

    async def parse_cities_data(self):
        data = []
        cities = await self.client.select_all(City)

        for city in cities:
            data.append(
                schemas.City(
                    name=city.city_name,
                    code=city.city_id,
                ),
            )
        return data

    async def create_trip_item(self, trip_item: schemas.TripItemCreate):
        new_trip_item = TripItem(
            name=trip_item.name,
            type=trip_item.type,
            description= trip_item.description,
            details=trip_item.details,
            cost=trip_item.cost,
            link_url=trip_item.link_url,
            image_url=trip_item.image_url
        )
        return await self.client.create_record(new_trip_item)
    async def get_trip_items(self):
        return await self.client.select_all(TripItem)

    async def create_trip(self, trip: schemas.TripCreate):
        new_trip = Trip(
            name=trip.name,
            description=trip.description,
            origin_city_id=trip.origin_city_id,
            dest_city_id=trip.dest_city_id,
            created_by=trip.created_by,
            start_date=trip.start_date,
            end_date=trip.end_date,
            created_at=datetime.utcnow()
        )
        return await self.client.create_record(new_trip)
