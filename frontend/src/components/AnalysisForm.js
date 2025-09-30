import React, { useState } from "react";

function AnalysisForm({ onTextAnalysis, onUrlAnalysis }) {
  const [mode, setMode] = useState("text");
  const [text, setText] = useState("");
  const [url, setUrl] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (mode === "text") {
      onTextAnalysis(text);
    } else {
      onUrlAnalysis(url);
    }
  };

  return (
    <div className="analysis-form">
      <div className="toggle-group">
        <button
          className={mode === "text" ? "active" : ""}
          onClick={() => setMode("text")}
        >
          Analyze Text
        </button>
        <button
          className={mode === "url" ? "active" : ""}
          onClick={() => setMode("url")}
        >
          Analyze URL
        </button>
      </div>
      <form onSubmit={handleSubmit}>
        {mode === "text" ? (
          <textarea
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder="Paste news text here..."
            required
            rows={5}
          />
        ) : (
          <input
            type="url"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            placeholder="Enter news article URL..."
            required
          />
        )}
        <button type="submit">Analyze</button>
      </form>
    </div>
  );
}

export default AnalysisForm;
