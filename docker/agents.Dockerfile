FROM python:3.11-slim

RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt requirements-agents.txt ./
RUN pip install --no-cache-dir -r requirements.txt -r requirements-agents.txt

COPY src/ src/

ENV PYTHONPATH=/app

CMD ["python", "-m", "src.agents.geopolitical_crew"]
