import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
from src.core.models import EventoGeopolitico

# Carrega chaves de API do arquivo .env
load_dotenv()

# Ferramenta de Busca Real-Time (Serper.dev)
search_tool = SerperDevTool()

# Configuração de Agentes
pesquisador = Agent(
    role='Pesquisador Geopolítico',
    goal='Identificar notícias reais e recentes (últimas 48h) sobre conflitos e tratados globais.',
    backstory='Especialista em inteligência de fontes abertas (OSINT) e análise de notícias.',
    tools=[search_tool],
    verbose=True,
    allow_delegation=False
)

analista = Agent(
    role='Analista de Dados',
    goal='Formatar os achados do pesquisador em objetos JSON estruturados e validados.',
    backstory='Engenheiro de dados especializado em transformar texto livre em esquemas rigorosos.',
    verbose=True,
    allow_delegation=False
)

def criar_crew_geopolitica():
    tarefa_pesquisa = Task(
        description=(
            "Use a ferramenta de busca para encontrar os 5 eventos geopolíticos mais relevantes "
            "das últimas 48 horas. Foque em: 1. Movimentações militares, 2. Novos tratados e 3. Crises econômicas."
            "\nPara cada evento, identifique: Título, Categoria, Resumo, Localização (País/Coordenadas se possível) e Fonte."
        ),
        expected_output="Um relatório consolidado e detalhado sobre os 5 eventos reais identificados.",
        agent=pesquisador
    )

    tarefa_analise = Task(
        description=(
            "Com base no relatório do pesquisador, gere uma lista de objetos JSON seguindo o "
            "formato do schema EventoGeopolitico. Garanta que as coordenadas sejam floats "
            "e as chaves de categoria sigam o Enum (Militar, Politica, Economica)."
        ),
        expected_output="Uma string JSON pura contendo a lista de eventos validados.",
        agent=analista
    )

    return Crew(
        agents=[pesquisador, analista],
        tasks=[tarefa_pesquisa, tarefa_analise],
        process=Process.sequential,
        verbose=True
    )

if __name__ == "__main__":
    # Nota: requer OPENAI_API_KEY e SERPER_API_KEY no ambiente
    if not os.getenv("SERPER_API_KEY"):
        print("ERRO: SERPER_API_KEY não encontrada. Configure seu arquivo .env.")
    else:
        crew = criar_crew_geopolitica()
        resultado = crew.kickoff()
        print("\n--- RESULTADO DA EXTRAÇÃO REAL ---")
        print(resultado)
