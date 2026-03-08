from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Evento(BaseModel):
    id: int
    titulo: str
    categoria: str
    lat: float
    lng: float

@app.get("/eventos", response_model=List[Evento])
async def listar_eventos():
    return [
        {"id": 1, "titulo": "Manobras Navais", "categoria": "Militar", "lat": -22.9068, "lng": -43.1729},
        {"id": 2, "titulo": "Cúpula de Líderes", "categoria": "Politica", "lat": 48.8566, "lng": 2.3522},
        {"id": 3, "titulo": "Acordo Comercial", "categoria": "Economica", "lat": 35.6895, "lng": 139.6917},
        {"id": 4, "titulo": "Movimentação de Tropas", "categoria": "Militar", "lat": 50.4501, "lng": 30.5234},
        {"id": 5, "titulo": "Votação na ONU", "categoria": "Politica", "lat": 40.7128, "lng": -74.0060}
    ]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
