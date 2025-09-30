import React from "react";

function ErrorMessage({ message }) {
  return (
    <div className="error">
      <strong>Error:</strong> {message}
    </div>
  );
}

export default ErrorMessage;
