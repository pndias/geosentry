from typing import List
from src.core.models import EventoGeopolitico, CategoriaEvento, Coordenadas

class EventoService:
    @staticmethod
    def get_mock_eventos() -> List[EventoGeopolitico]:
        """
        Retorna a lista de eventos simulados.
        Em produção, isso conectará ao repositório do PostGIS.
        """
        return [
            EventoGeopolitico(
                id=1, titulo="Bloqueio Naval no Mar Vermelho", 
                categoria=CategoriaEvento.MILITAR, 
                resumo_analitico="Escalada de tensões marítimas impactando rotas de suprimento vitais para o Sul Global.", 
                coordenadas=Coordenadas(lat=12.78, lon=43.32), impacto=5,
                tags=["marítimo", "conflito", "logística"],
                fontes_citadas=["Relatórios OSINT local", "Agências Regionais"]
            ),
            EventoGeopolitico(
                id=2, titulo="Cúpula de Soberania Amazônica", 
                categoria=CategoriaEvento.POLITICA, 
                resumo_analitico="Líderes indígenas e governamentais discutem proteção contra exploração predatória estrangeira.",
                coordenadas=Coordenadas(lat=-3.11, lon=-60.02), impacto=4,
                tags=["soberania", "indígena", "recursos"],
                fontes_citadas=["Conselho Indígena", "Mídia Independente"]
            ),
            EventoGeopolitico(
                id=3, titulo="Acordo Comercial Trans-Africano", 
                categoria=CategoriaEvento.ECONOMICA, 
                resumo_analitico="Nova zona de livre comércio visa reduzir dependência do dólar e fortalecer moedas locais.",
                coordenadas=Coordenadas(lat=-1.29, lon=36.82), impacto=4,
                tags=["economia", "desdolarização", "África"],
                fontes_citadas=["Banco Central Regional", "Análise Econômica Sul-Sul"]
            ),
            EventoGeopolitico(
                id=4, titulo="Movimentação de Tropas na Fronteira Leste", 
                categoria=CategoriaEvento.MILITAR, 
                resumo_analitico="Exercícios militares não anunciados geram alerta em comunidades civis fronteiriças.",
                coordenadas=Coordenadas(lat=49.81, lon=24.02), impacto=5,
                tags=["militar", "alerta", "fronteira"],
                fontes_citadas=["Monitoramento de Satélite", "Ativistas Locais"]
            ),
            EventoGeopolitico(
                id=5, titulo="Manifestação Simbólica por Justiça Social", 
                categoria=CategoriaEvento.RELIGIOSA_SIMBOLICA, 
                resumo_analitico="Milhares se reúnem em ato simbólico contra desigualdade histórica e exploração.",
                coordenadas=Coordenadas(lat=-23.55, lon=-46.63), impacto=3,
                tags=["social", "simbolismo", "povo"],
                fontes_citadas=["Movimentos Sociais", "Imprensa Popular"]
            ),
            EventoGeopolitico(
                id=6, titulo="Inauguração de Porto de Águas Profundas", 
                categoria=CategoriaEvento.ECONOMICA, 
                resumo_analitico="Parceria estratégica visa criar novo hub logístico independente de potências tradicionais.",
                coordenadas=Coordenadas(lat=24.86, lon=66.99), impacto=4,
                tags=["infraestrutura", "logística", "Ásia"],
                fontes_citadas=["Ministério da Infraestrutura", "Dados Portuários"]
            )
        ]
