#!/bin/bash

# Define a cleanup function
cleanup() {
    echo -e "\n🧹 Closing project and cleaning up metadata from local session..."
    
    # Kill all child background processes (like uvicorn)
    kill $(jobs -p) 2>/dev/null
    
    # Wait a bit to ensure processes release files
    sleep 1

    # Remove the temporary local database to ensure a fresh start next time
    rm -f geosentry.db
    
    # Remove log files
    rm -f api.log
    rm -f frontend/frontend.log
    rm -f frontend/frontend_deploy.log

    # Remove Python cache directories and files
    find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
    find . -type f -name "*.pyc" -delete 2>/dev/null
    
    echo "✨ Cleanup complete. You can reopen the project anytime without problems."
    exit 0
}

# Trap terminal interrupt signals (Ctrl+C, etc) to ensure cleanup runs
trap cleanup EXIT INT TERM

echo "🚀 Starting GeoSentry local environment..."

# 1. Setup Backend Environment
echo "📦 Setting up Python backend..."
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt > /dev/null 2>&1

# 2. Start Backend API in background
echo "🔌 Starting FastAPI Server on port 8000..."
export PYTHONPATH=$PYTHONPATH:.
./venv/bin/uvicorn src.api.main:app --host 0.0.0.0 --port 8000 > api.log 2>&1 &
BACKEND_PID=$!

# Wait for backend to be ready
sleep 5

# 3. Seed Database
echo "🌱 Seeding the database with fresh data..."
./venv/bin/python seed_db.py

# 4. Start Frontend
echo "💻 Starting Frontend Development Server..."
cd frontend
npm install > /dev/null 2>&1
npm run dev > frontend.log 2>&1 &
FRONTEND_PID=$!
cd ..

echo "✅ GeoSentry is perfectly up and running!"
echo "   - API: http://localhost:8000/docs"
echo "   - Frontend: http://localhost:5173"
echo "   (Press Ctrl+C to stop all services)"

# Wait for both processes
wait $BACKEND_PID $FRONTEND_PID

# 4. Setup and Start Frontend
echo "💻 Setting up and starting Frontend..."
cd frontend
npm install > frontend_deploy.log 2>&1
npm run dev

# The script will block here while 'npm run dev' runs.
# When the user stops it (Ctrl+C), the 'cleanup' trap will fire.
