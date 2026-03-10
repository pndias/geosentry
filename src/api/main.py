from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routers import eventos

def create_app() -> FastAPI:
    """Factory de criação da aplicação FastAPI para facilitar testes e modularidade."""
    app = FastAPI(
        title="GeoSentry API",
        version="1.1.0",
        description="API para orquestração e consulta de eventos geopolíticos focados no Sul Global."
    )

    # Configuração de CORS (Em produção, restrija as origens)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Inclusão de Rotas
    app.include_router(eventos.router)

    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    # Execução local para ambiente de desenvolvimento
    uvicorn.run("src.api.main:app", host="0.0.0.0", port=8000, reload=True)
