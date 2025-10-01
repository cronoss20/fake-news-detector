# 📰 Fake News Detector

[![Deploy to Render](https://img.shields.io/badge/Deploy%20to-Render-46E3B7?style=for-the-badge&logo=render)](https://render.com)
[![Deploy to Railway](https://img.shields.io/badge/Deploy%20to-Railway-0B0D0E?style=for-the-badge&logo=railway)](https://railway.app)
[![Deploy to Vercel](https://img.shields.io/badge/Deploy%20to-Vercel-000000?style=for-the-badge&logo=vercel)](https://vercel.com)

This is a complete fake news detection system that analyzes text content and URLs to identify potential misinformation using OpenAI's GPT model, with a beautiful React frontend interface.

## 🌐 Live Demo

Want to deploy your own live demo? Check out our deployment guides:

- **[🚀 Quick Start (5 minutes)](QUICKSTART.md)** - Deploy in 5 minutes with free hosting
- **[📖 Full Deployment Guide](DEMO.md)** - Comprehensive deployment instructions
- **[🔒 Security Guide](SECURITY.md)** - Security best practices and considerations
- **[📋 Deployment Checklist](DEPLOYMENT_CHECKLIST.md)** - Ensure nothing is missed

### Deployment Options

| Platform | Backend | Frontend | Free Tier | Setup Time |
|----------|---------|----------|-----------|------------|
| **Render** | ✅ | ✅ | ✅ Yes | ~5 min |
| **Railway** | ✅ | ✅ | ✅ Yes | ~5 min |
| **Vercel + Render** | ✅ | ✅ | ✅ Yes | ~7 min |
| **Netlify + Render** | ✅ | ✅ | ✅ Yes | ~7 min |

> **Try it now!** Follow the [Quick Start Guide](QUICKSTART.md) to deploy your own instance for free.

## 🚀 Features Implemented

### Backend (Flask + AI Integration)
- **Flask API Server** with comprehensive error handling and CORS support
- **OpenAI GPT-3.5-turbo Integration** for intelligent fake news analysis
- **Smart Fallback System** - works in demo mode without API key using heuristic analysis
- **URL Content Extraction** using BeautifulSoup to scrape and analyze web articles
- **Two Analysis Endpoints:**
  - `/predict` - Direct text analysis
  - `/analyze` - URL content analysis
- **Confidence Scoring** - Returns percentage-based reliability assessment
- **Red Flag Detection** - Identifies specific misinformation indicators

### Frontend (React)
- **Professional UI/UX** with responsive design and modern styling
- **Dual Input Modes** - Toggle between text analysis and URL analysis
- **Real-time Analysis** with loading states and comprehensive error handling
- **Detailed Results Display** showing confidence scores, reasoning, and red flags
- **Mobile-Friendly** responsive design that works on all devices

### Configuration & Deployment
- **Docker Support** - Complete containerization with multi-stage builds
- **Development Scripts** - Easy startup scripts for Windows and Linux
- **Production Ready** - Includes Heroku Procfile and deployment configurations
- **Environment Management** - Proper handling of API keys and configuration

## 🎯 How It Works

1. **Text Analysis**: Users can paste suspicious text directly for immediate analysis
2. **URL Analysis**: Users can enter news article URLs to extract and analyze content
3. **AI Processing**: Uses GPT-3.5-turbo to evaluate content for misinformation indicators
4. **Results Display**: Shows whether content is likely fake news with confidence percentage and specific red flags

## 🖼️ Screenshots

**Main Interface:**
![Fake News Detector Interface](https://github.com/user-attachments/assets/372e902b-848f-4d06-ba59-e511b34e4198)

**Analysis Results:**
![Analysis Results](https://github.com/user-attachments/assets/0f057593-5cc7-4bdd-ae14-9370fd7b9e1b)

## 🛠️ Technical Details

- **Backend**: Python Flask with OpenAI API integration, BeautifulSoup for web scraping
- **Frontend**: React with Axios for API communication, responsive CSS design
- **AI Model**: GPT-3.5-turbo for intelligent content analysis
- **Deployment**: Docker containers, Heroku/Render support, GitHub Pages ready
- **Error Handling**: Graceful fallbacks, user-friendly error messages

## 🚀 Quick Start

The system can be started easily using the provided scripts:

```bash
# Start both backend and frontend
./start-dev.sh

# Or manually:
cd backend && python app.py  # Backend on :5000
cd frontend && npm start     # Frontend on :3000
```

## 📋 Demo Mode

The system works immediately without requiring an OpenAI API key by providing intelligent heuristic analysis. For full AI-powered analysis, users can add their OpenAI API key to the `.env` file.

## 🔧 Files Added/Modified

### Core Application
- `backend/` - Complete Flask application with AI integration
- `frontend/` - React application with modern UI/UX
- `docker-compose.yml` - Container orchestration

### Deployment & Configuration
- `render.yaml` - Render.com deployment configuration
- `railway.json` - Railway.app deployment configuration
- `netlify.toml` - Netlify deployment configuration
- `frontend/vercel.json` - Vercel deployment configuration
- `Procfile` - Heroku/general deployment configuration
- `.github/workflows/deploy.yml` - Automated deployment workflow

### Deployment Scripts
- `deploy/render-deploy.sh` - Automated Render deployment
- `deploy/railway-deploy.sh` - Automated Railway deployment
- `deploy/vercel-render-deploy.sh` - Hybrid Vercel + Render deployment
- `deploy/README.md` - Deployment scripts documentation

### Documentation
- `README.md` - Main documentation with deployment overview
- `DEMO.md` - Comprehensive live demo deployment guide
- `QUICKSTART.md` - 5-minute quick start deployment guide
- `SECURITY.md` - Security best practices and considerations
- `DEPLOYMENT_CHECKLIST.md` - Complete deployment verification checklist

### Environment & Configuration
- `backend/.env.example` - Backend environment variable template
- `frontend/env.example` - Frontend environment variable template
- `.gitignore` - Excludes sensitive files and build artifacts

This implementation provides a production-ready fake news detection system that combines modern web technologies with AI-powered analysis, making it easy for users to identify potential misinformation in text content and news articles.

## 📚 Documentation Structure

```
📁 fake-news-detector/
├── 📄 README.md                    # Main documentation
├── 📄 QUICKSTART.md                # 5-minute deployment guide
├── 📄 DEMO.md                      # Comprehensive deployment guide
├── 📄 SECURITY.md                  # Security best practices
├── 📄 DEPLOYMENT_CHECKLIST.md      # Deployment verification
├── 📁 deploy/                      # Deployment automation scripts
│   ├── render-deploy.sh
│   ├── railway-deploy.sh
│   └── vercel-render-deploy.sh
├── 📁 backend/                     # Flask API server
└── 📁 frontend/                    # React application
```

## 🎯 Getting Started

1. **Local Development**: Follow the [Quick Start](#-quick-start) section above
2. **Deploy Live Demo**: See [QUICKSTART.md](QUICKSTART.md) for 5-minute deployment
3. **Production Deployment**: See [DEMO.md](DEMO.md) for comprehensive guide
4. **Security Setup**: Review [SECURITY.md](SECURITY.md) before going live

> [!WARNING]
>
> <details>
> <summary>Firewall rules blocked me from connecting to one or more addresses (expand for details)</summary>
>
> #### I tried to connect to the following addresses, but was blocked by firewall rules:
>
> - `example.com`
>   - Triggering command: `/home/REDACTED/work/fake-news-detector/fake-news-detector/backend/venv/bin/python app.py` (dns block)
>
> If you need me to access, download, or install something from one of these locations, you can either:
>
> - Configure [Actions setup steps](https://gh.io/copilot/actions-setup-steps) to set up my environment, which run before the firewall is enabled
> - Add the appropriate URLs or hosts to the custom allowlist in this repository's [Copilot coding agent settings](https://github.com/cronoss20/fake-news-detector/settings/copilot/coding_agent) (admins only)
>
> </details>
