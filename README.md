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

## 🚀 Como Executar (Em breve)
As instruções para subir os contêineres via `docker-compose up` serão adicionadas assim que os módulos base estiverem concluídos.

## 📂 Estrutura de Diretórios
```text
├── /api            # Backend FastAPI
├── /dashboard      # Frontend (HTML, JS, Leaflet)
├── /ingestion      # Scripts de extração e modelos Pydantic
├── /agents         # Configuração dos agentes CrewAI
└── docker-compose.yml
```
