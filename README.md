# 🌍 GeoSentry: Autonomous Geopolitical Monitoring Platform

![Status](https://img.shields.io/badge/Status-In%20Development-orange)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Docker](https://img.shields.io/badge/Docker-Microservices-2496ED)

## 📌 About the Project
A data intelligence system that uses Autonomous AI Agents to monitor, classify, and cross-reference geopolitical, military, and economic events worldwide in real time. The system extracts data from unstructured sources, structures it into JSON via LLMs, and plots events on an interactive dashboard with geolocation filters.

In the future, the project will include an experimental Natural Language Processing (NLP) module for comparative analysis between contemporary events and symbolic/historical texts.

## 🏗️ Modular Architecture
The project is designed using microservices principles and will be fully containerized via Docker:

* **Ingestion Engine:** Python scripts using `Pydantic` for strict validation of LLM-extracted data.
* **Database:** PostgreSQL with `PostGIS` extension for spatial and geolocation queries.
* **Automation Agents:** `CrewAI` implementation for asynchronous news and treaty search and analysis.
* **API & Backend:** `FastAPI` to serve consolidated data.
* **Frontend:** Interactive dashboard rendering maps using `Leaflet.js`.

## 🚀 How to Run Locally via CLI

To run the project on your machine, use the automated script that sets up the environment, starts the API and Dashboard, and cleans up all state and metadata on exit (avoiding issues from past runs).

Open a terminal and navigate to the project folder:
```bash
cd /path/to/geosentry
```

Grant execution permission to the script and start the environment:
```bash
chmod +x start.sh
./start.sh
```

This will set up the `geosentry.db` database, start the API (Backend), and open the Frontend.
The Dashboard will open automatically (or visit `http://localhost:5173`).

**When you stop the script** by pressing `Ctrl+C`, all temporary files, database files, and logs created during the local session will be deleted, ensuring the project starts fresh on the next run.

## 📂 Directory Structure
```text
├── /api            # FastAPI Backend
├── /dashboard      # Frontend (HTML, JS, Leaflet)
├── /ingestion      # Extraction scripts and Pydantic models
├── /agents         # CrewAI agent configuration
└── docker-compose.yml
```

---

## ⚖️ Copyright & Authorship
**GeoSentry** is a project conceived, designed, and developed by **Pablo Dias**.

© 2026 Pablo Dias. All rights reserved.
This software is distributed under the MIT License. See the `LICENSE` file for details.
