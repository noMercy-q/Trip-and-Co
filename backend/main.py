import logging

from fastapi import FastAPI
from app.routes.base import router


log = logging.getLogger(__name__)

app = FastAPI()
app.include_router(router)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # TODO: add server start
