import React, { useState } from "react";
import "../css/FileUpload.css";

const FileUpload = () => {
  const [file, setFile] = useState(null);
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) return;
    setLoading(true);
    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://localhost:8000/summarise/", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      console.log(data)
      setSummary(data.summary);
    } catch (error) {
      console.error("Error uploading file:", error);
      setSummary("An error occurred while uploading the PDF.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <div className="card">
        <h1 className="title">Upload PDF to Get Summary</h1>
        <input type="file" accept="application/pdf" onChange={handleFileChange} className="file-input" />
        <button onClick={handleUpload} disabled={loading} className="upload-button">
          {loading ? "Summarizing..." : "Upload and Summarize"}
        </button>
        <textarea
          className="summary-textarea"
          value={summary}
          readOnly
          placeholder="Summary will appear here..."
        />
      </div>
    </div>
  );
};

export default FileUpload;