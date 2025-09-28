@echo off
echo 🚀 Starting Fake News Detector...
echo ==================================

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is required but not installed.
    pause
    exit /b 1
)

REM Check if Node.js is available
node --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Node.js is required but not installed.
    pause
    exit /b 1
)

echo 🔧 Starting backend server...
cd backend

REM Check if virtual environment exists
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install requirements
echo 📋 Installing backend dependencies...
pip install -r requirements.txt >nul 2>&1

REM Check if .env exists
if not exist ".env" (
    echo ⚠️  Warning: .env file not found. Copying from .env.example
    copy .env.example .env >nul
    echo ❗ Please edit backend\.env and add your OpenAI API key
)

echo 🖥️  Backend starting on http://localhost:5000
start "Backend Server" cmd /k "python app.py"

REM Wait a bit for backend to start
timeout /t 3 /nobreak >nul

REM Start frontend
echo 🎨 Starting frontend server...
cd ..\frontend

REM Install dependencies
echo 📋 Installing frontend dependencies...
call npm install >nul 2>&1

echo 🌐 Frontend starting on http://localhost:3000
start "Frontend Server" cmd /k "set BROWSER=none && npm start"

echo.
echo ✅ Both servers are starting up!
echo ==================================
echo 🖥️  Backend API: http://localhost:5000
echo 🌐 Frontend UI:  http://localhost:3000
echo ==================================
echo 📝 Don't forget to set your OpenAI API key in backend\.env
echo 🛑 Close both command windows to stop the servers
echo.

pause