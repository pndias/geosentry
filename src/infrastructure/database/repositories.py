# src/infrastructure/database/repositories.py
from typing import List, Optional
from math import radians, cos
from sqlalchemy.orm import Session
from sqlalchemy import func
from src.domain.repositories import IEventRepository
from src.domain.entities import GeopoliticalEvent, EventCategory, Coordinates
from src.infrastructure.database.models import EventDB

class SQLAlchemyEventRepository(IEventRepository):
    def __init__(self, db: Session):
        self.db = db

    def _to_entity(self, e: EventDB) -> GeopoliticalEvent:
        coordinates = None
        if e.lat is not None and e.lon is not None:
            coordinates = Coordinates(lat=e.lat, lon=e.lon)
        return GeopoliticalEvent(
            id=e.id, title=e.title,
            category=EventCategory(e.category),
            analytical_summary=e.analytical_summary,
            coordinates=coordinates, impact=e.impact,
            tags=e.tags or [], cited_sources=e.cited_sources or [],
            date=e.date, source_link=e.source_link,
        )
    
    def list_all(self) -> List[GeopoliticalEvent]:
        return [self._to_entity(e) for e in self.db.query(EventDB).all()]

    def list_nearby(self, lat: float, lon: float, radius_km: float = 2000.0) -> List[GeopoliticalEvent]:
        # Approximate bounding box to pre-filter with indexed columns
        km_per_deg_lat = 111.0
        km_per_deg_lon = 111.0 * cos(radians(lat))
        dlat = radius_km / km_per_deg_lat
        dlon = radius_km / max(km_per_deg_lon, 0.01)

        rows = (
            self.db.query(EventDB)
            .filter(
                EventDB.lat.isnot(None),
                EventDB.lon.isnot(None),
                EventDB.lat.between(lat - dlat, lat + dlat),
                EventDB.lon.between(lon - dlon, lon + dlon),
            )
            .all()
        )

        # Haversine-sort in Python (SQLite lacks trig functions)
        from math import sin, sqrt, atan2
        def haversine(e: EventDB) -> float:
            r = 6371.0
            la1, la2 = radians(lat), radians(e.lat)
            dla = radians(e.lat - lat)
            dlo = radians(e.lon - lon)
            a = sin(dla / 2) ** 2 + cos(la1) * cos(la2) * sin(dlo / 2) ** 2
            return 2 * r * atan2(sqrt(a), sqrt(1 - a))

        rows.sort(key=haversine)
        return [self._to_entity(e) for e in rows]
    
    def get_by_id(self, event_id: int) -> Optional[GeopoliticalEvent]:
        e = self.db.query(EventDB).filter(EventDB.id == event_id).first()
        if not e:
            return None
        return self._to_entity(e)

    def create(self, event: GeopoliticalEvent) -> GeopoliticalEvent:
        pass
