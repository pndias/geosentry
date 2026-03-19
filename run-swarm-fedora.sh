#!/bin/bash
# ============================================
# GeoSentry - Docker Swarm Deploy (Fedora)
# ============================================
set -e

RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; NC='\033[0m'
STACK_NAME="geosentry"

cleanup() {
    echo -e "\n${YELLOW}🧹 Tearing down swarm stack...${NC}"
    docker stack rm $STACK_NAME 2>/dev/null || true
    sleep 5
    echo -e "${GREEN}✨ Stack removed.${NC}"
}

echo -e "${GREEN}🚀 GeoSentry — Docker Swarm Deploy (Fedora)${NC}"

# --- 1. Install Docker if missing ---
if ! command -v docker &>/dev/null; then
    echo -e "${YELLOW}📦 Installing Docker...${NC}"
    sudo dnf -y install dnf-plugins-core
    sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
    sudo dnf -y install docker-ce docker-ce-cli containerd.io docker-compose-plugin
    sudo systemctl enable --now docker
    sudo usermod -aG docker "$USER"
    echo -e "${RED}⚠️  Log out and back in for docker group, then re-run this script.${NC}"
    exit 1
fi

# --- 2. Ensure Docker is running ---
if ! sudo systemctl is-active --quiet docker; then
    sudo systemctl start docker
fi

# --- 3. Init Swarm if not active ---
if ! docker info 2>/dev/null | grep -q "Swarm: active"; then
    echo -e "${YELLOW}🐝 Initializing Docker Swarm...${NC}"
    docker swarm init --advertise-addr $(hostname -I | awk '{print $1}') 2>/dev/null || true
fi

# --- 4. Build images ---
echo -e "${YELLOW}🔨 Building container images...${NC}"
docker build -t geosentry/api:latest     -f docker/api.Dockerfile .
docker build -t geosentry/agents:latest  -f docker/agents.Dockerfile .
docker build -t geosentry/ingestion:latest -f docker/ingestion.Dockerfile .
docker build -t geosentry/seed:latest    -f docker/seed.Dockerfile .
docker build -t geosentry/frontend:latest -f docker/frontend.Dockerfile .

# --- 5. Deploy stack ---
echo -e "${YELLOW}🚢 Deploying swarm stack...${NC}"
docker stack deploy -c docker-compose-swarm.yml $STACK_NAME

# --- 6. Wait for services ---
echo "⏳ Waiting for services to stabilize..."
sleep 15

# --- 7. Pull Ollama model inside container ---
echo -e "${YELLOW}🤖 Pulling LLM model into Ollama container...${NC}"
OLLAMA_CONTAINER=$(docker ps --filter "name=${STACK_NAME}_ollama" --format "{{.ID}}" | head -1)
if [ -n "$OLLAMA_CONTAINER" ]; then
    docker exec "$OLLAMA_CONTAINER" ollama pull llama3.2:3b || echo "Model pull will retry on agent start"
fi

# --- 8. Run seed ---
echo -e "${YELLOW}🌱 Seeding database (one-shot)...${NC}"
sleep 5  # give postgres time

echo -e "${GREEN}✅ GeoSentry Swarm is running!${NC}"
echo ""
echo "   Dashboard: http://$(hostname -I | awk '{print $1}'):8080"
echo "   API:       http://$(hostname -I | awk '{print $1}'):8000/docs"
echo ""
echo "   Stack services:"
docker stack services $STACK_NAME
echo ""
echo "   To tear down: docker stack rm $STACK_NAME"
echo "   To leave swarm: docker swarm leave --force"
