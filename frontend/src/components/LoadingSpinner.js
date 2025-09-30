import React from "react";

function LoadingSpinner() {
  return (
    <div className="spinner">
      <div className="lds-dual-ring"></div>
      <span>Analyzing...</span>
    </div>
  );
}

export default LoadingSpinner;
