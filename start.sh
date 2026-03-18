#!/bin/bash

# ============================================
# GeoSentry - Versão Português (pt-br)
# ============================================

cleanup() {
    echo -e "\n🧹 Encerrando projeto e limpando metadados da sessão local..."
    kill $(jobs -p) 2>/dev/null
    sleep 1
    rm -f geosentry.db api.log frontend/frontend.log frontend/frontend_deploy.log
    find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
    find . -type f -name "*.pyc" -delete 2>/dev/null
    echo "✨ Limpeza completa. Você pode reabrir o projeto a qualquer momento."
    exit 0
}

trap cleanup EXIT INT TERM

echo "🚀 Iniciando ambiente local do GeoSentry (pt-br)..."

# 1. Backend
echo "📦 Configurando backend Python..."
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt > /dev/null 2>&1

echo "🔌 Iniciando servidor FastAPI na porta 8000..."
export PYTHONPATH=$PYTHONPATH:.
./venv/bin/uvicorn src.api.main:app --host 0.0.0.0 --port 8000 > api.log 2>&1 &
BACKEND_PID=$!
sleep 5

# 2. Seed
echo "🌱 Populando banco de dados..."
./venv/bin/python seed_db.py

# 3. Frontend
echo "💻 Iniciando servidor de desenvolvimento do Frontend..."
cd frontend
npm install > /dev/null 2>&1
npm run dev > frontend.log 2>&1 &
FRONTEND_PID=$!
cd ..
sleep 3

echo "✅ GeoSentry está rodando!"
echo "   - API: http://localhost:8000/docs"
echo "   - Frontend: http://localhost:3000"
echo "   (Pressione Ctrl+C para parar)"

open http://localhost:3000
wait $BACKEND_PID $FRONTEND_PID
