import os
from crewai import Agent, Task, Crew, Process

pesquisador = Agent(
    role='Pesquisador Geopolítico',
    goal='Buscar e sintetizar notícias recentes sobre tratados internacionais e conflitos militares globais.',
    backstory='Especialista em relações internacionais e segurança global.',
    verbose=True,
    allow_delegation=False
)

analista = Agent(
    role='Analista de Dados',
    goal='Formatar os achados da pesquisa geopolítica em um objeto JSON estruturado.',
    backstory='Engenheiro de dados especializado em extração de entidades.',
    verbose=True,
    allow_delegation=False
)

tarefa_pesquisa = Task(
    description="Identifique os 5 eventos geopolíticos mais relevantes das últimas 48 horas.",
    expected_output="Um relatório textual detalhado sobre os 5 eventos identificados.",
    agent=pesquisador
)

tarefa_analise = Task(
    description="Transforme o relatório em um formato JSON válido.",
    expected_output="Uma string formatada em JSON contendo a lista de eventos estruturados.",
    agent=analista
)

equipe_geopolitica = Crew(
    agents=[pesquisador, analista],
    tasks=[tarefa_pesquisa, tarefa_analise],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    resultado = equipe_geopolitica.kickoff()
    print(resultado)
