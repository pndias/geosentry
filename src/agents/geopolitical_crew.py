# © 2026 Pablo Dias. Todos os direitos reservados.

import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
from src.domain.entities import EventoGeopolitico

# Carrega chaves de API do arquivo .env
load_dotenv()

# Ferramenta de Busca Real-Time (Serper.dev)
search_tool = SerperDevTool()

# --- Configuração de Agentes Éticos e Plurais ---

pesquisador = Agent(
    role='Sentinela do Sul Global (OSINT)',
    goal='Identificar eventos que impactem diretamente a segurança e a soberania das populações no Sul Global.',
    backstory=(
        "Você é um analista de inteligência com foco humanitário e popular. "
        "Sua missão é filtrar o ruído da grande mídia ocidental e focar em como os conflitos "
        "e tratados afetam a vida do trabalhador, a segurança hídrica, alimentar e a integridade civil. "
        "Você é honesto, técnico, plural e profundamente comprometido com a paz através da informação."
    ),
    tools=[search_tool],
    verbose=True,
    allow_delegation=False
)

analista = Agent(
    role='Tradutor de Impacto Social',
    goal='Transformar fatos brutos em insights que ajudem as pessoas a se prepararem para mudanças sistêmicas.',
    backstory=(
        "Você é um engenheiro de dados que acredita que a informação deve salvar vidas. "
        "Seu trabalho é classificar eventos geopolíticos sob uma métrica ética: "
        "o nível de impacto (1-5) deve refletir o risco à vida humana e à estabilidade social. "
        "Você busca as correlações que a elite ignora, mas que a classe trabalhadora precisa saber."
    ),
    verbose=True,
    allow_delegation=False
)

def criar_crew_geopolitica():
    tarefa_pesquisa = Task(
        description=(
            "Investigue os 5 eventos mais críticos das últimas 48 horas no cenário global. "
            "Sua prioridade é identificar movimentos militares, novos acordos econômicos de exploração "
            "ou mudanças políticas que ameacem o Sul Global. "
            "Busque por sinais de escalada que possam exigir adaptação ou alerta para a população civil."
        ),
        expected_output=(
            "Um relatório focado em impacto humano, soberania e riscos sistêmicos, "
            "contendo os 5 eventos mais urgentes identificados."
        ),
        agent=pesquisador
    )

    tarefa_analise = Task(
        description=(
            "Traduza o relatório de pesquisa para o formato JSON (schema EventoGeopolitico). "
            "Defina o impacto (1-5) com base no potencial de sofrimento humano ou ganho de soberania popular. "
            "Mantenha uma linguagem direta, livre de jargões financeiros desnecessários, focada na clareza para o cidadão comum."
        ),
        expected_output="String JSON validada, pronta para visualização no Dashboard GeoSentry.",
        agent=analista
    )

    return Crew(
        agents=[pesquisador, analista],
        tasks=[tarefa_pesquisa, tarefa_analise],
        process=Process.sequential,
        verbose=True
    )

if __name__ == "__main__":
    if not os.getenv("SERPER_API_KEY"):
        print("ERRO: Configure sua SERPER_API_KEY no .env para ativar a Sentinela.")
    else:
        crew = criar_crew_geopolitica()
        resultado = crew.kickoff()
        print("\n--- INTELIGÊNCIA GEOSENTRY (Voz do Sul Global) ---")
        print(resultado)
