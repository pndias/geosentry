#!/bin/bash

# ============================================
# GeoSentry - English Version (en)
# ============================================

cleanup() {
    echo -e "\n🧹 Shutting down and cleaning up local session metadata..."
    kill $(jobs -p) 2>/dev/null
    sleep 1
    rm -f geosentry.db api.log frontend/frontend.log frontend/frontend_deploy.log
    find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
    find . -type f -name "*.pyc" -delete 2>/dev/null
    echo "✨ Cleanup complete. You can reopen the project anytime."
    exit 0
}

trap cleanup EXIT INT TERM

echo "🚀 Starting GeoSentry local environment (en)..."

# 1. Backend
echo "📦 Setting up Python backend..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
source venv/bin/activate
pip install -r requirements.txt --quiet || { echo "❌ pip install failed"; exit 1; }

echo "🌱 Seeding the database..."
export PYTHONPATH=$PYTHONPATH:.
./venv/bin/python3 seed_db.py

echo "🔌 Starting FastAPI server on port 8000..."
./venv/bin/uvicorn src.api.main:app --host 127.0.0.1 --port 8000 > api.log 2>&1 &
BACKEND_PID=$!

# Wait for API to be ready
echo "⏳ Waiting for API..."
for i in $(seq 1 15); do
    curl -sf http://127.0.0.1:8000/events > /dev/null 2>&1 && break
    sleep 1
done

# 2. Frontend
echo "💻 Starting Frontend development server..."
cd frontend
npm install --silent > /dev/null 2>&1
npm run dev > frontend.log 2>&1 &
FRONTEND_PID=$!
cd ..
sleep 3

echo "✅ GeoSentry is up and running!"
echo "   - API: http://localhost:8000/docs"
echo "   - Frontend: http://localhost:3000"
echo "   (Press Ctrl+C to stop all services)"

open http://localhost:3000
wait $BACKEND_PID $FRONTEND_PID
