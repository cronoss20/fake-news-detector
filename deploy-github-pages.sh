#!/bin/bash

# GitHub Pages Deployment Script
# This script builds the React frontend and deploys it to the docs/ folder for GitHub Pages

set -e

echo "🚀 Building Fake News Detector for GitHub Pages..."
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Navigate to frontend directory
cd frontend

echo "📦 Installing dependencies..."
npm install

echo ""
echo "🔨 Building production bundle..."
# Set the backend URL - you can change this to your deployed backend
REACT_APP_BACKEND_URL=https://fake-news-detector-backend.onrender.com npm run build

echo ""
echo "📁 Copying build to docs/ folder..."
cd ..
rm -rf docs/
mkdir -p docs
cp -r frontend/build/* docs/

echo ""
echo -e "${GREEN}✅ Build completed successfully!${NC}"
echo ""
echo "Next steps:"
echo "1. Commit the changes: git add docs/ frontend/package.json"
echo "2. Push to GitHub: git push origin main"
echo "3. Enable GitHub Pages in repository settings:"
echo "   - Go to Settings > Pages"
echo "   - Source: Deploy from a branch"
echo "   - Branch: main, Folder: /docs"
echo "4. Your demo will be available at: https://cronoss20.github.io/fake-news-detector/"
echo ""
echo -e "${YELLOW}Note:${NC} Make sure your backend is deployed and accessible."
echo "The current backend URL is: https://fake-news-detector-backend.onrender.com"
echo ""
