from app.services.aviasales_service import AviasalesService
from api_clients.aviasales_client import AviasalesClient
from app.services.postgres_service import PostgresService, TripCreate
from db.client import PostgresClient

import os


# AVIA_TOKEN from https://app.travelpayouts.com/programs/100/tools/api
aviasales_client = AviasalesClient(os.environ.get("AVIA_TOKEN"))
aviasales_service = AviasalesService(aviasales_client)

db_client = PostgresClient()
db_service = PostgresService(db_client)