# src/infrastructure/database/repositories.py
from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.repositories import IEventRepository
from src.domain.entities import GeopoliticalEvent, EventCategory, Coordinates
from src.infrastructure.database.models import EventDB

class SQLAlchemyEventRepository(IEventRepository):
    def __init__(self, db: Session):
        self.db = db
    
    def list_all(self) -> List[GeopoliticalEvent]:
        """Retrieves events from the local SQLite database."""
        db_events = self.db.query(EventDB).all()
        result = []
        for e in db_events:
            coordinates = None
            if e.lat is not None and e.lon is not None:
                coordinates = Coordinates(lat=e.lat, lon=e.lon)
                
            result.append(
                GeopoliticalEvent(
                    id=e.id,
                    title=e.title,
                    category=EventCategory(e.category),
                    analytical_summary=e.analytical_summary,
                    coordinates=coordinates,
                    impact=e.impact,
                    tags=e.tags or [],
                    cited_sources=e.cited_sources or [],
                    date=e.date,
                    source_link=e.source_link
                )
            )
        return result
    
    def get_by_id(self, event_id: int) -> Optional[GeopoliticalEvent]:
        e = self.db.query(EventDB).filter(EventDB.id == event_id).first()
        if not e:
            return None
            
        coordinates = None
        if e.lat is not None and e.lon is not None:
            coordinates = Coordinates(lat=e.lat, lon=e.lon)
            
        return GeopoliticalEvent(
            id=e.id,
            title=e.title,
            category=EventCategory(e.category),
            analytical_summary=e.analytical_summary,
            coordinates=coordinates,
            impact=e.impact,
            tags=e.tags or [],
            cited_sources=e.cited_sources or [],
            date=e.date,
            source_link=e.source_link
        )

    def create(self, event: GeopoliticalEvent) -> GeopoliticalEvent:
        pass
