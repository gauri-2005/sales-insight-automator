import React, { useState } from "react";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [email, setEmail] = useState("");
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();

    setLoading(true);

    const formData = new FormData();
    formData.append("file", file);
    formData.append("email", email);

    try {
      const res = await fetch("http://127.0.0.1:8000/upload", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();
      setMessage(data.message || data.error);
    } catch (err) {
      setMessage("Something went wrong.");
    }

    setLoading(false);
  };

  return (
    <div className="app">

      <div className="card">

        <h1>AI Sales Insight Automator</h1>

        <p className="subtitle">
          Upload your sales CSV and get AI-powered insights instantly.
        </p>

        <form onSubmit={handleSubmit}>

          <input
            type="file"
            onChange={(e) => setFile(e.target.files[0])}
            required
          />

          <input
            type="email"
            placeholder="Enter your email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />

          <button type="submit">
            {loading ? "Generating..." : "Generate Insights"}
          </button>

        </form>

        {message && <div className="result">{message}</div>}

      </div>

    </div>
  );
}

export default App;