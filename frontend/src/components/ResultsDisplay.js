import React from "react";

function ResultsDisplay({ results }) {
  return (
    <div className="results-display">
      <h2>Analysis Results</h2>
      <p>
        <strong>Likelihood of Fake News: </strong>
        <span className={results.is_fake ? "fake" : "real"}>
          {results.is_fake ? "Likely Fake" : "Likely Real"}
        </span>
      </p>
      <p>
        <strong>Confidence:</strong> {results.confidence}%
      </p>
      {results.red_flags && results.red_flags.length > 0 && (
        <div>
          <strong>Red Flags:</strong>
          <ul>
            {results.red_flags.map((flag, i) => (
              <li key={i}>{flag}</li>
            ))}
          </ul>
        </div>
      )}
      {results.reasoning && (
        <div>
          <strong>Reasoning:</strong>
          <pre>{results.reasoning}</pre>
        </div>
      )}
      {results.extracted && (
        <details>
          <summary>Extracted Article Content</summary>
          <div className="extracted">{results.extracted}</div>
        </details>
      )}
      {results.mode && (
        <div className="mode-indicator">
          <small>Analysis Mode: {results.mode === "gpt" ? "AI (OpenAI)" : "Demo/Heuristic"}</small>
        </div>
      )}
    </div>
  );
}

export default ResultsDisplay;
