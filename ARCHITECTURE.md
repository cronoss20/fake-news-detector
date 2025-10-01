# 🎨 Deployment Architecture

This document provides a visual overview of the deployment architecture and options for the Fake News Detector.

## 📊 System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Fake News Detector                        │
│                     Live Demo System                         │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
          ┌──────────────────────────────────────┐
          │                                      │
          ▼                                      ▼
┌──────────────────┐                  ┌──────────────────┐
│   Frontend       │                  │    Backend       │
│   (React SPA)    │◄─────────────────│   (Flask API)    │
│                  │   API Requests   │                  │
└──────────────────┘                  └──────────────────┘
         │                                      │
         │                                      │
         ▼                                      ▼
┌──────────────────┐                  ┌──────────────────┐
│  Static Hosting  │                  │  Python Hosting  │
│  - Vercel        │                  │  - Render.com    │
│  - Netlify       │                  │  - Railway.app   │
│  - Render        │                  │  - Heroku        │
└──────────────────┘                  └──────────────────┘
                                               │
                                               ▼
                                      ┌──────────────────┐
                                      │  OpenAI API      │
                                      │  (Optional)      │
                                      └──────────────────┘
```

## 🚀 Deployment Options

### Option 1: Render (All-in-One)
```
GitHub Repository
       │
       ├──► Render Backend Service ──┐
       │    (Python Web Service)      │
       │                              ├──► Live Demo
       └──► Render Frontend Site ─────┘
            (Static Site)
```

**Pros:**
- ✅ Single platform for everything
- ✅ Free tier available
- ✅ Automatic HTTPS
- ✅ Easy environment variables

**Cons:**
- ⚠️ Cold starts on free tier
- ⚠️ Limited to 750 hours/month

### Option 2: Vercel + Render
```
GitHub Repository
       │
       ├──► Render Backend Service ──┐
       │    (Python Web Service)      │
       │                              ├──► Live Demo
       └──► Vercel Static Site ───────┘
            (React Frontend)
```

**Pros:**
- ✅ Best frontend performance
- ✅ Global CDN with Vercel
- ✅ Generous free tier
- ✅ Instant cache invalidation

**Cons:**
- ⚠️ Two platforms to manage
- ⚠️ Requires CORS configuration

### Option 3: Railway (Auto-Deploy)
```
GitHub Repository
       │
       └──► Railway Project
            │
            ├──► Service 1: Backend
            │    (Auto-detected)
            │
            └──► Service 2: Frontend
                 (Auto-detected)
```

**Pros:**
- ✅ Automatic service detection
- ✅ Simple CLI
- ✅ Built-in database support
- ✅ Great developer experience

**Cons:**
- ⚠️ Credit card required
- ⚠️ Limited free tier

### Option 4: Netlify + Render
```
GitHub Repository
       │
       ├──► Render Backend Service ──┐
       │    (Python Web Service)      │
       │                              ├──► Live Demo
       └──► Netlify Static Site ──────┘
            (React Frontend)
```

**Pros:**
- ✅ Excellent for static sites
- ✅ Built-in forms & functions
- ✅ Generous free tier
- ✅ Great CI/CD

**Cons:**
- ⚠️ Two platforms to manage
- ⚠️ Requires CORS configuration

## 🔄 Request Flow

```
┌──────────┐
│  User    │
└────┬─────┘
     │ 1. Opens Website
     ▼
┌──────────────────┐
│  Frontend (CDN)  │
│  React App       │
└────┬─────────────┘
     │ 2. User submits text/URL
     ▼
┌──────────────────┐
│  Backend API     │
│  Flask Server    │
└────┬─────────────┘
     │
     ├─ 3a. API Key? ──Yes──► ┌──────────────┐
     │                        │  OpenAI GPT  │
     │                        └──────┬───────┘
     │                               │ AI Analysis
     │                               ▼
     └─ 3b. No API Key ──────► ┌──────────────┐
                               │  Heuristic   │
                               │  Analysis    │
                               └──────┬───────┘
                                      │
     ┌────────────────────────────────┘
     │ 4. Return Results
     ▼
