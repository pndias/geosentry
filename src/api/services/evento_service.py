from typing import List
from sqlalchemy.orm import Session
from src.core.models import EventoGeopolitico, CategoriaEvento, Coordenadas
from src.api.models_db import EventoDB

class EventoService:
    @staticmethod
    def get_eventos_db(db: Session) -> List[EventoGeopolitico]:
        """
        Recupera os eventos do banco de dados local SQLite.
        """
        db_eventos = db.query(EventoDB).all()
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
