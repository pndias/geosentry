from fastapi import APIRouter, Depends, Query
from typing import List
from sqlalchemy.orm import Session
from src.domain.entities import GeopoliticalEvent
from src.infrastructure.database.session import get_db
from src.infrastructure.database.repositories import SQLAlchemyEventRepository
from src.application.services.event_service import EventService
from src.domain.repositories import IEventRepository

router = APIRouter(
    prefix="/events",
    tags=["Geopolitical Events"]
)

def get_repository(db: Session = Depends(get_db)) -> IEventRepository:
    return SQLAlchemyEventRepository(db)

def get_service(repo: IEventRepository = Depends(get_repository)) -> EventService:
    return EventService(repo)

@router.get("", response_model=List[GeopoliticalEvent])
async def list_events(service: EventService = Depends(get_service)):
    """Retrieves the list of geopolitical events from the local database."""
    return service.list_events()

@router.get("/nearby", response_model=List[GeopoliticalEvent])
async def list_nearby_events(
    lat: float = Query(..., ge=-90, le=90),
    lon: float = Query(..., ge=-180, le=180),
    radius_km: float = Query(2000.0, gt=0, le=20100),
    service: EventService = Depends(get_service),
):
    """Returns events near a location, sorted by proximity."""
    return service.list_nearby(lat, lon, radius_km)
