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

Para rodar o projeto de forma simplificada na sua máquina, utilize o script automatizado que prepara o ambiente, inicia a API e o Dashboard, e limpa todo o estado e metadata ao ser fechado (evitando problemas de execuções passadas).

Abra um terminal e navegue até a pasta do projeto:
```bash
cd /caminho/para/geosentry
```

Dê permissão de execução ao script e inicie o ambiente:
```bash
chmod +x start.sh
./start.sh
```

Isso fará o setup do banco de dados `geosentry.db`, iniciará a API (Backend) e abrirá o Frontend. 
O Dashboard abrirá automaticamente (ou acesse `http://localhost:5173`).

**Ao encerrar o script** pressionando `Ctrl+C`, todos os arquivos temporários, de banco de dados e logs criados na sessão local serão deletados, garantindo que o projeto inicie fresco na próxima execução.

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
