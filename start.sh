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
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt > /dev/null 2>&1

echo "🔌 Starting FastAPI server on port 8000..."
export PYTHONPATH=$PYTHONPATH:.
./venv/bin/uvicorn src.api.main:app --host 0.0.0.0 --port 8000 > api.log 2>&1 &
BACKEND_PID=$!
sleep 5

# 2. Seed
echo "🌱 Seeding the database..."
./venv/bin/python seed_db.py

# 3. Frontend
echo "💻 Starting Frontend development server..."
cd frontend
npm install > /dev/null 2>&1
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
