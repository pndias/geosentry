#!/bin/bash
# ============================================
# GeoSentry - macOS Local Deploy (Docker)
# ============================================
set -e

RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; NC='\033[0m'

cleanup() {
    echo -e "\n${YELLOW}🧹 Stopping containers...${NC}"
    docker compose down -v 2>/dev/null || true
    echo -e "${GREEN}✨ Done.${NC}"
    exit 0
}
trap cleanup INT TERM

echo -e "${GREEN}🚀 GeoSentry — macOS Docker Deploy${NC}"

# --- 1. Ensure Docker is available and running ---
if ! command -v docker &>/dev/null; then
    echo -e "${RED}❌ Docker not found. Install Docker Desktop: https://docker.com/products/docker-desktop${NC}"
    exit 1
fi

if ! docker info &>/dev/null 2>&1; then
    echo -e "${YELLOW}🐳 Starting Docker Desktop...${NC}"
    open -a Docker
    for i in $(seq 1 30); do
        docker info &>/dev/null 2>&1 && break
        echo "   Waiting for Docker daemon... ($i/30)"
        sleep 2
    done
    if ! docker info &>/dev/null 2>&1; then
        echo -e "${RED}❌ Docker failed to start. Open Docker Desktop manually and retry.${NC}"
        exit 1
    fi
fi
echo -e "${GREEN}   Docker is running.${NC}"

# --- 2. Build and start all containers ---
echo -e "${YELLOW}🔨 Building and starting containers...${NC}"
docker compose up --build -d

# --- 3. Wait for API to be healthy ---
echo -e "${YELLOW}⏳ Waiting for services...${NC}"
for i in $(seq 1 60); do
    if curl -sf http://localhost:8000/events &>/dev/null; then
        break
    fi
    sleep 2
done

if ! curl -sf http://localhost:8000/events &>/dev/null; then
    echo -e "${RED}❌ API did not come up. Logs:${NC}"
    docker compose logs api seed db
    exit 1
fi

# --- 4. Pull LLM model into Ollama container ---
echo -e "${YELLOW}🤖 Pulling LLM model...${NC}"
docker exec geosentry_ollama ollama pull llama3.2:3b 2>/dev/null || echo "   (model pull will retry on agent start)"

# --- 5. Ready ---
EVENTS=$(curl -sf http://localhost:8000/events | python3 -c "import sys,json; print(len(json.load(sys.stdin)))" 2>/dev/null || echo "?")
echo ""
echo -e "${GREEN}✅ GeoSentry is running! ($EVENTS events loaded)${NC}"
echo "   Dashboard: http://localhost:8080"
echo "   API Docs:  http://localhost:8000/docs"
echo "   Ollama:    http://localhost:11434"
echo ""
echo "   Ctrl+C to stop  |  docker compose logs -f  to watch logs"
echo ""

open http://localhost:8080

# Keep alive — stream logs
docker compose logs -f
