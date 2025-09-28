#!/bin/bash

# Start Fake News Detector in Development Mode
# This script starts both backend and frontend servers

echo "🚀 Starting Fake News Detector..."
echo "=================================="

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

# Check if Node.js is available
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is required but not installed."
    exit 1
fi

# Function to kill background processes on script exit
cleanup() {
    echo "🛑 Shutting down servers..."
    kill $BACKEND_PID $FRONTEND_PID 2>/dev/null
    exit 0
}

trap cleanup SIGINT SIGTERM

# Start backend
echo "🔧 Starting backend server..."
cd backend

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install requirements
echo "📋 Installing backend dependencies..."
pip install -r requirements.txt > /dev/null 2>&1

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "⚠️  Warning: .env file not found. Copying from .env.example"
    cp .env.example .env
    echo "❗ Please edit backend/.env and add your OpenAI API key"
fi

# Start backend server
echo "🖥️  Backend starting on http://localhost:5000"
python app.py &
BACKEND_PID=$!

# Wait a bit for backend to start
sleep 3

# Start frontend
echo "🎨 Starting frontend server..."
cd ../frontend

# Install dependencies
echo "📋 Installing frontend dependencies..."
npm install > /dev/null 2>&1

# Start frontend server
echo "🌐 Frontend starting on http://localhost:3000"
BROWSER=none npm start &
FRONTEND_PID=$!

echo ""
echo "✅ Both servers are starting up!"
echo "=================================="
echo "🖥️  Backend API: http://localhost:5000"
echo "🌐 Frontend UI:  http://localhost:3000"
echo "=================================="
echo "📝 Don't forget to set your OpenAI API key in backend/.env"
echo "🛑 Press Ctrl+C to stop both servers"
echo ""

# Wait for background processes
wait