┌──────────────────┐
│  Frontend        │
│  Display Results │
└────┬─────────────┘
     │ 5. Show to User
     ▼
┌──────────┐
│  User    │
└──────────┘
```

## 🔐 Security Architecture

```
┌──────────────────────────────────────────────────────────┐
│                    Security Layers                        │
└──────────────────────────────────────────────────────────┘
                              │
          ┌──────────────────┬┴┬──────────────────┐
          ▼                  ▼ ▼                  ▼
    ┌─────────┐      ┌──────────┐       ┌─────────────┐
    │  HTTPS  │      │   CORS   │       │Input Valid. │
    │  SSL    │      │ Config   │       │Sanitization │
    └─────────┘      └──────────┘       └─────────────┘
          │                  │                   │
          └──────────────────┼───────────────────┘
                             │
                    ┌────────▼────────┐
                    │  Environment    │
                    │  Variables      │
                    │  - API Keys     │
                    │  - Secrets      │
                    └─────────────────┘
                             │
                    ┌────────▼────────┐
                    │  No Data        │
                    │  Storage        │
                    │  - Memory Only  │
                    │  - No Logs      │
                    └─────────────────┘
```

## 📦 Deployment Pipeline

```
┌─────────────┐
│  Developer  │
└──────┬──────┘
       │ git push
       ▼
┌─────────────────┐
│  GitHub Repo    │
└──────┬──────────┘
       │ Webhook
       ▼
┌─────────────────────────────────────────┐
│         Hosting Platform                │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐│
│  │  Build  │→ │  Test   │→ │ Deploy  ││
│  └─────────┘  └─────────┘  └─────────┘│
└────────────────────┬────────────────────┘
                     │
       ┌─────────────┼─────────────┐
       ▼             ▼             ▼
┌───────────┐ ┌───────────┐ ┌───────────┐
│   CDN     │ │  Backend  │ │   SSL     │
│   Cache   │ │  Server   │ │   Cert    │
└───────────┘ └───────────┘ └───────────┘
       │             │             │
       └─────────────┼─────────────┘
                     │
                     ▼
              ┌─────────────┐
              │  Live Demo  │
              └─────────────┘
```

## 🛠️ Quick Deployment Comparison

| Feature | Render | Railway | Vercel+Render | Netlify+Render |
|---------|--------|---------|---------------|----------------|
| Setup Time | 5 min | 5 min | 7 min | 7 min |
| Free Tier | ✅ | ✅ | ✅ | ✅ |
| Auto Deploy | ✅ | ✅ | ✅ | ✅ |
| HTTPS/SSL | ✅ | ✅ | ✅ | ✅ |
| Custom Domain | ✅ | ✅ | ✅ | ✅ |
| Environment Vars | ✅ | ✅ | ✅ | ✅ |
| Single Platform | ✅ | ✅ | ❌ | ❌ |
| Best Performance | Good | Good | Excellent | Excellent |
| Complexity | Low | Low | Medium | Medium |

## 🎯 Recommended Setup

### For Beginners
```
Render (Backend + Frontend)
↓
Simple, all-in-one solution
Fast deployment
Minimal configuration
```

### For Production
```
Vercel (Frontend) + Render (Backend)
↓
Excellent performance
Global CDN
Separate scaling
More control
```

### For Developers
```
Railway (Backend + Frontend)
↓
Great CLI experience
Automatic detection
Easy environment management
Built-in monitoring
```

## 📖 Resources

- [QUICKSTART.md](QUICKSTART.md) - Start deploying in 5 minutes
- [DEMO.md](DEMO.md) - Comprehensive deployment guide
- [SECURITY.md](SECURITY.md) - Security best practices
- [DEPLOYMENT_CHECKLIST.md](DEPLOYMENT_CHECKLIST.md) - Verification checklist

---

**Choose your deployment path and start building your live demo today!** 🚀
