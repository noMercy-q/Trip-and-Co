from http.client import HTTPException
from typing import Optional

from fastapi import APIRouter
from app.routes.handlers import *

from app.routes.auth import auth_router

router = APIRouter()

router.include_router(auth_router)

router.get("/cities")(get_cities)
router.post("/create_trip")(create_trip)
@router.get("/views/")
async def get_trip_items(trip_id: Optional[int] = None):
    if trip_id is None:
        raise HTTPException(status_code=400, detail="trip_id query parameter is required")
    return await trip_items_handler(trip_id)

@router.get("/hotels/")
async def get_trip_items(trip_id: Optional[int] = None):
    if trip_id is None:
        raise HTTPException(status_code=400, detail="trip_id query parameter is required")
    return await hotel_handler(trip_id)

router.post("/create_view")(create_trip_item)
router.get("/tickets")(get_tickets)
router.get("/votes")(get_votes)
router.post("/votes")(create_vote)
router.get("/comments")(get_comments)
router.post("/comments")(create_comment)
router.get("/top_options")(top_options)