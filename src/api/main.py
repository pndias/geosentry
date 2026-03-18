# © 2026 Pablo Dias. All rights reserved.

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routers import eventos

def create_app() -> FastAPI:
    """FastAPI application factory for testability and modularity."""
    app = FastAPI(
        title="GeoSentry API",
        version="1.1.0",
        description="API for orchestration and querying of geopolitical events focused on the Global South."
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(eventos.router)

    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.api.main:app", host="0.0.0.0", port=8000, reload=True)
