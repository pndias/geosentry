# src/infrastructure/database/models.py
from sqlalchemy import Column, Integer, String, Float, JSON
from src.infrastructure.database.session import Base

class EventDB(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    category = Column(String, index=True)
    analytical_summary = Column(String)
    lat = Column(Float, nullable=True, index=True)
    lon = Column(Float, nullable=True, index=True)
    impact = Column(Integer)
    context = Column(String, default="Regional", index=True)
    tags = Column(JSON)
    cited_sources = Column(JSON)
    date = Column(String)  # ISO Format: YYYY-MM-DD
    source_link = Column(String, nullable=True)
