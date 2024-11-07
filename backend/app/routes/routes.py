from fastapi import APIRouter
from app.routes.handlers import *


router = APIRouter()

router.get("/cities")(cities_handler)
router.post("/create_trip")(create_trip)
router.get("/trip_item")(trip_items_handler)
router.post("/trip_item")(create_trip_item)
