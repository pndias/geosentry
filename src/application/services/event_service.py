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

    def list_nearby(self, lat: float, lon: float, radius_km: float = 2000.0) -> List[GeopoliticalEvent]:
        """Use case: List events near a geographic location."""
        return self.repository.list_nearby(lat, lon, radius_km)

    def get_event(self, event_id: int) -> Optional[GeopoliticalEvent]:
        return self.repository.get_by_id(event_id)

    def list_by_context(self, context: str) -> List[GeopoliticalEvent]:
        """Use case: List events filtered by context."""
        return self.repository.list_by_context(context)
