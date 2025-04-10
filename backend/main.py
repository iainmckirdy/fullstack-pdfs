from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import tempfile
import shutil
from summarise import summarise_pdf  # Replace with actual import path

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React app is likely on this port
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.post("/summarise/")
async def summarise_endpoint(file: UploadFile = File(...), use_local: bool = False):
    # Save uploaded file to a temp location
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        shutil.copyfileobj(file.file, tmp)
        tmp_path = tmp.name

    try:
        summary = summarise_pdf(tmp_path, use_local=use_local)
        return {"summary": summary}
    except Exception as e:
        return {"error": str(e)}