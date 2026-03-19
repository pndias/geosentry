FROM fedora:latest

RUN dnf -y install python3.13 python3.13-pip python3.13-devel gcc libpq-devel && dnf clean all

WORKDIR /app
COPY requirements.txt .
RUN python3.13 -m pip install --no-cache-dir -r requirements.txt

COPY src/ src/
COPY seed_db.py .

ENV PYTHONPATH=/app
EXPOSE 8000

CMD ["python3.13", "-m", "uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
