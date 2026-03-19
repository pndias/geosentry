FROM fedora:latest

RUN dnf -y install python3.13 python3.13-pip python3.13-devel gcc gcc-c++ libpq-devel cargo rust && dnf clean all

WORKDIR /app
COPY requirements.txt requirements-agents.txt ./
RUN python3.13 -m pip install --no-cache-dir -r requirements.txt -r requirements-agents.txt

COPY src/ src/

ENV PYTHONPATH=/app

CMD ["python3.13", "-m", "src.agents.geopolitical_crew"]
