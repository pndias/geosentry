# © 2026 Pablo Dias. All rights reserved.

import os
from crewai import Agent, Task, Crew, Process, LLM
from src.domain.entities import GeopoliticalEvent

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "ollama/llama3.2:3b")

llm = LLM(model=OLLAMA_MODEL, base_url=OLLAMA_BASE_URL)

# --- Ethical and Plural Agent Configuration ---

researcher = Agent(
    role='Global South Sentinel (OSINT)',
    goal='Identify events that directly impact the security and sovereignty of populations in the Global South.',
    backstory=(
        "You are an intelligence analyst with a humanitarian and grassroots focus. "
        "Your mission is to filter through Western mainstream media noise and focus on how conflicts "
        "and treaties affect workers' lives, water security, food security, and civilian integrity. "
        "You are honest, technical, pluralistic, and deeply committed to peace through information."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False
)

analyst = Agent(
    role='Social Impact Translator',
    goal='Transform raw facts into insights that help people prepare for systemic changes.',
    backstory=(
        "You are a data engineer who believes information should save lives. "
        "Your job is to classify geopolitical events under an ethical metric: "
        "the impact level (1-5) must reflect the risk to human life and social stability. "
        "You seek the correlations that elites ignore but the working class needs to know."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False
)

def create_geopolitical_crew():
    research_task = Task(
        description=(
            "Investigate the 5 most critical events from the last 48 hours on the global stage. "
            "Your priority is to identify military movements, new exploitative economic agreements, "
            "or political changes that threaten the Global South. "
            "Look for escalation signals that may require adaptation or civilian alerts."
        ),
        expected_output=(
            "A report focused on human impact, sovereignty, and systemic risks, "
            "containing the 5 most urgent events identified."
        ),
        agent=researcher
    )

    analysis_task = Task(
        description=(
            "Translate the research report into JSON format (GeopoliticalEvent schema). "
            "Set the impact (1-5) based on the potential for human suffering or gains in popular sovereignty. "
            "Maintain direct language, free of unnecessary financial jargon, focused on clarity for the common citizen."
        ),
        expected_output="Validated JSON string, ready for visualization on the GeoSentry Dashboard.",
        agent=analyst
    )

    return Crew(
        agents=[researcher, analyst],
        tasks=[research_task, analysis_task],
        process=Process.sequential,
        verbose=True
    )

if __name__ == "__main__":
    import time

    CYCLE_HOURS = int(os.getenv("COLLECTION_INTERVAL_HOURS", "6"))

    while True:
        crew = create_geopolitical_crew()
        result = crew.kickoff()
        print("\n--- GEOSENTRY INTELLIGENCE (Voice of the Global South) ---")
        print(result)
        print(f"\n⏳ Next collection in {CYCLE_HOURS}h...")
        time.sleep(CYCLE_HOURS * 3600)
