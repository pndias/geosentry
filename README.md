# 🌍 GeoSentry: Plataforma de Monitoramento Geopolítico Autônomo

![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Docker](https://img.shields.io/badge/Docker-Microservices-2496ED)

## 📌 Sobre o Projeto
Um sistema de inteligência de dados que utiliza Agentes Autônomos (IA) para monitorar, classificar e cruzar eventos geopolíticos, militares e econômicos globais em tempo real. O sistema extrai dados de fontes desestruturadas, estrutura em JSON via LLMs, e plota os eventos em um dashboard interativo com filtros de geolocalização.

Futuramente, o projeto contará com um módulo experimental de Processamento de Linguagem Natural (PLN) para análise comparativa entre eventos contemporâneos e textos simbólicos/históricos.

## 🏗️ Arquitetura Modular
O projeto foi desenhado utilizando princípios de microserviços e será totalmente conteinerizado via Docker:

* **Motor de Ingestão:** Scripts em Python utilizando `Pydantic` para validação estrita de extração de dados via LLM.
* **Banco de Dados:** PostgreSQL com extensão `PostGIS` para consultas espaciais e de geolocalização.
* **Agentes de Automação:** Implementação de `CrewAI` para busca e análise assíncrona de notícias e tratados.
* **API & Backend:** `FastAPI` para servir os dados consolidados.
* **Frontend:** Dashboard interativo renderizando mapas utilizando `Leaflet.js`.

## 🚀 Como Executar Localmente via CLI

Para rodar o projeto na sua máquina sem o uso de agentes automatizados ou Docker, siga o passo a passo abaixo:

### 1. Preparar o Backend (FastAPI & SQLite)
Abra um terminal e navegue até a pasta do projeto:
```bash
cd /caminho/para/geosentry
```

Ative o ambiente virtual e instale as dependências:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Inicie o servidor Backend:
```bash
PYTHONPATH=. uvicorn src.api.main:app --reload --port 8000
```
A API estará rodando em `http://localhost:8000/eventos`.

*(Opcional)* Se o banco de dados `geosentry.db` ainda não estiver populado, abra outro terminal com o `venv` ativo e rode:
```bash
PYTHONPATH=. python3 seed_db.py
```

### 2. Iniciar o Frontend (React + Vite)
Abra uma **nova aba de terminal** e navegue para a pasta do frontend:
```bash
cd /caminho/para/geosentry/frontend
```

Instale as dependências Node (apenas na primeira vez):
```bash
npm install
```

Inicie o servidor de desenvolvimento:
```bash
npm run dev
```
O Dashboard abrirá automaticamente (ou acesse `http://localhost:5173` ou a porta indicada no terminal).

## 📂 Estrutura de Diretórios
```text
├── /api            # Backend FastAPI
├── /dashboard      # Frontend (HTML, JS, Leaflet)
├── /ingestion      # Scripts de extração e modelos Pydantic
├── /agents         # Configuração dos agentes CrewAI
└── docker-compose.yml
```

---

## ⚖️ Copyright & Autoria
**GeoSentry** é um projeto idealizado, projetado e desenvolvido por **Pablo Dias**.

© 2026 Pablo Dias. Todos os direitos reservados.
Este software é distribuído sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
