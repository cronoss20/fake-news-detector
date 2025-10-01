#!/bin/bash

# Railway.app Deployment Script for Fake News Detector
# This script helps deploy the application to Railway.app

set -e

echo "🚂 Fake News Detector - Railway Deployment Script"
echo "==================================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if Railway CLI is installed
echo "📋 Checking prerequisites..."
if ! command -v railway &> /dev/null; then
    echo -e "${YELLOW}Railway CLI not found. Installing...${NC}"
    echo ""
    echo "To install Railway CLI:"
    echo "  npm install -g @railway/cli"
    echo "  or"
    echo "  brew install railway"
    echo ""
    echo "After installation, run this script again."
    exit 1
fi

echo -e "${GREEN}✅ Railway CLI found${NC}"
echo ""

# Check if logged in to Railway
echo "🔐 Checking Railway authentication..."
if ! railway whoami &> /dev/null; then
    echo -e "${YELLOW}Not logged in to Railway. Please login:${NC}"
    railway login
    echo ""
fi

echo -e "${GREEN}✅ Authenticated with Railway${NC}"
echo ""

# Check if git repo is clean
if [[ -n $(git status -s) ]]; then
    echo -e "${YELLOW}Warning: You have uncommitted changes. Please commit them before deploying.${NC}"
    echo ""
fi

echo "🚀 Deploying to Railway..."
echo ""

# Check if project exists
if [ ! -f "railway.json" ]; then
    echo "📦 Creating new Railway project..."
    railway init
else
    echo "📦 Using existing Railway project..."
fi

echo ""
echo "🔧 Setting up environment variables..."
echo ""
echo -e "${YELLOW}Please enter your OpenAI API key (or press Enter to skip for demo mode):${NC}"
read -s OPENAI_KEY

if [ -n "$OPENAI_KEY" ]; then
    railway variables set OPENAI_API_KEY="$OPENAI_KEY"
    echo -e "${GREEN}✅ OpenAI API key configured${NC}"
else
    echo -e "${YELLOW}⚠️  No API key provided. App will run in demo mode.${NC}"
fi

echo ""
echo "🚀 Deploying application..."
railway up

echo ""
echo -e "${GREEN}🎉 Deployment initiated!${NC}"
echo ""
echo "📊 Check deployment status:"
echo "  railway status"
echo ""
echo "🌐 Get your app URL:"
echo "  railway domain"
echo ""
echo "📝 View logs:"
echo "  railway logs"
echo ""
echo "For more Railway commands:"
echo "  railway --help"
echo ""
echo "📚 For detailed instructions, see DEMO.md"
echo ""
