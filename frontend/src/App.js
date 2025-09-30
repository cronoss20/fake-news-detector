import React, { useState } from "react";
import AnalysisForm from "./components/AnalysisForm";
import ResultsDisplay from "./components/ResultsDisplay";
import LoadingSpinner from "./components/LoadingSpinner";
import ErrorMessage from "./components/ErrorMessage";
import axios from "axios";

const backendUrl = process.env.REACT_APP_BACKEND_URL || "http://localhost:5000";

function App() {
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState(null);
  const [error, setError] = useState(null);

  const handleTextAnalysis = async (text) => {
    setLoading(true);
    setError(null);
    setResults(null);
    try {
      const { data } = await axios.post(`${backendUrl}/predict`, { text });
      setResults(data);
    } catch (err) {
      setError(err.response?.data?.error || "Error analyzing text");
    }
    setLoading(false);
  };

  const handleUrlAnalysis = async (url) => {
    setLoading(true);
    setError(null);
    setResults(null);
    try {
      const { data } = await axios.post(`${backendUrl}/analyze`, { url });
      setResults(data);
    } catch (err) {
      setError(err.response?.data?.error || "Error analyzing URL");
    }
    setLoading(false);
  };

  return (
    <div className="app-container">
      <h1>📰 Fake News Detector</h1>
      <AnalysisForm
        onTextAnalysis={handleTextAnalysis}
        onUrlAnalysis={handleUrlAnalysis}
      />
      {loading && <LoadingSpinner />}
      {error && <ErrorMessage message={error} />}
      {results && <ResultsDisplay results={results} />}
      <footer>
        <small>
          Powered by OpenAI | <a href="https://github.com/cronoss20/fake-news-detector">GitHub</a>
        </small>
      </footer>
    </div>
  );
}

export default App;
