# 📄 PDF Summarizer API

This is a FastAPI backend service that takes in PDF files and returns AI-generated summaries using either OpenAI or a local LLM (like Ollama's LLaMA).

## Features

- Upload a PDF and receive a summarised version via API
- Supports both OpenAI (`gpt-3.5-turbo`) and local models (`llama3`)
- Efficient file handling and concurrency-safe with `asyncio`
- React frontend compatible for easy integration

## Tech Stack

- FastAPI
- LangChain
- OpenAI or Ollama (for LLMs)
- React (Frontend, optional)

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/iainmckirdy/fullstack-pdfs.git
cd fullstack-pdfs
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```
### 3. Create a .env file

```
OPENAI_API_KEY=your-openai-api-key
```
### 4. Run the FastAPI app

```bash
cd backend
uvicorn main:app --reload
```

## API Usage
### POST `/summarise/`

#### Request:

- `multipart/form-data` with:

    - `file`: the PDF to summarise

    - `use_local` (optional query param): `true` to use local model, otherwise defaults to OpenAI

#### Example with cURL:

```bash
curl -X POST "http://localhost:8000/summarise/?use_local=false" \
  -F "file=@example.pdf"
```
#### Response:

```json
{
  "summary": "This document covers the following key points..."
}
```
## Frontend (Optional)
You can use the provided React component (see `FileUpload.jsx`) to let users upload PDFs through a web UI. The frontend sends a `FormData` object to the backend and displays the returned summary.

## Notes
If using a local model like LLaMA with Ollama, ensure the model is already running:

```bash
ollama run llama3
```
For large PDFs, the API processes them efficiently by streaming uploads to a temporary file.

Temporary files are cleaned up after use to avoid storage issues.

License:
MIT


