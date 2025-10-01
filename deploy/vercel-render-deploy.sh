#!/bin/bash

# Vercel (Frontend) + Render (Backend) Deployment Script
# This script helps deploy the application with Vercel frontend and Render backend

set -e

echo "🚀 Fake News Detector - Vercel + Render Deployment"
echo "===================================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check prerequisites
echo "📋 Checking prerequisites..."
echo ""

# Check Vercel CLI
if ! command -v vercel &> /dev/null; then
    echo -e "${YELLOW}Vercel CLI not found. Installing...${NC}"
    npm install -g vercel
fi

echo -e "${GREEN}✅ Vercel CLI found${NC}"
echo ""

# Step 1: Deploy Backend to Render
echo "======================================"
echo "STEP 1: Deploy Backend to Render"
echo "======================================"
echo ""
echo "Please follow these steps to deploy the backend:"
echo ""
echo "1. Go to https://render.com and sign up/login"
echo "2. Click 'New +' → 'Web Service'"
echo "3. Connect your GitHub repository"
echo "4. Configure:"
echo "   - Name: fake-news-detector-backend"
echo "   - Environment: Python 3"
echo "   - Build Command: cd backend && pip install -r requirements.txt"
echo "   - Start Command: cd backend && python app.py"
echo "   - Add Environment Variable: OPENAI_API_KEY (optional)"
echo ""
echo "5. Click 'Create Web Service'"
echo ""
echo -e "${YELLOW}Press Enter when backend is deployed and you have the URL...${NC}"
read

echo ""
echo "Please enter your backend URL (e.g., https://fake-news-detector-backend.onrender.com):"
read BACKEND_URL

if [ -z "$BACKEND_URL" ]; then
    echo -e "${RED}Error: Backend URL is required${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Backend URL saved: $BACKEND_URL${NC}"
echo ""

# Step 2: Deploy Frontend to Vercel
echo "======================================"
echo "STEP 2: Deploy Frontend to Vercel"
echo "======================================"
echo ""

# Navigate to frontend directory
cd frontend

# Login to Vercel if needed
echo "🔐 Checking Vercel authentication..."
vercel whoami || vercel login

echo ""
echo "🚀 Deploying frontend to Vercel..."
echo ""

# Deploy to Vercel with environment variable
vercel --prod -e REACT_APP_BACKEND_URL="$BACKEND_URL"

echo ""
echo -e "${GREEN}🎉 Deployment complete!${NC}"
echo ""
echo "Your Fake News Detector is now live!"
echo ""
echo "Backend: $BACKEND_URL"
echo "Frontend: Check the Vercel output above for your frontend URL"
echo ""
echo "📝 To update environment variables later:"
echo "  vercel env add REACT_APP_BACKEND_URL"
echo ""
echo "📚 For detailed instructions, see DEMO.md"
echo ""
