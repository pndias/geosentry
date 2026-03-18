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
    def create(self, event: GeopoliticalEvent) -> GeopoliticalEvent:
        """Create a new event."""
        pass
