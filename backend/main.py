import logging
from contextlib import asynccontextmanager

import uvicorn

from fastapi import FastAPI
from app.routes.routes import router
from app import db_client

log = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db_client.connect()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    uvicorn.run(app, host="0.0.0.0", port=8000)
