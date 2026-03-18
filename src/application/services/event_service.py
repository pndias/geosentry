# src/application/services/event_service.py
from typing import List, Optional
from src.domain.repositories import IEventRepository
from src.domain.entities import GeopoliticalEvent

class EventService:
    def __init__(self, repository: IEventRepository):
        self.repository = repository
        
    def list_events(self) -> List[GeopoliticalEvent]:
        """Use case: List all geopolitical events."""
        return self.repository.list_all()

    def get_event(self, event_id: int) -> Optional[GeopoliticalEvent]:
        return self.repository.get_by_id(event_id)
