# © 2026 Pablo Dias. All rights reserved.

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from src.api.routers import eventos

ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:5173",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5173",
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]

def create_app() -> FastAPI:
    """FastAPI application factory for testability and modularity."""
    app = FastAPI(
        title="GeoSentry API",
        version="1.2.0",
        description="API for orchestration and querying of geopolitical events focused on the Global South."
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_ORIGINS,
        allow_credentials=False,
        allow_methods=["GET"],
        allow_headers=["Content-Type"],
    )

    app.include_router(eventos.router)

    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.api.main:app", host="127.0.0.1", port=8000, reload=True)
