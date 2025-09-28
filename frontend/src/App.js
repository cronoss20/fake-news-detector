import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

function App() {
  const [inputType, setInputType] = useState('text');
  const [inputValue, setInputValue] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleAnalyze = async () => {
    if (!inputValue.trim()) {
      setError('Please enter some text or a URL to analyze');
      return;
    }

    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const endpoint = inputType === 'text' ? '/predict' : '/analyze';
      const data = inputType === 'text' 
        ? { text: inputValue }
        : { url: inputValue };

      const response = await axios.post(`${API_BASE_URL}${endpoint}`, data);
      
      if (response.data.success) {
        setResult(response.data);
      } else {
        setError('Analysis failed. Please try again.');
      }
    } catch (err) {
      if (err.response && err.response.data && err.response.data.error) {
        setError(err.response.data.error);
      } else if (err.code === 'ECONNREFUSED') {
        setError('Cannot connect to the backend server. Please make sure it\'s running.');
      } else {
        setError('An error occurred while analyzing. Please try again.');
      }
    } finally {
      setLoading(false);
    }
  };

  const handleClear = () => {
    setInputValue('');
    setResult(null);
    setError(null);
  };

  return (
    <div className="App">
      <div className="container">
        <header className="header">
          <h1>🕵️ Fake News Detector</h1>
          <p>Analyze text or articles to detect potential misinformation using AI</p>
        </header>

        <div className="input-section">
          <div className="input-type-selector">
            <button 
              className={inputType === 'text' ? 'active' : ''}
              onClick={() => setInputType('text')}
            >
              📝 Text Analysis
            </button>
            <button 
              className={inputType === 'url' ? 'active' : ''}
              onClick={() => setInputType('url')}
            >
              🔗 URL Analysis
            </button>
          </div>

          <div className="input-container">
            {inputType === 'text' ? (
              <textarea
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
                placeholder="Enter the text you want to analyze for fake news detection..."
                rows={8}
                className="text-input"
              />
            ) : (
              <input
                type="url"
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
                placeholder="Enter a URL to analyze (e.g., https://example.com/article)"
                className="url-input"
              />
            )}
          </div>

          <div className="button-container">
            <button 
              onClick={handleAnalyze}
              disabled={loading || !inputValue.trim()}
              className="analyze-button"
            >
              {loading ? '🔄 Analyzing...' : '🚀 Analyze'}
            </button>
            <button 
              onClick={handleClear}
              className="clear-button"
            >
              🧹 Clear
            </button>
          </div>
        </div>

        {error && (
          <div className="error-container">
            <h3>❌ Error</h3>
            <p>{error}</p>
          </div>
        )}

        {result && (
          <div className="result-container">
            <h3>📊 Analysis Results</h3>
            
            <div className="result-summary">
              <div className={`result-status ${result.analysis.is_fake ? 'fake' : 'legitimate'}`}>
                <span className="status-icon">
                  {result.analysis.is_fake ? '⚠️' : '✅'}
                </span>
                <span className="status-text">
                  {result.analysis.is_fake ? 'Potentially Fake News' : 'Likely Legitimate'}
                </span>
              </div>
              
              <div className="confidence-meter">
                <label>Confidence Level: {result.analysis.confidence}%</label>
                <div className="confidence-bar">
                  <div 
                    className="confidence-fill"
                    style={{ width: `${result.analysis.confidence}%` }}
                  ></div>
                </div>
              </div>
            </div>

            <div className="result-details">
              <div className="reasoning">
                <h4>💭 Analysis Reasoning</h4>
                <p>{result.analysis.reasoning}</p>
              </div>

              {result.analysis.red_flags && result.analysis.red_flags.length > 0 && (
                <div className="red-flags">
                  <h4>🚩 Red Flags Detected</h4>
                  <ul>
                    {result.analysis.red_flags.map((flag, index) => (
                      <li key={index}>{flag}</li>
                    ))}
                  </ul>
                </div>
              )}

              {result.content_preview && (
                <div className="content-preview">
                  <h4>📰 Content Preview</h4>
                  <p className="preview-text">{result.content_preview}</p>
                  <small>Analyzed {result.content_length} characters from the URL</small>
                </div>
              )}

              {result.text_length && (
                <div className="analysis-meta">
                  <small>Analyzed {result.text_length} characters of text</small>
                </div>
              )}
            </div>
          </div>
        )}

        <footer className="footer">
          <p>
            <strong>Disclaimer:</strong> This tool provides AI-powered analysis to help identify potential misinformation. 
            Results should be verified with reliable sources. Always practice critical thinking and fact-checking.
          </p>
        </footer>
      </div>
    </div>
  );
}

export default App;
