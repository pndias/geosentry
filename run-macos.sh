#!/bin/bash
# ============================================
# GeoSentry - macOS Local Deploy (Ollama)
# ============================================
set -e

RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; NC='\033[0m'

cleanup() {
    echo -e "\n🧹 Shutting down..."
    kill $(jobs -p) 2>/dev/null
    sleep 1
    rm -f geosentry.db api.log frontend/frontend.log
    find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
    echo -e "${GREEN}✨ Cleanup complete.${NC}"
    exit 0
}
trap cleanup EXIT INT TERM

echo -e "${GREEN}🚀 GeoSentry — macOS Local Deploy${NC}"

# --- 1. Check / Install Homebrew dependencies ---
echo -e "${YELLOW}📦 Checking dependencies...${NC}"
for cmd in python3 node npm; do
    if ! command -v $cmd &>/dev/null; then
        echo -e "${RED}❌ $cmd not found. Install via: brew install ${cmd/python3/python}${NC}"; exit 1
    fi
done

# --- 2. Ollama ---
echo -e "${YELLOW}🤖 Setting up Ollama...${NC}"
if ! command -v ollama &>/dev/null; then
    echo "Installing Ollama..."
    brew install ollama
fi

if ! pgrep -x "ollama" &>/dev/null; then
    echo "Starting Ollama server..."
    ollama serve &>/dev/null &
    sleep 3
fi

echo "Pulling llama3.2:3b model (skip if cached)..."
ollama pull llama3.2:3b 2>/dev/null || true

# --- 3. Python Backend ---
echo -e "${YELLOW}📦 Setting up Python backend...${NC}"
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
source venv/bin/activate
pip install -r requirements.txt --quiet
pip install -r requirements-agents.txt --quiet

echo -e "${YELLOW}🔌 Starting API on port 8000...${NC}"
export PYTHONPATH=$PYTHONPATH:.
export OLLAMA_BASE_URL=http://localhost:11434
export OLLAMA_MODEL=ollama/llama3.2:3b
uvicorn src.api.main:app --host 127.0.0.1 --port 8000 > api.log 2>&1 &

echo "⏳ Waiting for API..."
for i in $(seq 1 15); do
    curl -sf http://127.0.0.1:8000/events > /dev/null 2>&1 && break
    sleep 1
done

# --- 4. Seed DB ---
echo -e "${YELLOW}🌱 Seeding database...${NC}"
python3 seed_db.py

# --- 5. Frontend ---
echo -e "${YELLOW}💻 Starting Frontend...${NC}"
cd frontend
npm install --silent > /dev/null 2>&1
npm run dev > frontend.log 2>&1 &
cd ..
sleep 3

echo -e "${GREEN}✅ GeoSentry is running!${NC}"
echo "   API:      http://localhost:8000/docs"
echo "   Frontend: http://localhost:3000"
echo "   Ollama:   http://localhost:11434"
echo "   (Ctrl+C to stop)"

open http://localhost:3000
wait
