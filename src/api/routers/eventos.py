from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from src.domain.entities import EventoGeopolitico
from src.infrastructure.database.session import get_db
from src.infrastructure.database.repositories import SQLAlchemyEventoRepository
from src.application.services.event_service import EventService
from src.domain.repositories import IEventoRepository

router = APIRouter(
    prefix="/eventos",
    tags=["Eventos Geopolíticos"]
)

def get_repository(db: Session = Depends(get_db)) -> IEventoRepository:
    return SQLAlchemyEventoRepository(db)

def get_service(repo: IEventoRepository = Depends(get_repository)) -> EventService:
    return EventService(repo)

@router.get("", response_model=List[EventoGeopolitico])
async def listar_eventos(service: EventService = Depends(get_service)):
    """
    Recupera a lista de eventos geopolíticos diretamente do banco de dados local.
    """
    return service.list_events()
