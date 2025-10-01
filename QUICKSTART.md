# 🚀 Quick Start - Deploy in 5 Minutes

Get your Fake News Detector live demo up and running quickly with these streamlined instructions.

## Option 1: Render.com (Easiest - Recommended) ⭐

**Time: ~5 minutes | Cost: Free**

### Backend Deployment

1. **Fork this repository** to your GitHub account

2. Go to [render.com](https://render.com) and sign up (free)

3. Click **"New +"** → **"Web Service"**

4. Select **"Build and deploy from a Git repository"**

5. Connect your forked repository

6. Configure:
   ```
   Name: fake-news-detector-backend
   Environment: Python 3
   Build Command: cd backend && pip install -r requirements.txt
   Start Command: cd backend && python app.py
   ```

7. Add Environment Variable (optional):
   ```
   OPENAI_API_KEY = your_api_key_here
   ```

8. Click **"Create Web Service"**

9. **Copy your backend URL** (e.g., `https://fake-news-detector-backend.onrender.com`)

### Frontend Deployment

1. In Render, click **"New +"** → **"Static Site"**

2. Select your repository again

3. Configure:
   ```
   Name: fake-news-detector-frontend
   Build Command: cd frontend && npm install && npm run build
   Publish Directory: frontend/build
   ```

4. Add Environment Variable:
   ```
   REACT_APP_BACKEND_URL = [your backend URL from step 9 above]
   ```

5. Click **"Create Static Site"**

6. **Done!** Your frontend URL will be shown (e.g., `https://fake-news-detector-frontend.onrender.com`)

### ✅ Test Your Deployment

Visit your frontend URL and try analyzing this text:
```
BREAKING: You won't believe this shocking miracle cure that doctors hate!
```

---

## Option 2: Vercel (Frontend) + Render (Backend)

**Time: ~7 minutes | Cost: Free**

### Backend on Render

Follow steps 1-9 from Option 1 above for backend deployment.

### Frontend on Vercel

1. Install Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. Navigate to frontend directory:
   ```bash
   cd frontend
   ```

3. Deploy:
   ```bash
   vercel --prod
   ```

4. When prompted, set environment variable:
   ```
   REACT_APP_BACKEND_URL = [your Render backend URL]
   ```

5. **Done!** Vercel will provide your live URL.

---

## Option 3: Railway.app (All-in-One)

**Time: ~5 minutes | Cost: Free**

1. **Fork this repository** to your GitHub account

2. Go to [railway.app](https://railway.app) and sign up

3. Click **"New Project"** → **"Deploy from GitHub repo"**

4. Select your forked repository

5. Railway will auto-detect and deploy both services

6. Add environment variables:
   - For backend: `OPENAI_API_KEY` (optional)
   - For frontend: `REACT_APP_BACKEND_URL` (use your backend URL)

7. **Done!** Railway provides URLs for both services.

---

## Option 4: Netlify (Frontend Only)

**Best for: Static frontend deployment**

### Deploy with Netlify CLI

1. Install Netlify CLI:
   ```bash
   npm install -g netlify-cli
   ```

2. Deploy:
   ```bash
   cd frontend
   netlify deploy --prod
   ```

3. Set environment variable in Netlify dashboard:
   ```
   REACT_APP_BACKEND_URL = [your backend URL]
   ```

### Deploy with Netlify UI

1. Go to [netlify.com](https://netlify.com) and sign up

2. Click **"Add new site"** → **"Import an existing project"**

3. Connect your repository

4. Configure:
   ```
   Base directory: frontend
   Build command: npm run build
   Publish directory: frontend/build
   ```

5. Add environment variable:
   ```
   REACT_APP_BACKEND_URL = [your backend URL]
   ```

---

## 🎮 Using Deploy Scripts

We provide automated deployment scripts for convenience:

### Render Deployment
```bash
./deploy/render-deploy.sh
```

### Railway Deployment
```bash
./deploy/railway-deploy.sh
```

### Vercel + Render Deployment
```bash
./deploy/vercel-render-deploy.sh
```

---

## 🔧 Environment Variables

### Backend (.env)
```env
OPENAI_API_KEY=sk-...        # Optional - works without it
FLASK_ENV=production
PORT=5000
```

### Frontend (.env)
```env
REACT_APP_BACKEND_URL=https://your-backend-url.com
```

---

## ✅ Post-Deployment Checklist

- [ ] Backend is accessible (visit `/` endpoint)
- [ ] Frontend loads correctly
- [ ] Text analysis works
- [ ] URL analysis works
- [ ] Error handling works (test with invalid inputs)
- [ ] Mobile responsive (test on phone)
- [ ] HTTPS is enabled

---

## 🧪 Testing Your Deployment

### Test Backend Health
```bash
curl https://your-backend-url.com/
```
Expected response: `{"status": "Fake News Detector backend running."}`

### Test Text Analysis
```bash
curl -X POST https://your-backend-url.com/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "BREAKING: shocking news that will change everything!"}'
```

### Test URL Analysis (requires backend)
Visit your frontend URL and try analyzing a news article URL.

---

## 🐛 Troubleshooting

### Backend Issues

**Problem**: Backend returns 500 error
- **Solution**: Check logs on hosting platform
- Verify environment variables are set
- Ensure dependencies installed correctly

**Problem**: API errors even with valid key
- **Solution**: Check OpenAI API key is correct
- Verify API quota hasn't been exceeded
- App will fall back to demo mode automatically

### Frontend Issues

**Problem**: Frontend can't reach backend
- **Solution**: Check `REACT_APP_BACKEND_URL` is set correctly
- Ensure backend URL is accessible
- Verify CORS is configured properly

**Problem**: Blank page after deployment
- **Solution**: Check browser console for errors
- Verify build completed successfully
- Check environment variables

### Common Issues

**CORS Errors**
```python
# In backend/app.py, update CORS configuration
CORS(app, origins=["https://your-frontend-domain.com"])
```

**Build Failures**
- Ensure Node.js version is 16+ for frontend
- Ensure Python version is 3.8+ for backend
- Check all dependencies are in requirements.txt/package.json

---

## 📊 Monitoring Your Demo

### Free Monitoring Tools

1. **UptimeRobot** - Monitor uptime
   - Add your URLs
   - Get alerts if site goes down

2. **Platform Dashboards**
   - Render: Check analytics in dashboard
   - Vercel: View deployment logs and analytics
   - Railway: Monitor resource usage

3. **Browser DevTools**
   - Check Network tab for API calls
   - Check Console for JavaScript errors

---

## 🎉 Success!

Your Fake News Detector is now live! Share your demo URL with others:

```
🌐 Frontend: https://your-frontend-url.com
📡 Backend: https://your-backend-url.com
```

### Next Steps

1. ⭐ Star this repository
2. 🔗 Add your live demo URL to README
3. 📢 Share on social media
4. 🛡️ Review [SECURITY.md](SECURITY.md) for best practices
5. 📚 Read full [DEMO.md](DEMO.md) for advanced options

---

## 📚 Additional Resources

- [Full Deployment Guide](DEMO.md)
- [Security Best Practices](SECURITY.md)
- [GitHub Repository](https://github.com/cronoss20/fake-news-detector)

---

## 🆘 Need Help?

- 📖 Check [DEMO.md](DEMO.md) for detailed instructions
- 🐛 Open an issue on GitHub
- 💬 Check existing issues for solutions

---

**Total Time**: 5-10 minutes
**Total Cost**: $0 (Free tier)
**Difficulty**: Beginner-friendly

Happy deploying! 🚀
