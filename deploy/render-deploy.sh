#!/bin/bash

# Render.com Deployment Script for Fake News Detector
# This script helps deploy the application to Render.com

set -e

echo "🚀 Fake News Detector - Render Deployment Script"
echo "=================================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if Render CLI is installed
echo "📋 Checking prerequisites..."
if ! command -v render &> /dev/null; then
    echo -e "${YELLOW}Warning: Render CLI not found. You'll need to deploy via the Render web interface.${NC}"
    echo ""
    echo "To install Render CLI:"
    echo "  npm install -g @render/cli"
    echo ""
fi

# Check if git repo is clean
if [[ -n $(git status -s) ]]; then
    echo -e "${YELLOW}Warning: You have uncommitted changes. Please commit them before deploying.${NC}"
    echo ""
fi

echo ""
echo "📦 Deployment Options:"
echo "1. Deploy via Render Web Interface (Recommended)"
echo "2. Use Render Blueprint (render.yaml)"
echo ""
echo -e "${GREEN}Option 1: Web Interface Deployment${NC}"
echo "-----------------------------------"
echo "1. Go to https://render.com and sign up/login"
echo "2. Click 'New +' → 'Web Service'"
echo "3. Connect your GitHub repository"
echo ""
echo "Backend Configuration:"
echo "  - Name: fake-news-detector-backend"
echo "  - Environment: Python 3"
echo "  - Build Command: cd backend && pip install -r requirements.txt"
echo "  - Start Command: cd backend && python app.py"
echo "  - Add Environment Variable: OPENAI_API_KEY (optional)"
echo ""
echo "4. Click 'New +' → 'Static Site' for frontend"
echo ""
echo "Frontend Configuration:"
echo "  - Name: fake-news-detector-frontend"
echo "  - Build Command: cd frontend && npm install && npm run build"
echo "  - Publish Directory: frontend/build"
echo "  - Add Environment Variable: REACT_APP_BACKEND_URL (your backend URL)"
echo ""
echo -e "${GREEN}Option 2: Blueprint Deployment${NC}"
echo "-------------------------------"
echo "The repository includes a render.yaml file for automatic deployment."
echo "1. Go to https://render.com/deploy"
echo "2. Connect your repository"
echo "3. Render will automatically detect and deploy both services"
echo ""

# Check if render.yaml exists
if [ ! -f "render.yaml" ]; then
    echo -e "${YELLOW}render.yaml not found. Creating it now...${NC}"
    
    cat > render.yaml << 'EOF'
services:
  # Backend Service
  - type: web
    name: fake-news-detector-backend
    env: python
    region: oregon
    plan: free
    buildCommand: "cd backend && pip install -r requirements.txt"
    startCommand: "cd backend && python app.py"
    envVars:
      - key: OPENAI_API_KEY
        sync: false
      - key: FLASK_ENV
        value: production
    healthCheckPath: /

  # Frontend Service
  - type: web
    name: fake-news-detector-frontend
    env: static
    region: oregon
    plan: free
    buildCommand: "cd frontend && npm install && npm run build"
    staticPublishPath: frontend/build
    envVars:
      - key: REACT_APP_BACKEND_URL
        fromService:
          type: web
          name: fake-news-detector-backend
          property: host
EOF
    
    echo -e "${GREEN}✅ render.yaml created successfully!${NC}"
fi

echo ""
echo -e "${GREEN}🎉 Ready to Deploy!${NC}"
echo ""
echo "Next steps:"
echo "1. Commit the render.yaml file (if just created)"
echo "2. Push to your GitHub repository"
echo "3. Visit https://render.com and deploy"
echo ""
echo "📚 For detailed instructions, see DEMO.md"
echo ""
