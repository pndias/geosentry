# src/domain/repositories.py
from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities import GeopoliticalEvent

class IEventRepository(ABC):
    @abstractmethod
    def list_all(self) -> List[GeopoliticalEvent]:
        """List all geopolitical events."""
        pass
        
    @abstractmethod
    def get_by_id(self, event_id: int) -> Optional[GeopoliticalEvent]:
        """Get a specific event by ID."""
        pass

    @abstractmethod
    def list_nearby(self, lat: float, lon: float, radius_km: float = 2000.0) -> List[GeopoliticalEvent]:
        """List events near a location, sorted by distance."""
        pass

    @abstractmethod
    def list_by_context(self, context: str) -> List[GeopoliticalEvent]:
        """List events filtered by context (e.g. Global Threats)."""
        pass

    @abstractmethod
    def create(self, event: GeopoliticalEvent) -> GeopoliticalEvent:
        """Create a new event."""
        pass
