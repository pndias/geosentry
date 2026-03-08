from crewai import Agent, Task, Crew, Process
from src.core.models import EventoGeopolitico

# Configuração de Agentes
pesquisador = Agent(
    role='Pesquisador Geopolítico',
    goal='Identificar e sintetizar notícias sobre tratados e conflitos globais.',
    backstory='Especialista em inteligência de fontes abertas (OSINT).',
    verbose=True,
    allow_delegation=False
)

analista = Agent(
    role='Analista de Dados',
    goal='Formatar achados geopolíticos em objetos JSON estruturados.',
    backstory='Engenheiro de dados especializado em extração de entidades.',
    verbose=True,
    allow_delegation=False
)

def criar_crew_geopolitica():
    tarefa_pesquisa = Task(
        description="Pesquise os 5 eventos geopolíticos mais impactantes das últimas 48 horas.",
        expected_output="Relatório detalhado dos 5 eventos.",
        agent=pesquisador
    )

    tarefa_analise = Task(
        description="Gere uma lista JSON baseada no relatório, seguindo o schema de EventoGeopolitico.",
        expected_output="String JSON validada.",
        agent=analista
    )

    return Crew(
        agents=[pesquisador, analista],
        tasks=[tarefa_pesquisa, tarefa_analise],
        process=Process.sequential,
        verbose=True
    )

if __name__ == "__main__":
    crew = criar_crew_geopolitica()
    resultado = crew.kickoff()
    print(resultado)
