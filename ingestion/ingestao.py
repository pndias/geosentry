import asyncio
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field, ValidationError

class CategoriaEvento(str, Enum):
    MILITAR = "Militar"
    POLITICA = "Politica"
    ECONOMICA = "Economica"
    RELIGIOSA_SIMBOLICA = "Religiosa/Simbólica"

class Coordenadas(BaseModel):
    lat: float = Field(..., description="Latitude decimal do local do evento")
    lon: float = Field(..., description="Longitude decimal do local do evento")

class EventoGeopolitico(BaseModel):
    titulo: str = Field(..., description="Título conciso do evento extraído")
    categoria: CategoriaEvento = Field(..., description="Classificação temática do evento")
    resumo_analitico: str = Field(..., description="Análise resumida do evento e suas implicações imediatas")
    coordenadas: Optional[Coordenadas] = Field(None, description="Localização geográfica opcional (lat/lon)")
    impacto: int = Field(..., ge=1, le=5, description="Nível de impacto global de 1 (baixo) a 5 (crítico)")
    tags: List[str] = Field(default_factory=list, description="Lista de palavras-chave relacionadas ao evento")
    fontes_citadas: List[str] = Field(default_factory=list, description="Lista de URLs ou nomes de agências de notícias mencionadas")

async def extrair_dados_texto(texto: str) -> EventoGeopolitico:
    """
    Simula a extração estruturada de dados a partir de um texto bruto usando um LLM.
    """
    # Simulação de latência de processamento do LLM
    await asyncio.sleep(1)
    
    # Dados mockados que seriam retornados pelo LLM após o parsing
    mock_data = {
        "titulo": "Escalada de Tensões no Estreito de Ormuz",
        "categoria": "Militar",
        "resumo_analitico": "Movimentação naval atípica e exercícios de prontidão aumentam o risco de bloqueio comercial.",
        "coordenadas": {"lat": 26.56, "lon": 56.25},
        "impacto": 4,
        "tags": ["marítimo", "petróleo", "Irã", "manobras"],
        "fontes_citadas": ["Reuters", "Al Jazeera"]
    }
    
    try:
        evento = EventoGeopolitico(**mock_data)
        return evento
    except ValidationError as e:
        print(f"Erro na validação do schema: {e}")
        raise

if __name__ == "__main__":
    async def main():
        texto_exemplo = "Relatos de frotas navais se aproximando do Estreito de Ormuz..."
        try:
            resultado = await extrair_dados_texto(texto_exemplo)
            print(resultado.model_dump_json(indent=2))
        except Exception as e:
            print(f"Falha na extração: {e}")

    asyncio.run(main())
