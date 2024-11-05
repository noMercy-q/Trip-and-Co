import logging
import os

from fastapi import FastAPI

from api_clients.aviasales_client import AviasalesClient

log = logging.getLogger(__name__)

app = FastAPI()

# from https://app.travelpayouts.com/programs/100/tools/api
aviasales_client = AviasalesClient(os.environ.get("AVIA_TOKEN"))


@app.get("/")
async def root():
    return {"message": "Helsfhfhefejwlo World"}

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # TODO: add server start
