from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from src.core.models import EventoGeopolitico, CategoriaEvento, Coordenadas

app = FastAPI(title="GeoSentry API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/eventos", response_model=List[EventoGeopolitico])
async def listar_eventos():
    # Simulação de dados (posteriormente vindo do PostGIS)
    return [
        EventoGeopolitico(
            id=1, titulo="Manobras Navais", categoria=CategoriaEvento.MILITAR, 
            resumo_analitico="Exercícios em águas internacionais.", 
            coordenadas=Coordenadas(lat=-22.9068, lon=-43.1729), impacto=3
        ),
        EventoGeopolitico(
            id=2, titulo="Cúpula de Líderes", categoria=CategoriaEvento.POLITICA, 
            resumo_analitico="Discussão sobre tratados climáticos.",
            coordenadas=Coordenadas(lat=48.8566, lon=2.3522), impacto=4
        )
    ]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
