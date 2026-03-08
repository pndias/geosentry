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
    -   `PostgreSQL` com extensão `PostGIS` (essencial para consultas espaciais e geolocalização).
    -   `Redis` para cache de notícias e filas de agentes.

4.  **Sentinel-UI (Frontend):**
    -   Dashboard SPA (Single Page Application).
    -   `Leaflet.js` para visualização cartográfica interativa.

5.  **Simbolus-Module (Módulo Analítico Futuro):**
    -   Serviço isolado de PLN para análise de semiótica comparada entre eventos atuais e textos escatológicos históricos.

---

## 🛠️ 2. Stack de Tecnologias Ideal (Fase 1)

| Camada | Tecnologia | Justificativa |
| :--- | :--- | :--- |
| **Linguagem** | Python 3.11+ | Ecossistema líder em IA e manipulação de dados. |
| **Framework Web** | FastAPI | Nativo assíncrono, gera documentação OpenAPI automaticamente. |
| **IA/Agentes** | CrewAI | Melhor framework para colaboração entre múltiplos agentes de IA. |
| **Banco de Dados** | PostGIS | Única opção robusta para filtrar eventos por "raio de distância" no mapa. |
| **Infraestrutura** | Docker & Compose | Garante paridade entre ambientes de desenvolvimento e produção. |
| **Frontend** | Vanilla JS / Leaflet | Leveza e foco total na interação com o mapa geopolítico. |

---

## 📈 3. Roadmap de Desenvolvimento

### Fase 1: Fundação e Ingestão Militar/Econômica (Atual)
- [x] Definição de Schemas Pydantic (V1.0.0).
- [x] Estrutura Modular de Pastas.
- [ ] Implementação de Scrapers reais (Agente de Busca).
- [ ] Configuração do Banco PostGIS e persistência de eventos.
- [ ] Integração do CrewAI com APIs de busca (Serper.dev/Google).

### Fase 2: Inteligência e Visualização (Próximo Passo)
- [ ] Implementação de filtros por Categoria (Militar, Política, Econômica) no Frontend.
- [ ] Sistema de "Alertas de Impacto" (Notificações para Impacto > 4).
- [ ] Painel de Fontes (Transparência das notícias citadas).

### Fase 3: Módulo Simbolus (O Guia)
- [ ] Desenvolvimento da biblioteca de correlação semântica.
- [ ] Ingestão de textos históricos (Apocalipse e outros textos proféticos).
- [ ] Interface de análise comparativa: "O Presente espelhando o Passado".

### Fase 4: Resiliência e Impacto Social
- [ ] Modo Offline/Baixa largura de banda para zonas de conflito.
- [ ] Exportação de relatórios de preparação para civis.
- [ ] Deploy em infraestrutura de alta disponibilidade.

---

## 📜 4. Filosofia do Projeto
GeoSentry não é apenas um agregador de notícias; é um instrumento de **vigilância ética**. O sucesso do projeto será medido pela sua capacidade de fornecer informações que ajudem na tomada de decisões que preservem a paz e a justiça global.
