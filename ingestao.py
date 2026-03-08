import asyncio
import json
from enum import Enum
from typing import Dict
from pydantic import BaseModel, Field, ValidationError

class CategoriaNoticia(str, Enum):
    """Categorias permitidas para as notícias geopolíticas."""
    MILITAR = "Militar"
    POLITICA = "Politica"
    ECONOMICA = "Economica"

class Coordenadas(BaseModel):
    """Representação geográfica de latitude e longitude."""
    lat: float = Field(..., description="Latitude do evento")
    long: float = Field(..., description="Longitude do evento")

class NoticiaExtraida(BaseModel):
    """Schema Pydantic para estruturação de dados extraídos de notícias."""
    titulo: str = Field(..., min_length=5, description="Título resumido da notícia")
    categoria: CategoriaNoticia = Field(..., description="Categoria predominante do evento")
    resumo: str = Field(..., description="Resumo executivo do impacto geopolítico")
    coordenadas: Coordenadas = Field(..., description="Dicionário com latitude e longitude")
    impacto: int = Field(..., ge=1, le=5, description="Grau de impacto geopolítico de 1 a 5")

async def extrair_noticia_llm_simulacao(texto_bruto: str) -> NoticiaExtraida:
    """
    Simula uma chamada assíncrona a um Modelo de Linguagem (LLM) 
    para processar texto bruto e retornar um objeto validado pelo Pydantic.
    """
    print(f"[Simulação LLM] Processando: {texto_bruto[:50]}...")
    
    # Simula latência de rede/processamento
    await asyncio.sleep(1.5)
    
    # Resposta mockada que o LLM retornaria em JSON após o parsing
    mock_llm_response = {
        "titulo": "Escalada de tensões no Estreito de Ormuz",
        "categoria": "Militar",
        "resumo": "Movimentação naval atípica detectada após exercícios conjuntos na região.",
        "coordenadas": {"lat": 26.56, "long": 56.25},
        "impacto": 4
    }
    
    try:
        # Instancia e valida os dados conforme o schema definido
        noticia = NoticiaExtraida(**mock_llm_response)
        return noticia
    except ValidationError as e:
        print(f"Erro na validação dos dados do LLM: {e}")
        raise

async def main():
    """Ponto de entrada para demonstração da funcionalidade."""
    texto_exemplo = "Urgente: Relatos de frotas navais se aproximando do Estreito de Ormuz nesta manhã..."
    
    try:
        resultado = await extrair_noticia_llm_simulacao(texto_exemplo)
        print("\n--- Notícia Extraída com Sucesso ---")
        print(resultado.model_dump_json(indent=2))
    except Exception as e:
        print(f"Falha na ingestão: {e}")

if __name__ == "__main__":
    asyncio.run(main())
