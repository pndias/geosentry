# src/infrastructure/database/repositories.py
from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.repositories import IEventoRepository
from src.domain.entities import EventoGeopolitico, CategoriaEvento, Coordenadas
from src.infrastructure.database.models import EventoDB

class SQLAlchemyEventoRepository(IEventoRepository):
    def __init__(self, db: Session):
        self.db = db
    
    def list_all(self) -> List[EventoGeopolitico]:
        """Recupera os eventos do banco de dados local SQLite."""
        db_eventos = self.db.query(EventoDB).all()
        result = []
        for e in db_eventos:
            coordenadas = None
            if e.lat is not None and e.lon is not None:
                coordenadas = Coordenadas(lat=e.lat, lon=e.lon)
                
            result.append(
                EventoGeopolitico(
                    id=e.id,
                    titulo=e.titulo,
                    categoria=CategoriaEvento(e.categoria),
                    resumo_analitico=e.resumo_analitico,
                    coordenadas=coordenadas,
                    impacto=e.impacto,
                    tags=e.tags or [],
                    fontes_citadas=e.fontes_citadas or [],
                    data=e.data,
                    link_fonte=e.link_fonte
                )
            )
        return result
    
    def get_by_id(self, event_id: int) -> Optional[EventoGeopolitico]:
        # Implementação básica, pode ser expandida
        e = self.db.query(EventoDB).filter(EventoDB.id == event_id).first()
        if not e:
            return None
            
        coordenadas = None
        if e.lat is not None and e.lon is not None:
            coordenadas = Coordenadas(lat=e.lat, lon=e.lon)
            
        return EventoGeopolitico(
            id=e.id,
            titulo=e.titulo,
            categoria=CategoriaEvento(e.categoria),
            resumo_analitico=e.resumo_analitico,
            coordenadas=coordenadas,
            impacto=e.impacto,
            tags=e.tags or [],
            fontes_citadas=e.fontes_citadas or [],
            data=e.data,
            link_fonte=e.link_fonte
        )

    def create(self, event: EventoGeopolitico) -> EventoGeopolitico:
        # Implementação se necessário
        pass
