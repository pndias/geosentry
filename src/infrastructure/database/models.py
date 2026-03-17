# src/infrastructure/database/models.py
from sqlalchemy import Column, Integer, String, Float, JSON
from src.infrastructure.database.session import Base

class EventoDB(Base):
    __tablename__ = "eventos"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    categoria = Column(String, index=True)
    resumo_analitico = Column(String)
    lat = Column(Float, nullable=True)
    lon = Column(Float, nullable=True)
    impacto = Column(Integer)
    tags = Column(JSON)
    fontes_citadas = Column(JSON)
    data = Column(String)  # ISO Format: YYYY-MM-DD
    link_fonte = Column(String, nullable=True)
