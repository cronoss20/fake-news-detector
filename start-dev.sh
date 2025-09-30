#!/bin/bash
# Start backend and frontend concurrently for dev

echo "Starting backend..."
cd backend && python app.py &
BACKEND_PID=$!
cd ..

echo "Starting frontend..."
cd frontend && npm start &
FRONTEND_PID=$!
cd ..

trap "kill $BACKEND_PID $FRONTEND_PID" EXIT

wait
