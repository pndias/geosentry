# © 2026 Pablo Dias. Todos os direitos reservados.

from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field

class CategoriaEvento(str, Enum):
    MILITAR = "Militar"
    POLITICA = "Politica"
    ECONOMICA = "Economica"
    RELIGIOSA_SIMBOLICA = "Religiosa/Simbólica"

class Coordenadas(BaseModel):
    lat: float = Field(..., description="Latitude decimal do local do evento")
    lon: float = Field(..., description="Longitude decimal do local do evento")

class EventoGeopolitico(BaseModel):
    id: Optional[int] = Field(None, description="ID único opcional")
    titulo: str = Field(..., description="Título conciso do evento")
    categoria: CategoriaEvento = Field(..., description="Classificação temática")
    resumo_analitico: str = Field(..., description="Análise resumida das implicações")
    coordenadas: Optional[Coordenadas] = Field(None, description="Localização geográfica")
    impacto: int = Field(..., ge=1, le=5, description="Impacto global de 1 a 5")
    tags: List[str] = Field(default_factory=list)
    fontes_citadas: List[str] = Field(default_factory=list)
    data: Optional[str] = Field(None, description="Data do evento em formato ISO (YYYY-MM-DD)")
    link_fonte: Optional[str] = Field(None, description="Link para a fonte original do evento")
