from app.routes import *
from app.services import *
from api_clients.aviasales_client import AviasalesClient

import os


# AVIA_TOKEN from https://app.travelpayouts.com/programs/100/tools/api
aviasales_client = AviasalesClient(os.environ.get("AVIA_TOKEN"))
aviasales_service = AviasalesService(aviasales_client)