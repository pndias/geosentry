# src/application/services/event_service.py
from typing import List, Optional
from src.domain.repositories import IEventoRepository
from src.domain.entities import EventoGeopolitico

class EventService:
    def __init__(self, repository: IEventoRepository):
        self.repository = repository
        
    def list_events(self) -> List[EventoGeopolitico]:
        """
        Use case: List all geopolitical events.
        """
        return self.repository.list_all()

    def get_event(self, event_id: int) -> Optional[EventoGeopolitico]:
        return self.repository.get_by_id(event_id)
