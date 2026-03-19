# 🗺️ GeoSentry: Development Strategy and Roadmap

This document defines the technical architecture and implementation timeline for the GeoSentry platform, focused on autonomous geopolitical monitoring and global impact analysis.

## 🏗️ 1. Technical Architecture (High-Level Design)

The system is based on an **Event-Driven Microservices Architecture (EDA)**, fully containerized:

1.  **Sentry-Agents (AI Engineers):**
    -   Orchestrated via `CrewAI` and `LangChain`.
    -   **Search Agent (OSINT):** Scanning RSS feeds, news APIs, and official documents.
    -   **Extraction Agent (Analyst):** Processing via LLM (GPT-4o/Claude 3.5) to transform raw text into the `GeopoliticalEvent` schema.

2.  **Geo-Core (Backend API):**
    -   `FastAPI` (Python) for high-performance async operations.
    -   Data validation via `Pydantic V2`.

3.  **Sentry-Storage (Data Layer):**
    -   `PostgreSQL` with `PostGIS` extension (Production) / `SQLite` via SQLAlchemy (Local Dev).

4.  **Sentinel-UI (Frontend):**
    -   SPA (Single Page Application) Dashboard in `React` + `TypeScript`.
    -   `Leaflet.js` for interactive cartographic visualization.

5.  **Simbolus-Module (Future Analytical Module):**
    -   Isolated NLP service for comparative semiotic analysis between current events and historical eschatological texts.

---

## 🛠️ 2. Ideal Technology Stack

| Layer | Technology | Rationale |
| :--- | :--- | :--- |
| **Language** | Python 3.11+ | Leading ecosystem for AI and data manipulation. |
| **Web Framework** | FastAPI | Native async, high performance. |
| **Database** | SQLite / PostGIS | Local flexibility and geospatial scalability. |
| **Frontend** | React + Vite | Responsive and componentized Command Center interface. |

| **Containerization** | Docker + Docker Swarm | Independent containers, overlay networking, replica scaling. |
| **LLM Runtime** | Ollama (llama3.2:3b) | Local open-source model, no API keys required. |
| **Reverse Proxy** | Nginx | Frontend serving and API proxying in production. |

---

## 📈 3. Development Roadmap

### Phase 1: Technical Foundation (Completed)
- [x] Pydantic Schemas and SQLAlchemy Models definition.
- [x] Modular Folder Structure (Clean Architecture).
- [x] FastAPI API creation.
- [x] Initial Local Database Seed (100 realistic mocked events).
- [x] Ethical Definition (Manifesto and Copyright under Pablo Dias).

### Phase 2: Intelligence and Visualization (Completed)
- [x] Category filters implementation (Military, Political, Economic) on the Frontend.
- [x] "Impact Alerts" system (Visual notifications and feed for Impact > 4).
- [x] Sources Panel (Module for news citation transparency).

### Phase 3: Containerization & Orchestration (Completed)
- [x] Each service (API, Agents, Ingestion, Frontend, DB, Ollama) as independent Docker container.
- [x] Docker Swarm stack with overlay network, replica scaling, and rolling updates.
- [x] Nginx reverse proxy for frontend → API routing.
- [x] Environment-aware config: `DATABASE_URL`, `OLLAMA_BASE_URL`, `OLLAMA_MODEL`.
- [x] `run-macos.sh`: Local macOS deploy with Ollama + llama3.2:3b.
- [x] `run-swarm-fedora.sh`: Full Docker Swarm deploy on Fedora.
- [x] Multi-stage frontend Dockerfile (Node build → nginx alpine).
- [x] PostgreSQL (Docker) / SQLite (local) dual database support.

### Phase 4: Agent Orchestration (Real-time Implementation)
- [ ] Real scraper implementation (Search Agent).
- [ ] CrewAI integration with search APIs (Serper.dev/Google).
- [ ] Continuous database ingestion.

### Phase 5: Simbolus Module and Social Impact (The Guide)
- [ ] Historical text ingestion (Revelation and other prophetic texts).
- [ ] Comparative analysis interface: "The Present mirroring the Past".
- [ ] Offline/Low-bandwidth mode for conflict zones.

---

## 📜 4. Project Philosophy
GeoSentry is not just a news aggregator; it is an instrument of **ethical vigilance**. The project's success will be measured by its ability to provide information that helps in decision-making that preserves global peace and justice.
