# src/domain/repositories.py
from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities import EventoGeopolitico

class IEventoRepository(ABC):
    @abstractmethod
    def list_all(self) -> List[EventoGeopolitico]:
        """List all geopolitical events."""
        pass
        
    @abstractmethod
    def get_by_id(self, event_id: int) -> Optional[EventoGeopolitico]:
        """Get a specific event by ID."""
        pass

    @abstractmethod
    def create(self, event: EventoGeopolitico) -> EventoGeopolitico:
        """Create a new event."""
        pass
