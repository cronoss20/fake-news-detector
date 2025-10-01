# Deployment Scripts

This directory contains automated deployment scripts for various hosting platforms.

## Available Scripts

### 1. render-deploy.sh
Deploys to Render.com (recommended for beginners)
- Backend and frontend deployment
- Free tier available
- Automatic SSL/HTTPS

**Usage:**
```bash
./deploy/render-deploy.sh
```

### 2. railway-deploy.sh
Deploys to Railway.app
- All-in-one deployment
- Auto-detects services
- Simple CLI interface

**Usage:**
```bash
./deploy/railway-deploy.sh
```

### 3. vercel-render-deploy.sh
Hybrid deployment: Vercel (frontend) + Render (backend)
- Best performance for frontend
- Separate backend scaling

**Usage:**
```bash
./deploy/vercel-render-deploy.sh
```

## Prerequisites

Before running any script:
1. Fork this repository to your GitHub account
2. Install required CLI tools (scripts will guide you)
3. Create accounts on hosting platforms
4. Have your OpenAI API key ready (optional)

## Platform Comparisons

| Platform | Free Tier | Setup Time | Best For |
|----------|-----------|------------|----------|
| Render | ✅ Yes | 5 min | Beginners |
| Railway | ✅ Yes | 5 min | All-in-one |
| Vercel + Render | ✅ Yes | 7 min | Performance |

## Manual Deployment

If you prefer manual deployment without scripts, see [DEMO.md](../DEMO.md) for detailed instructions.

## Troubleshooting

### Script Permission Denied
```bash
chmod +x deploy/*.sh
```

### CLI Tool Not Found
Follow the installation instructions provided by each script.

### Environment Variables
Make sure to set:
- `OPENAI_API_KEY` (optional) for backend
- `REACT_APP_BACKEND_URL` for frontend

## Support

For issues with deployment scripts:
1. Check [DEMO.md](../DEMO.md) for detailed guides
2. Review [SECURITY.md](../SECURITY.md) for security setup
3. Open an issue on GitHub
