from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from src.core.models import EventoGeopolitico
from src.api.services.evento_service import EventoService
from src.api.database import get_db

router = APIRouter(
    prefix="/eventos",
    tags=["Eventos Geopolíticos"]
)

@router.get("", response_model=List[EventoGeopolitico])
async def listar_eventos(db: Session = Depends(get_db)):
    """
    Recupera a lista de eventos geopolíticos diretamente do banco de dados local.
    """
    return EventoService.get_eventos_db(db)
