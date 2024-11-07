import logging

from fastapi import Response

from app import schemas

from db.client import PostgresClient
from db.models import *

from db.models import TripItemsTypes

log = logging.getLogger(__name__)
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
            trip_id=trip_item.trip_id,
            type=trip_item.type,
            description= trip_item.description,
            details=trip_item.details,
            cost=trip_item.cost,
            link_url=trip_item.link_url,
            image_url=trip_item.image_url
        )
        return await self.client.create_record(new_trip_item)

    async def get_trip_items(self, item_type: TripItemsTypes, trip_id: int):
        data =[]
        trip_items = await self.client.select_by_filter(TripItem, {"type": item_type, "trip_id": trip_id})
        try:
            for trip_item in trip_items:
                data.append(
                    schemas.TripItem(
                        id= trip_item.id,
                        trip_id= int(trip_item.trip_id),
                        name =trip_item.name,
                        type=trip_item.type,
                        descriptrion=trip_item.description,
                        details=trip_item.details,
                        cost=trip_item.cost,
                        link_url=trip_item.link_url,
                        image_url=trip_item.image_url
                        ),
                    )

        except TypeError as e:
            pass
        return data

    async def create_trip(self, trip: schemas.TripCreate):
        new_trip = Trip(
            name=trip.name,
            description=trip.description,
            origin_city_id=trip.origin_city_id,
            dest_city_id=trip.dest_city_id,
            created_by=trip._created_by,
            start_date=trip.start_date,
            end_date=trip.end_date,
            created_at=datetime.utcnow(),
            invite_token=trip._invite_token,
        )
        return await self.client.create_record(new_trip)

    async def get_user_participants(self, user_id: uuid.UUID):
        filter = {
            "user_id": user_id,
        }
        participants: list[TripParticipant] | None = await self.client.select_by_filter(TripParticipant, filter)

        if not participants:
            return []

        return [part.trip_id for part in participants]

    async def get_trips(self, **kwargs):
        trips: list[Trip] | None = await self.client.select_by_filter(Trip, kwargs)

        if not trips:
            return []

        return [schemas.Trip(
            id=trip.id,
            name=trip.name,
            description=trip.description,
            origin_city_id=trip.origin_city_id,
            dest_city_id=trip.dest_city_id,
            created_by=trip.created_by,
            start_date=trip.start_date,
            end_date=trip.end_date,
            created_at=trip.created_at,
            invite_token=trip.invite_token,
        ) for trip in trips]

    async def add_participant(self, user_id: uuid.UUID, trip_id: int):
        await self.client.create_record(TripParticipant(
            user_id=user_id,
            trip_id=trip_id,
        ))

    async def get_votes(self, trip_item_id):
        filters = {"trip_item_id": trip_item_id}
        votes_count = await self.client.select_by_filter(Vote, filters, count_only=True)

        return Response(content=str(votes_count), media_type="text/plain")


    async def create_vote(self, vote: schemas.Vote, user_id: str):
        new_vote = Vote(
            user_id=user_id,
            trip_item_id=vote.trip_item_id,
            created_at=datetime.utcnow()
        )

        return await self.client.create_record(new_vote)

    async def get_comments(self, trip_item_id):
        filters = {"trip_item_id": trip_item_id}
        comments = await self.client.select_with_join(Comment, "user_id", User, "id", filters)

        comments.sort(key=lambda x: x[0].created_at)
        data = []
        for comment_user in comments:
            data.append(
                {
                    "user_id": comment_user[0].user_id,
                    "name": comment_user[1].name,
                    "trip_item_id": comment_user[0].trip_item_id,
                    "created_at": comment_user[0].created_at
                }
            )

        return data

    async def create_comment(self, comment: schemas.Comment, user_id: str):
        new_comment = Comment(
            user_id=user_id,
            trip_item_id=comment.trip_item_id,
            content=comment.content,
            created_at=datetime.utcnow()
        )

        return await self.client.create_record(new_comment)

    async def top_options(self, trip_id, best_tickets_data):
        filters = {"trip_id": trip_id, "type": "hotel"}
        top_hotel_id, votes_count = await self.client.select_with_join_and_group_by(TripItem, "id", Vote, "trip_item_id", filters, "id")
        trip_item = await self.client.select_by_filter(TripItem, {"id": top_hotel_id})
        trip_item = trip_item[0]
        random_users = await self.client.select_all(User)

        return {
            "hotel": trip_item.name,
            "total_cost": trip_item.cost + best_tickets_data["cost"],
            "dates": f"{best_tickets_data["depart_date"]} to {best_tickets_data["return_data"]}",
            "participants": [user.name for user in random_users[:3]]
        }

