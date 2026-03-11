# 🗺️ GeoSentry: Estratégia de Desenvolvimento e Roadmap

Este documento define a arquitetura técnica e o cronograma de implementação da plataforma GeoSentry, focada em monitoramento geopolítico autônomo e análise de impacto global.

## 🏗️ 1. Arquitetura Técnica (High-Level Design)

O sistema é baseado em uma **Arquitetura de Microserviços Orientada a Eventos (EDA)**, totalmente conteinerizada:

1.  **Sentry-Agents (Engineers de IA):**
    -   Orquestrados via `CrewAI` e `LangChain`.
    -   **Agente de Busca (OSINT):** Varredura de RSS, APIs de notícias e documentos oficiais.
    -   **Agente de Extração (Analista):** Processamento via LLM (GPT-4o/Claude 3.5) para transformar texto bruto no schema `EventoGeopolitico`.

2.  **Geo-Core (Backend API):**
    -   `FastAPI` (Python) para alta performance assíncrona.
    -   Validação de dados via `Pydantic V2`.

3.  **Sentry-Storage (Camada de Dados):**
    -   `PostgreSQL` com extensão `PostGIS` (Produção) / `SQLite` via SQLAlchemy (Local Dev).

4.  **Sentinel-UI (Frontend):**
    -   Dashboard SPA (Single Page Application) em `React` + `TypeScript`.
    -   `Leaflet.js` para visualização cartográfica interativa.

5.  **Simbolus-Module (Módulo Analítico Futuro):**
    -   Serviço isolado de PLN para análise de semiótica comparada entre eventos atuais e textos escatológicos históricos.

---

## 🛠️ 2. Stack de Tecnologias Ideal

| Camada | Tecnologia | Justificativa |
| :--- | :--- | :--- |
| **Linguagem** | Python 3.11+ | Ecossistema líder em IA e manipulação de dados. |
| **Framework Web** | FastAPI | Nativo assíncrono, alta performance. |
| **Banco de Dados** | SQLite / PostGIS | Flexibilidade local e escalabilidade geoespacial. |
| **Frontend** | React + Vite | Interface de Command Center responsiva e componentizada. |

---

## 📈 3. Roadmap de Desenvolvimento

### Fase 1: Fundação Técnica (Concluída)
- [x] Definição de Schemas Pydantic e Models SQLAlchemy.
- [x] Estrutura Modular de Pastas (Clean Architecture).
- [x] Criação da API FastAPI.
- [x] Seed Inicial de Banco de Dados Local (100 eventos realistas mockados).
- [x] Definição Ética (Manifesto e Copyright em nome de Pablo Dias).

### Fase 2: Inteligência e Visualização (Concluída)
- [x] Implementação de filtros por Categoria (Militar, Política, Econômica) no Frontend.
- [x] Sistema de "Alertas de Impacto" (Notificações visuais e feed para Impacto > 4).
- [x] Painel de Fontes (Módulo para transparência das notícias citadas).

### Fase 3: Orquestração de Agentes (Implementação Real-time)
- [ ] Implementação de Scrapers reais (Agente de Busca).
- [ ] Integração do CrewAI com APIs de busca (Serper.dev/Google).
- [ ] Ingestão contínua no Banco de Dados.

### Fase 4: Módulo Simbolus e Impacto Social (O Guia)
- [ ] Ingestão de textos históricos (Apocalipse e outros textos proféticos).
- [ ] Interface de análise comparativa: "O Presente espelhando o Passado".
- [ ] Modo Offline/Baixa largura de banda para zonas de conflito.

---

## 📜 4. Filosofia do Projeto
GeoSentry não é apenas um agregador de notícias; é um instrumento de **vigilância ética**. O sucesso do projeto será medido pela sua capacidade de fornecer informações que ajudem na tomada de decisões que preservem a paz e a justiça global.
