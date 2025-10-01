# 🚀 Quick Reference: GitHub Pages Setup

## For Repository Owner: Enable GitHub Pages in 3 Steps

### Step 1: Go to Settings
1. Navigate to your repository on GitHub
2. Click **Settings** (top menu)
3. Click **Pages** (left sidebar under "Code and automation")

### Step 2: Configure Source
1. Under "Build and deployment"
2. Set **Source**: `Deploy from a branch`
3. Set **Branch**: `main`
4. Set **Folder**: `/docs`
5. Click **Save**

### Step 3: Wait and Access
1. Wait 2-5 minutes for deployment
2. GitHub will show the URL at the top of the Pages settings
3. Your demo will be live at: `https://cronoss20.github.io/fake-news-detector/`

---

## To Update the Live Demo

### Quick Update (Recommended)
```bash
./deploy-github-pages.sh
git add docs/ frontend/
git commit -m "Update demo"
git push origin main
```

### Change Backend URL
Edit `deploy-github-pages.sh` line 25:
```bash
REACT_APP_BACKEND_URL=https://your-new-backend-url.com npm run build
```

---

## Troubleshooting

**Issue**: 404 Error
- **Fix**: Wait 5 minutes, GitHub Pages takes time to deploy
- **Check**: Settings → Pages shows "Your site is live"

**Issue**: Blank page
- **Fix**: Clear browser cache (Ctrl+Shift+Delete)
- **Check**: View browser console for errors

**Issue**: Assets not loading
- **Fix**: Verify `homepage: "/fake-news-detector"` in `frontend/package.json`
- **Rebuild**: Run `./deploy-github-pages.sh`

---

## Documentation

- **Complete Guide**: [GITHUB_PAGES.md](GITHUB_PAGES.md)
- **Implementation Details**: [GITHUB_PAGES_IMPLEMENTATION.md](GITHUB_PAGES_IMPLEMENTATION.md)
- **Main README**: [README.md](README.md)

---

## Support

If you encounter issues:
1. Check [GITHUB_PAGES.md](GITHUB_PAGES.md) troubleshooting section
2. Verify GitHub Pages is enabled in Settings
3. Wait 5-10 minutes for deployment to complete
4. Check GitHub Actions tab for deployment status

---

**Quick Links:**
- 🔧 [GitHub Pages Settings](https://github.com/cronoss20/fake-news-detector/settings/pages)
- 📊 [Actions (Deployment Status)](https://github.com/cronoss20/fake-news-detector/actions)
- 📖 [Complete Documentation](GITHUB_PAGES.md)
