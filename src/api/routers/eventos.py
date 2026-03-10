from fastapi import APIRouter
from typing import List
from src.core.models import EventoGeopolitico
from src.api.services.evento_service import EventoService

router = APIRouter(
    prefix="/eventos",
    tags=["Eventos Geopolíticos"]
)

@router.get("", response_model=List[EventoGeopolitico])
async def listar_eventos():
    """
    Recupera a lista de eventos geopolíticos recentes.
    """
    return EventoService.get_mock_eventos()
