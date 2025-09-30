This PR implements a complete fake news detection system that analyzes text content and URLs to identify potential misinformation using OpenAI's GPT model, with a beautiful React frontend interface.

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

- `backend/` - Complete Flask application with AI integration
- `frontend/` - React application with modern UI/UX
- `README.md` - Comprehensive documentation and setup guide
- `docker-compose.yml` - Container orchestration
- Development and deployment configuration files

This implementation provides a production-ready fake news detection system that combines modern web technologies with AI-powered analysis, making it easy for users to identify potential misinformation in text content and news articles.

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

<!-- START COPILOT CODING AGENT SUFFIX -->



<details>

<summary>Original prompt</summary>

> Crear un repositorio funcional en "fake-news-detector" que detecte noticias falsas utilizando IA (GPT) y proporcione una interfaz web con React. Los componentes que se necesitan son los siguientes:
> 
> 1. **Backend con Flask (Python):**
>    - Implementar un servidor Flask que reciba texto y URLs.
>    - Integrar un modelo de lenguaje basado en GPT (puede ser OpenAI API o Hugging Face).
>    - Procesar el texto o el contenido obtenido desde el enlace y devolver si es "Fake News" junto con un porcentaje de confianza.
>    - Crear endpoints `/predict` y `/analyze`.
> 
> 2. **Frontend con React:**
>    - Una página principal que permita:
>      - Ingresar texto o un enlace.
>      - Enviar la solicitud al backend y mostrar los resultados.
>    - Diseño sencillo pero funcional.
> 
> 3. **Integración y Despliegue:**
>    - Incluir un archivo de configuración para ejecutar el backend y frontend juntos.
>    - Proporcionar un archivo README.md con instrucciones para la instalación, ejecución y uso del sistema.
> 
> 4. **Extras:**
>    - Añadir soporte para Docker (opcional).
>    - Usar GitHub Pages para desplegar el frontend y proporcionar instrucciones para desplegar el backend en una plataforma como Render o Heroku.


</details>
*This pull request was created as a result of the following prompt from Copilot chat.*
> Crear un repositorio funcional en "fake-news-detector" que detecte noticias falsas utilizando IA (GPT) y proporcione una interfaz web con React. Los componentes que se necesitan son los siguientes:
> 
> 1. **Backend con Flask (Python):**
>    - Implementar un servidor Flask que reciba texto y URLs.
>    - Integrar un modelo de lenguaje basado en GPT (puede ser OpenAI API o Hugging Face).
>    - Procesar el texto o el contenido obtenido desde el enlace y devolver si es "Fake News" junto con un porcentaje de confianza.
>    - Crear endpoints `/predict` y `/analyze`.
> 
> 2. **Frontend con React:**
>    - Una página principal que permita:
>      - Ingresar texto o un enlace.
>      - Enviar la solicitud al backend y mostrar los resultados.
>    - Diseño sencillo pero funcional.
> 
> 3. **Integración y Despliegue:**
>    - Incluir un archivo de configuración para ejecutar el backend y frontend juntos.
>    - Proporcionar un archivo README.md con instrucciones para la instalación, ejecución y uso del sistema.
> 
> 4. **Extras:**
>    - Añadir soporte para Docker (opcional).
>    - Usar GitHub Pages para desplegar el frontend y proporcionar instrucciones para desplegar el backend en una plataforma como Render o Heroku.

<!-- START COPILOT CODING AGENT TIPS -->
---

✨ Let Copilot coding agent [set things up for you](https://github.com/cronoss20/fake-news-detector/issues/new?title=✨+Set+up+Copilot+instructions&body=Configure%20instructions%20for%20this%20repository%20as%20documented%20in%20%5BBest%20practices%20for%20Copilot%20coding%20agent%20in%20your%20repository%5D%28https://gh.io/copilot-coding-agent-tips%29%2E%0A%0A%3COnboard%20this%20repo%3E&assignees=copilot) — coding agent works faster and does higher quality work when set up for your repo.
