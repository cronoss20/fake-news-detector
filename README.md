# 🕵️ Fake News Detector

An AI-powered fake news detection system that analyzes text content and URLs to identify potential misinformation using OpenAI's GPT model.

## ✨ Features

- **Text Analysis**: Directly analyze text content for fake news indicators
- **URL Analysis**: Extract and analyze content from news articles and web pages
- **AI-Powered Detection**: Uses OpenAI GPT-3.5-turbo for intelligent analysis
- **Confidence Scoring**: Provides confidence percentages for analysis results
- **Red Flag Detection**: Identifies specific concerning elements in the content
- **Responsive Web Interface**: Clean, modern React frontend
- **REST API**: Flask backend with clear endpoints

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Node.js 14 or higher
- OpenAI API key (required for AI analysis)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/cronoss20/fake-news-detector.git
   cd fake-news-detector
   ```

2. **Set up the Backend**
   ```bash
   cd backend
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Set up environment variables
   cp .env.example .env
   # Edit .env and add your OpenAI API key
   ```

3. **Set up the Frontend**
   ```bash
   cd ../frontend
   npm install
   ```

4. **Configure API Key**
   - Get an OpenAI API key from [OpenAI Platform](https://platform.openai.com/api-keys)
   - Add it to `backend/.env`:
     ```
     OPENAI_API_KEY=your_actual_api_key_here
     ```

### Running the Application

1. **Start the Backend** (Terminal 1)
   ```bash
   cd backend
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   python app.py
   ```
   Backend will run on `http://localhost:5000`

2. **Start the Frontend** (Terminal 2)
   ```bash
   cd frontend
   npm start
   ```
   Frontend will run on `http://localhost:3000`

3. **Open your browser** and go to `http://localhost:3000`

## 📖 Usage

### Text Analysis
1. Select "📝 Text Analysis" tab
2. Enter or paste the text you want to analyze
3. Click "🚀 Analyze" to get results
4. Review the confidence score, reasoning, and red flags

### URL Analysis
1. Select "🔗 URL Analysis" tab
2. Enter a URL to a news article or web page
3. Click "🚀 Analyze" to extract and analyze the content
4. Review the analysis results and content preview

### Understanding Results

- **✅ Likely Legitimate**: Content appears to be factual and reliable
- **⚠️ Potentially Fake News**: Content shows signs of misinformation
- **Confidence Level**: Percentage indicating how certain the AI is about its assessment
- **Red Flags**: Specific concerning elements detected in the content

## 🔧 API Reference

### Base URL
```
http://localhost:5000
```

### Endpoints

#### Health Check
```
GET /
```
Returns API status and available endpoints.

#### Text Analysis
```
POST /predict
Content-Type: application/json

{
  "text": "Text content to analyze"
}
```

#### URL Analysis
```
POST /analyze
Content-Type: application/json

{
  "url": "https://example.com/article"
}
```

### Response Format
```json
{
  "success": true,
  "analysis": {
    "is_fake": false,
    "confidence": 75,
    "reasoning": "Analysis explanation...",
    "red_flags": ["List of concerns"]
  },
  "content_length": 1234,
  "content_preview": "Preview of analyzed content..."
}
```

## 🐳 Docker Deployment (Optional)

### Backend Dockerfile
Create `backend/Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

### Frontend Dockerfile
Create `frontend/Dockerfile`:
```dockerfile
FROM node:16-alpine as build

WORKDIR /app
COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

### Docker Compose
Create `docker-compose.yml` in the root directory:
```yaml
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "5000:5000"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    volumes:
      - ./backend:/app

  frontend:
    build: ./frontend
    ports:
      - "3000:80"
    depends_on:
      - backend
```

Run with: `docker-compose up`

## 🌐 Production Deployment

### Backend (Render/Heroku)

#### Render Deployment
1. Connect your repository to Render
2. Create a new Web Service
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `gunicorn app:app`
5. Add environment variable: `OPENAI_API_KEY`

#### Heroku Deployment
1. Install Heroku CLI
2. Create `Procfile` in backend directory:
   ```
   web: gunicorn app:app
   ```
3. Deploy:
   ```bash
   heroku create your-app-name
   heroku config:set OPENAI_API_KEY=your_api_key
   git push heroku main
   ```

### Frontend (GitHub Pages)

1. **Build for production**
   ```bash
   cd frontend
   npm run build
   ```

2. **Deploy to GitHub Pages**
   ```bash
   npm install -g gh-pages
   
   # Add to package.json:
   "homepage": "https://yourusername.github.io/fake-news-detector",
   "scripts": {
     ...
     "predeploy": "npm run build",
     "deploy": "gh-pages -d build"
   }
   
   npm run deploy
   ```

3. **Update API URL**
   - Set `REACT_APP_API_URL` environment variable to your backend URL
   - For GitHub Pages, create `.env.production`:
     ```
     REACT_APP_API_URL=https://your-backend-url.com
     ```

## ⚠️ Important Notes

### Disclaimer
This tool provides AI-powered analysis to help identify potential misinformation. Results should always be verified with reliable sources. The tool is designed to assist, not replace, critical thinking and proper fact-checking.

### API Key Security
- Never commit your OpenAI API key to version control
- Use environment variables for API keys
- Rotate API keys regularly
- Monitor API usage to prevent abuse

### Rate Limits
- OpenAI API has rate limits based on your plan
- Consider implementing caching for repeated requests
- Monitor API costs and usage

## 🛠️ Development

### Project Structure
```
fake-news-detector/
├── backend/
│   ├── app.py                 # Main Flask application
│   ├── fake_news_detector.py  # AI detection logic
│   ├── text_processor.py      # Text processing utilities
│   ├── requirements.txt       # Python dependencies
│   └── .env.example          # Environment variables template
├── frontend/
│   ├── src/
│   │   ├── App.js            # Main React component
│   │   ├── App.css           # Styles
│   │   └── index.js          # React entry point
│   ├── package.json          # Node dependencies
│   └── public/               # Static assets
└── README.md                 # This file
```

### Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

### Testing
- Backend: Add unit tests for API endpoints
- Frontend: Use React Testing Library for component tests
- Integration: Test full workflow with sample data

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section below
2. Open an issue on GitHub
3. Review the API documentation

### Troubleshooting

**Backend won't start:**
- Verify Python virtual environment is activated
- Check that all dependencies are installed
- Ensure OpenAI API key is set correctly

**Frontend can't connect to backend:**
- Verify backend is running on port 5000
- Check CORS settings
- Ensure API URL is correct in frontend

**Analysis fails:**
- Verify OpenAI API key is valid and has credits
- Check internet connection for URL analysis
- Ensure text meets minimum length requirements

**URL analysis not working:**
- Some websites block scraping
- Try different URLs
- Check if the website requires special headers or authentication