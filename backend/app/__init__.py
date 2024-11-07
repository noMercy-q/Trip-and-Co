from app.services.auth_service import AuthService
from app.services.aviasales_service import AviasalesService
from api_clients.aviasales_client import AviasalesClient
from app.services.postgres_service import PostgresService
from db.client import PostgresClient

import os

from db.user_repo import UserRepository

from dotenv import load_dotenv

from api_clients.amadeus_client import AmadeusClient
from app.services.amadeus_service import AmadeusService

load_dotenv()  # take environment variables from .env.

db_client = PostgresClient()
db_service = PostgresService(db_client)

# AVIA_TOKEN from https://app.travelpayouts.com/programs/100/tools/api
aviasales_client = AviasalesClient(os.environ.get("AVIA_TOKEN"))
amadeus_client = AmadeusClient()
aviasales_service = AviasalesService(aviasales_client, db_client)
amadeus_service = AmadeusService(amadeus_client,db_service)

user_repo = UserRepository(db_client)
auth_service = AuthService(user_repo)
