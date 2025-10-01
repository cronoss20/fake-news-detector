# 📄 GitHub Pages Deployment Guide

This guide explains how to deploy and maintain the Fake News Detector on GitHub Pages.

## 🌐 Live Demo

The application is live at: **[https://cronoss20.github.io/fake-news-detector/](https://cronoss20.github.io/fake-news-detector/)**

## 🚀 Quick Deploy

### Option 1: Using the Deployment Script (Recommended)

```bash
# Run the automated deployment script
./deploy-github-pages.sh
```

This script will:
1. Install frontend dependencies
2. Build the production bundle
3. Copy files to the `docs/` folder
4. Create the `.nojekyll` file
5. Provide next steps for pushing to GitHub

### Option 2: Manual Deployment

```bash
# Navigate to frontend
cd frontend

# Install dependencies (if not already installed)
npm install

# Build for production
REACT_APP_BACKEND_URL=https://your-backend-url.com npm run build

# Go back to root and prepare docs folder
cd ..
rm -rf docs/
mkdir -p docs
cp -r frontend/build/* docs/

# Create .nojekyll file
touch docs/.nojekyll

# Commit and push
git add docs/ frontend/package.json
git commit -m "Update GitHub Pages deployment"
git push origin main
```

## ⚙️ Configuration

### Frontend Package.json

The `frontend/package.json` must include the `homepage` field:

```json
{
  "name": "fake-news-detector-frontend",
  "version": "1.0.0",
  "homepage": "/fake-news-detector",
  ...
}
```

This tells React to use the correct base path for routing on GitHub Pages.

### Backend URL Configuration

The frontend connects to a backend API. To change the backend URL:

1. **Edit `deploy-github-pages.sh`**:
   ```bash
   REACT_APP_BACKEND_URL=https://your-backend-url.com npm run build
   ```

2. **Or set it when building manually**:
   ```bash
   REACT_APP_BACKEND_URL=https://your-backend-url.com npm run build
   ```

### GitHub Pages Settings

To enable GitHub Pages in your repository:

1. Go to your repository on GitHub
2. Click **Settings** → **Pages**
3. Under **Source**:
   - Branch: `main`
   - Folder: `/docs`
4. Click **Save**

GitHub will automatically deploy your site and provide the URL.

## 📁 Project Structure

```
fake-news-detector/
├── docs/                          # GitHub Pages deployment
│   ├── .nojekyll                  # Prevents Jekyll processing
│   ├── README.md                  # Docs folder documentation
│   ├── index.html                 # Main HTML file
│   ├── manifest.json              # PWA manifest
│   ├── robots.txt                 # SEO robots file
│   └── static/                    # Static assets
│       ├── css/                   # Compiled CSS
│       └── js/                    # Compiled JavaScript
├── frontend/                      # React source code
│   ├── src/                       # Source files
│   ├── public/                    # Public assets
│   └── package.json               # Frontend dependencies
└── deploy-github-pages.sh         # Deployment script
```

## 🔄 Updating the Deployment

Whenever you make changes to the frontend:

1. **Make your changes** in the `frontend/src/` directory
2. **Test locally**:
   ```bash
   cd frontend
   npm start
   ```
3. **Deploy**:
   ```bash
   ./deploy-github-pages.sh
   ```
4. **Commit and push**:
   ```bash
   git add docs/ frontend/
   git commit -m "Update frontend with [your changes]"
   git push origin main
   ```

GitHub Pages will automatically update within a few minutes.

## 🐛 Troubleshooting

### Issue: 404 Error on GitHub Pages

**Solution**: 
- Ensure the `homepage` field in `frontend/package.json` matches your repository name
- Verify GitHub Pages is enabled and pointing to `/docs` folder
- Check that `.nojekyll` file exists in the `docs/` folder

### Issue: Assets not loading (CSS/JS)

**Solution**:
- Verify the `homepage` field in `package.json` is correct
- Rebuild the application with the deployment script
- Clear your browser cache

### Issue: Backend API not responding

**Solution**:
- Verify your backend is deployed and accessible
- Check the backend URL in `deploy-github-pages.sh`
- Test the backend endpoint directly
- Ensure CORS is configured on the backend

### Issue: Changes not reflecting

**Solution**:
- Wait 2-5 minutes for GitHub Pages to rebuild
- Clear browser cache (Ctrl+Shift+Delete)
- Check the Actions tab in GitHub to see if deployment completed

## 🔐 Security Considerations

### API Keys
- Never commit API keys to the repository
- Backend should handle API key management
- The frontend should not expose sensitive credentials

### CORS
- Backend must allow requests from your GitHub Pages URL
- Example CORS configuration:
  ```python
  CORS(app, resources={
      r"/*": {
          "origins": ["https://cronoss20.github.io"]
      }
  })
  ```

## 📊 Monitoring

### Check Deployment Status
- Go to your repository's **Actions** tab
- Look for "pages build and deployment" workflows
- Check for any errors or warnings

### Analytics (Optional)
You can add Google Analytics or other tracking to monitor usage:
1. Add tracking script to `frontend/public/index.html`
2. Rebuild and deploy

## 🚀 Advanced: Custom Domain

To use a custom domain with GitHub Pages:

1. **Update `frontend/package.json`**:
   ```json
   "homepage": "https://your-custom-domain.com"
   ```

2. **Create `docs/CNAME` file**:
   ```
   your-custom-domain.com
   ```

3. **Configure DNS** at your domain registrar:
   - Add a CNAME record pointing to `username.github.io`
   - Or A records to GitHub Pages IPs

4. **Update GitHub Settings**:
   - Settings → Pages → Custom domain
   - Enter your domain and save

5. **Rebuild and deploy**:
   ```bash
   ./deploy-github-pages.sh
   ```

## 📚 Additional Resources

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Create React App Deployment](https://create-react-app.dev/docs/deployment/)
- [Main Repository README](../README.md)
- [Quick Start Guide](../QUICKSTART.md)
- [Full Deployment Guide](../DEMO.md)

## 🆘 Getting Help

If you encounter issues:

1. Check this troubleshooting guide
2. Review the [main documentation](../README.md)
3. Check existing [GitHub Issues](https://github.com/cronoss20/fake-news-detector/issues)
4. Create a new issue with:
   - Description of the problem
   - Steps to reproduce
   - Expected vs actual behavior
   - Browser and OS information

---

**Last Updated**: October 2024
