from fastapi import APIRouter
from app.routes.handlers import *

from app.routes.auth import auth_router

router = APIRouter()

router.include_router(auth_router)

router.get("/cities")(get_cities)
router.post("/create_trip")(create_trip)
router.get("/views")(trip_items_handler)
router.post("/create_view")(create_trip_item)
router.get("/tickets")(get_tickets)
