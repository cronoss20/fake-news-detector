# Multi-stage Dockerfile for backend and frontend

# --- Backend build ---
FROM python:3.10-slim as backend

WORKDIR /app/backend
COPY backend/ ./
RUN pip install --no-cache-dir -r requirements.txt

# --- Frontend build ---
FROM node:18 as frontend

WORKDIR /app/frontend
COPY frontend/ ./
RUN npm install && npm run build

# --- Final stage ---
FROM python:3.10-slim

WORKDIR /app
COPY --from=backend /app/backend ./backend
COPY --from=frontend /app/frontend/build ./frontend/build

# Flask API
EXPOSE 5000

ENV FLASK_APP=backend/app.py

CMD ["sh", "-c", "cd backend && python app.py"]
