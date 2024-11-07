from os import sched_get_priority_max

from api_clients.aviasales_client import AviasalesClient
from db.models import Trip, City
from db.client import PostgresClient
from app import schemas


class AviasalesService:
    def __init__(self, aviasales_client: AviasalesClient, db_client: PostgresClient):
        self.client = aviasales_client
        self.db_client = db_client

    async def parse_tickets(self, trip_id):
        filters = {"id": trip_id}
        trip_data = await self.db_client.select_by_filter(Trip, filters)
        origin_city = trip_data[0].origin_city_id
        dest_city = trip_data[0].dest_city_id
        start_date = trip_data[0].start_date
        end_date = trip_data[0].end_date

        tickets_to_dest = await self.client.get_latest_prices(origin_city, dest_city, start_date.strftime('%Y-%m-%d'), (end_date - start_date).days)
        ticket_to_origin = await self.client.get_latest_prices(dest_city, origin_city, start_date.strftime('%Y-%m-%d'), (end_date - start_date).days)

        data = {
            "to_dest": [],
            "to_origin": []
        }
        for ticket in tickets_to_dest['data']:
            data["to_dest"].append(
                schemas.Ticket(
                    depart_date=ticket["depart_date"],
                    origin=ticket["origin"],
                    destination=ticket["destination"],
                    cost=f"{ticket["value"]} RUB"
                )
            )

        for ticket in ticket_to_origin['data']:
            data["to_origin"].append(
                schemas.Ticket(
                    depart_date=ticket["depart_date"],
                    origin=ticket["origin"],
                    destination=ticket["destination"],
                    cost=f"{ticket["value"]} RUB"
                )
            )

        return data
