# src/domain/entities.py
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field

class EventCategory(str, Enum):
    MILITARY = "Military"
    POLITICAL = "Political"
    ECONOMIC = "Economic"
    RELIGIOUS_SYMBOLIC = "Religious/Symbolic"

class Coordinates(BaseModel):
    lat: float = Field(..., description="Decimal latitude of the event location")
    lon: float = Field(..., description="Decimal longitude of the event location")

class GeopoliticalEvent(BaseModel):
    id: Optional[int] = Field(None, description="Optional unique ID")
    title: str = Field(..., description="Concise event title")
    category: EventCategory = Field(..., description="Thematic classification")
    analytical_summary: str = Field(..., description="Summarized analysis of implications")
    coordinates: Optional[Coordinates] = Field(None, description="Geographic location")
    impact: int = Field(..., ge=1, le=5, description="Global impact from 1 to 5")
    tags: List[str] = Field(default_factory=list)
    cited_sources: List[str] = Field(default_factory=list)
    date: Optional[str] = Field(None, description="Event date in ISO format (YYYY-MM-DD)")
    source_link: Optional[str] = Field(None, description="Link to the original event source")
