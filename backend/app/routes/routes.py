from fastapi import APIRouter
from app.routes.handlers import cities_handler, create_trip


router = APIRouter()

router.get("/cities")(cities_handler)
router.post("/create_trip")(create_trip)