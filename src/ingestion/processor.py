import asyncio
from typing import Optional
from src.core.models import EventoGeopolitico, CategoriaEvento, Coordenadas
from pydantic import ValidationError

async def extrair_dados_texto(texto: str) -> EventoGeopolitico:
    """
    Simula a extração estruturada de dados usando LLM.
    Futuramente integrará com LangChain ou chamadas diretas a LLMs.
    """
    await asyncio.sleep(1)
    
    # Mock data
    mock_data = {
        "titulo": "Escalada de Tensões no Estreito de Ormuz",
        "categoria": CategoriaEvento.MILITAR,
        "resumo_analitico": "Movimentação naval atípica e exercícios de prontidão.",
        "coordenadas": {"lat": 26.56, "lon": 56.25},
        "impacto": 4,
        "tags": ["marítimo", "Irã"],
        "fontes_citadas": ["Reuters"]
    }
    
    try:
        return EventoGeopolitico(**mock_data)
    except ValidationError as e:
        print(f"Erro na validação do schema: {e}")
        raise

if __name__ == "__main__":
    async def main():
        resultado = await extrair_dados_texto("Exemplo de notícia geopolítica...")
        print(resultado.model_dump_json(indent=2))

    asyncio.run(main())
