from api_clients.aviasales_client import AviasalesClient


class AviasalesService:
    def __init__(self, aviasales_client: AviasalesClient):
        self.client = aviasales_client

    def parse_plains_data(self):
        pass