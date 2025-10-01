# 🚀 Live Demo Setup Guide

This guide provides comprehensive instructions for deploying the Fake News Detector as a publicly accessible live demo.

## 📋 Table of Contents

- [Overview](#overview)
- [Security Considerations](#security-considerations)
- [Deployment Options](#deployment-options)
- [Quick Deploy (Recommended)](#quick-deploy-recommended)
- [Manual Deployment](#manual-deployment)
- [Configuration](#configuration)
- [Testing the Demo](#testing-the-demo)

## 🔍 Overview

The Fake News Detector consists of two components:
- **Backend**: Flask API server (Python)
- **Frontend**: React single-page application (JavaScript)

Both components can be deployed separately for optimal performance and scalability.

## 🔒 Security Considerations

### Data Privacy
- **No User Data Storage**: The application does not store any user-submitted content
- **Temporary Processing**: All text and URL analysis is performed in-memory only
- **No Logging of Content**: User inputs are not logged to any persistent storage

### API Key Security
- **Environment Variables**: OpenAI API key is stored securely in environment variables
- **Demo Mode**: The app works without API key using heuristic analysis
- **Never Expose Keys**: API keys are never sent to the frontend or exposed in responses

### Input Validation
- **URL Sanitization**: All URLs are validated before processing
- **Rate Limiting**: Consider implementing rate limiting for production deployments
- **CORS Configuration**: Backend uses CORS to accept requests only from trusted origins

### Recommended Security Measures
1. Use environment variables for all sensitive configuration
2. Enable HTTPS for all public deployments
3. Implement rate limiting to prevent abuse
4. Set up monitoring and alerting for unusual activity
5. Keep dependencies updated regularly

## 🚀 Deployment Options

### Option 1: Render (Recommended - Free Tier Available)

**Backend Deployment:**
1. Fork this repository to your GitHub account
2. Go to [Render.com](https://render.com) and sign up
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Configure:
   - **Name**: `fake-news-detector-backend`
   - **Environment**: `Python 3`
   - **Build Command**: `cd backend && pip install -r requirements.txt`
   - **Start Command**: `cd backend && python app.py`
   - **Environment Variables**: Add `OPENAI_API_KEY` (optional)

**Frontend Deployment:**
1. In Render, click "New +" → "Static Site"
2. Connect your GitHub repository
3. Configure:
   - **Name**: `fake-news-detector-frontend`
   - **Build Command**: `cd frontend && npm install && npm run build`
   - **Publish Directory**: `frontend/build`
   - **Environment Variables**: 
     - `REACT_APP_BACKEND_URL`: Your backend URL (e.g., `https://fake-news-detector-backend.onrender.com`)

### Option 2: Railway.app (Free Tier Available)

1. Go to [Railway.app](https://railway.app) and sign up
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Railway will auto-detect and deploy both services
5. Add environment variables:
   - `OPENAI_API_KEY` (optional for backend)
   - `REACT_APP_BACKEND_URL` (frontend)

### Option 3: Vercel (Frontend) + Render (Backend)

**Backend on Render** (see Option 1)

**Frontend on Vercel:**
1. Go to [Vercel.com](https://vercel.com) and sign up
2. Click "New Project" → Import your repository
3. Configure:
   - **Framework Preset**: Create React App
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `build`
   - **Environment Variables**: Add `REACT_APP_BACKEND_URL`

### Option 4: Heroku (Requires Credit Card)

1. Install Heroku CLI: `npm install -g heroku`
2. Login: `heroku login`
3. Create app: `heroku create your-app-name`
4. Add buildpacks:
   ```bash
   heroku buildpacks:add heroku/python
   heroku buildpacks:add heroku/nodejs
   ```
5. Set environment variables:
   ```bash
   heroku config:set OPENAI_API_KEY=your_key_here
   ```
6. Deploy:
   ```bash
   git push heroku main
   ```

### Option 5: Docker + Cloud Run (Google Cloud)

1. Build the Docker image:
   ```bash
   docker build -t fake-news-detector .
   ```
2. Push to Google Container Registry:
   ```bash
   docker tag fake-news-detector gcr.io/YOUR_PROJECT/fake-news-detector
   docker push gcr.io/YOUR_PROJECT/fake-news-detector
   ```
3. Deploy to Cloud Run:
   ```bash
   gcloud run deploy fake-news-detector \
     --image gcr.io/YOUR_PROJECT/fake-news-detector \
     --platform managed \
     --allow-unauthenticated
   ```

## ⚡ Quick Deploy (Recommended)

### Using Deploy Scripts

We provide one-click deployment scripts for popular platforms:

**Render Deployment:**
```bash
./deploy/render-deploy.sh
```

**Railway Deployment:**
```bash
./deploy/railway-deploy.sh
```

**Vercel + Render:**
```bash
./deploy/vercel-render-deploy.sh
```

These scripts will:
1. Check prerequisites
2. Install dependencies
3. Build both frontend and backend
4. Deploy to the selected platform
5. Provide you with live URLs

## 🔧 Manual Deployment

### Backend Setup

1. **Prerequisites:**
   - Python 3.8+
   - pip

2. **Install Dependencies:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Configure Environment:**
   ```bash
   cp .env.example .env
   # Edit .env and add your OPENAI_API_KEY (optional)
   ```

4. **Run Backend:**
   ```bash
   python app.py
   ```
   Backend will run on `http://localhost:5000`

### Frontend Setup

1. **Prerequisites:**
   - Node.js 16+
   - npm or yarn

2. **Install Dependencies:**
   ```bash
   cd frontend
   npm install
   ```

3. **Configure Environment:**
   ```bash
   cp env.example .env
   # Edit .env and set REACT_APP_BACKEND_URL
   ```

4. **Build for Production:**
   ```bash
   npm run build
   ```

5. **Serve Production Build:**
   ```bash
   npm install -g serve
   serve -s build -l 3000
   ```
   Frontend will be available on `http://localhost:3000`

### Docker Deployment

1. **Build Docker Image:**
   ```bash
   docker build -t fake-news-detector .
   ```

2. **Run Container:**
   ```bash
   docker run -p 5000:5000 -e OPENAI_API_KEY=your_key_here fake-news-detector
   ```

3. **Using Docker Compose:**
   ```bash
   docker-compose up -d
   ```

## ⚙️ Configuration

### Environment Variables

**Backend (.env):**
```env
OPENAI_API_KEY=your_openai_api_key_here  # Optional - app works without it
FLASK_ENV=production
PORT=5000
```

**Frontend (.env):**
```env
REACT_APP_BACKEND_URL=https://your-backend-url.com
REACT_APP_ENV=production
```

### Demo Mode

The application works in two modes:

1. **Demo Mode (No API Key)**
   - Uses heuristic analysis based on keyword detection
   - No external API calls
   - Instant results
   - Perfect for testing and demonstration

2. **AI Mode (With API Key)**
   - Uses OpenAI GPT-3.5-turbo for intelligent analysis
   - More accurate results
   - Detailed reasoning
   - Requires OpenAI API key

## 🧪 Testing the Demo

### Local Testing

1. **Start Backend:**
   ```bash
   cd backend && python app.py
   ```

2. **Start Frontend:**
   ```bash
   cd frontend && npm start
   ```

3. **Test Analysis:**
   - Open `http://localhost:3000`
   - Enter test text: "BREAKING: You won't believe this shocking miracle cure!"
   - Click "Analyze"
   - Verify results are displayed

### Production Testing

After deployment, test the following:

1. **Text Analysis:**
   - Enter suspicious text
   - Verify analysis results
   - Check confidence scores

2. **URL Analysis:**
   - Enter a news article URL
   - Verify content extraction
   - Check analysis accuracy

3. **Error Handling:**
   - Test with invalid URLs
   - Test with empty inputs
   - Verify error messages

4. **Mobile Responsiveness:**
   - Test on mobile devices
   - Verify layout adapts properly
   - Check touch interactions

### Health Checks

**Backend Health:**
```bash
curl https://your-backend-url.com/
```
Expected response: `{"status": "Fake News Detector backend running."}`

**Frontend Health:**
Visit your frontend URL and verify the page loads correctly.

## 📊 Monitoring

### Recommended Monitoring Tools

1. **Uptime Monitoring:**
   - [UptimeRobot](https://uptimerobot.com) (Free)
   - [Pingdom](https://www.pingdom.com)

2. **Error Tracking:**
   - [Sentry](https://sentry.io) (Free tier available)
   - [LogRocket](https://logrocket.com)

3. **Analytics:**
   - Google Analytics
   - Plausible Analytics (Privacy-friendly)

### Setting Up Monitoring

1. **Backend Health Endpoint:**
   The backend includes a `/` endpoint for health checks.

2. **Frontend Analytics:**
   Add analytics code to `frontend/public/index.html`

3. **Error Tracking:**
   Integrate Sentry or similar tool in both frontend and backend

## 🆘 Troubleshooting

### Common Issues

**Issue: Backend not accessible**
- Check if backend is running: `curl http://localhost:5000`
- Verify firewall rules allow port 5000
- Check environment variables are set correctly

**Issue: Frontend can't reach backend**
- Verify `REACT_APP_BACKEND_URL` is set correctly
- Check CORS configuration in backend
- Ensure backend URL is accessible from browser

**Issue: OpenAI API errors**
- Verify API key is valid
- Check API quota and billing
- App will fall back to demo mode if API fails

**Issue: URL analysis not working**
- Some websites block scraping
- Check if URL is accessible
- Verify BeautifulSoup is installed

### Getting Help

- Open an issue on GitHub
- Check existing issues for solutions
- Review application logs

## 🎉 Success!

Once deployed, your live demo will be accessible at:
- **Frontend**: `https://your-frontend-url.com`
- **Backend API**: `https://your-backend-url.com`

Share these URLs with users to try the Fake News Detector!

## 📝 Next Steps

1. Add custom domain (optional)
2. Set up monitoring and alerts
3. Implement rate limiting
4. Add user analytics
5. Collect feedback for improvements

## 📄 License

This project is open source and available for demonstration purposes. Always verify results with reliable sources.
