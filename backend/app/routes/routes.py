from fastapi import APIRouter
from app.routes.handlers import *

from app.routes.auth import auth_router

router = APIRouter()

router.include_router(auth_router)

router.get("/cities")(get_cities)
router.post("/create_trip")(create_trip)
@router.get("/views/{trip_id}")
async def get_trip_items(trip_id: int):
    return await trip_items_handler(trip_id)

@router.get("/hotels/{trip_id}")
async def get_trip_items(trip_id: int):
    return await hotel_handler(trip_id)
router.post("/create_view")(create_trip_item)
router.get("/tickets")(get_tickets)
