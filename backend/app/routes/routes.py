from fastapi import APIRouter
from app.routes.handlers import *


router = APIRouter()

router.get("/cities")(cities_handler)
router.post("/create_trip")(create_trip)
router.get("/views")(trip_items_handler)
router.post("/create_view")(create_trip_item)
